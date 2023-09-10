import threading
import grpc
from chat import Chat
from common.day_stage import DayStage
from common.player import Player
from common.player_role import PlayerRole
from notifications import loop_notification_check
from scheme.engine_pb2 import (
    CreateGameRequest,
    ConnectRequest,
    StartGameRequest,
    LynchChooseRequest,
    MafiaChooseRequest,
    DetectiveChooseRequest,
)
from scheme.engine_pb2_grpc import MafiaEngineStub
from state_updating import loop_state_updater


class Client:

    def __init__(self, host, chat_host, chat_port):
        self.client = MafiaEngineStub(grpc.insecure_channel(host))
        self.commands = {
            "help": Client.help,
            "create_game": Client.create_game,
            "connect": Client.connect,
            "start_game": Client.start_game,
            "lynch": Client.lynch,
            "mafia_choose": Client.mafia_choose,
            "detective_choose": Client.detective_choose,
            "chat": Client.send_message,
        }
        self.day_stage = None
        self.session_state = None
        self.players = []
        self.me: Player = None
        self.username = None
        self.user_key = None
        self.session_id = None
        self.notification_thread = None
        self.state_updater_thread = None
        self.is_connected = False
        self.chat_host = chat_host
        self.chat_port = chat_port
        self.citizen_chat = None
        self.mafia_chat = None
        self.mafia_chat_id = None
        self.detective_chat = None
        self.detective_chat_id = None
        self.bot = False

    def next_command(self):
        print("Welcome! This is client for mafia game. Type 'help' if you need help")
        while True:
            inp = input()
            command = inp.split()
            yield command, inp

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

        if not self.bot:
            self.citizen_chat = Chat(self.chat_host, self.chat_port, self.session_id, self.username)
            self.citizen_chat.start()

    def start_game(self, mafia_count, detective_count):
        mafia_count = int(mafia_count)
        detective_count = int(detective_count)
        response = self.client.StartGame(StartGameRequest(
            session_id=self.session_id,
            user_key=self.user_key,
            mafia_count=mafia_count,
            detective_count=detective_count))

        if not response.ok:
            print("Failed to start game. Check mafia and detective counts.")

    def lynch(self, username):
        self.client.LynchChoose(LynchChooseRequest(
            session_id=self.session_id,
            user_key=self.user_key,
            choose_player=username
        ))

    def mafia_choose(self, username):
        self.client.MafiaChoose(MafiaChooseRequest(
            session_id=self.session_id,
            user_key=self.user_key,
            choose_player=username
        ))

    def detective_choose(self, username):
        self.client.DetectiveChoose(DetectiveChooseRequest(
            session_id=self.session_id,
            user_key=self.user_key,
            choose_player=username
        ))

    def update_chats(self):
        if self.bot:
            return

        if self.me.role == PlayerRole.MAFIA and self.mafia_chat is None:
            self.mafia_chat = Chat(self.chat_host, self.chat_port, self.mafia_chat_id, self.username)
            self.mafia_chat.start()
        elif self.me.role == PlayerRole.DETECTIVE and self.detective_chat is None:
            self.detective_chat = Chat(self.chat_host, self.chat_port, self.detective_chat_id, self.username)
            self.detective_chat.start()

    def send_message(self, message):
        if not self.me.is_alive:
            print("You can't send messages after death")
            return
        if self.day_stage == DayStage.DAY:
            self.citizen_chat.send_message(message)
        elif self.day_stage == DayStage.NIGHT_MAFIA:
            if self.me.role == PlayerRole.MAFIA:
                self.mafia_chat.send_message(message)
            else:
                print("You can't send message now")
        elif self.day_stage == DayStage.NIGHT_DETECTIVE:
            if self.me.role == PlayerRole.DETECTIVE:
                self.detective_chat.send_message(message)
            else:
                print("You can't send message now")
