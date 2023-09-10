import logging
from typing import Dict
from common import Session
from common.player import Player
from scheme.engine_pb2 import (
    GetNotificationsResponse,
    CreateGameResponse,
    ConnectResponse,
    GetStateResponse,
    PlayerState,
)
from utils.random_id import generate_random_id
from scheme.engine_pb2_grpc import MafiaEngineServicer


class Engine(MafiaEngineServicer):
    def __init__(self, single=False, max_players=None):
        super().__init__()
        self.sessions: Dict[str, Session] = {}
        self.max_players = max_players
        if single:
            self.sessions["0"] = Session("0")

    def CreateGame(self, request, context):
        session_id = generate_random_id()
        self.sessions[session_id] = Session(session_id)

        return CreateGameResponse(session_id=session_id)

    def Connect(self, request, context):
        user_key = generate_random_id()
        session_id = request.session_id
        username = request.username
        player = Player(username)
        self.sessions[session_id].connect(user_key, player)
        self.sessions[session_id].notify(f"Player {username} connected")

        return ConnectResponse(user_key=user_key, ok=True)

    def GetNotifications(self, request, context):
        user_key = request.user_key
        session_id = request.session_id
        notifications = self.sessions[session_id].pop_notifications(user_key)

        response = GetNotificationsResponse(notifications=notifications)
        return response

    def GetState(self, request, context):
        user_key = request.user_key
        session_id = request.session_id

        response = GetStateResponse(day_stage=self.sessions[session_id].day_stage.value)
        for player_key, player in self.sessions[session_id].players.items():
            player_pb = PlayerState(username=player.username, is_alive=player.is_alive)
            if player_key == user_key:
                player_pb.role = 0 if player.role is None else player.role.value
            response.players.append(player_pb)

        return response

    def StartGame(self, request, context):
        session_id = request.session_id
        self.sessions[session_id].start()