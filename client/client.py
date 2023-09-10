import threading

import grpc

from notifications import loop_notification_check
from scheme.engine_pb2 import CreateGameRequest, ConnectRequest
from scheme.engine_pb2_grpc import MafiaEngineStub
from state_updating import loop_state_updater


class Client:

    def __init__(self, host):
        self.client = MafiaEngineStub(grpc.insecure_channel(host))
        self.commands = {
            "help": Client.help,
            "create_game": Client.create_game,
            "connect": Client.connect,
        }
        self.day_stage = None
        self.session_state = None
        self.players = []
        self.me = None
        self.username = None
        self.user_key = None
        self.session_id = None
        self.notification_thread = None
        self.state_updater_thread = None
        self.is_connected = False

    def next_command(self):
        print("Welcome! This is client for mafia game. Type 'help' if you need help")
        while True:
            command = input().split()
            yield command

    def help(self):
        print("This is mafia client. Use [command] [<args>]")
        print(f"Available commands: {list(self.commands.keys())}")

    def create_game(self):
        response = self.client.CreateGame(CreateGameRequest())
        print(f"Game {response.session_id} created")

    def connect(self, session_id, username):
        response = self.client.Connect(ConnectRequest(session_id=session_id, username=username))
        if not response.ok:
            print("Failed to connect")
            return

        self.session_id = session_id
        self.user_key = response.user_key
        self.username = username
        self.is_connected = True

        self.notification_thread = threading.Thread(
            target=loop_notification_check, args=(self.client, session_id, self.user_key))
        self.notification_thread.start()

        self.state_updater_thread = threading.Thread(
            target=loop_state_updater, args=(self.client, session_id, self.user_key, self))
        self.state_updater_thread.start()

