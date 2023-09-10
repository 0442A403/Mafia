import logging
from typing import Dict
from common import Session
from common.player import Player
from common.player_role import PlayerRole
from common.session_state import SessionState
from scheme.engine_pb2 import (
    GetNotificationsResponse,
    CreateGameResponse,
    ConnectResponse,
    GetStateResponse,
    PlayerState, LynchChooseResponse, MafiaChooseResponse, DetectiveChooseResponse, StartGameResponse,
)
from utils.random_id import generate_random_id
from scheme.engine_pb2_grpc import MafiaEngineServicer


class Engine(MafiaEngineServicer):
    def __init__(self, single, max_players, default_mafia_count, default_detective_count):
        super().__init__()
        self.sessions: Dict[str, Session] = {}
        self.default_mafia_count = default_mafia_count
        self.default_detective_count = default_detective_count
        if single:
            self.sessions["0"] = Session("0", max_players)

    def CreateGame(self, request, context):
        session_id = generate_random_id()
        self.sessions[session_id] = Session(session_id)

        return CreateGameResponse(session_id=session_id)

    def Connect(self, request, context):
        user_key = generate_random_id()
        session_id = request.session_id
        username = request.username
        player = Player(username)
        session = self.sessions[session_id]
        ok = session.connect(user_key, player)
        if not ok:
            return ConnectResponse(ok=False)

        if len(session.players) == session.max_players:
            session.start(self.default_mafia_count, self.default_detective_count)

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
        session = self.sessions[session_id]

        response = GetStateResponse(
            day_stage=session.day_stage.value,
            session_state=session.session_state.value,
            session_id=session_id,
        )

        for player_key, player in session.players.items():
            player_pb = PlayerState(username=player.username, is_alive=player.is_alive)
            if player_key == user_key:
                player_pb.role = 0 if player.role is None else player.role.value
            response.players.append(player_pb)

        role = session.players[user_key].role
        if role == PlayerRole.MAFIA and session.mafia_chat is not None:
            response.mafia_chat = session.mafia_chat
        elif role == PlayerRole.DETECTIVE and session.detective_chat is not None:
            response.detective_chat = session.detective_chat

        return response

    def StartGame(self, request, context):
        session_id = request.session_id
        mafia_count = request.mafia_count if request.mafia_count > 0 else self.default_mafia_count
        detective_count = request.detective_count if request.detective_count > 0 else self.default_detective_count

        ok = self.sessions[session_id].start(mafia_count, detective_count)

        return StartGameResponse(ok=ok)

    def LynchChoose(self, request, context):
        session_id = request.session_id
        user_key = request.user_key
        choose_player = request.choose_player

        ok = self.sessions[session_id].lynch(user_key, choose_player)

        return LynchChooseResponse(ok=ok)

    def MafiaChoose(self, request, context):
        session_id = request.session_id
        user_key = request.user_key
        choose_player = request.choose_player

        ok = self.sessions[session_id].mafia_choose(user_key, choose_player)

        return MafiaChooseResponse(ok=ok)

    def DetectiveChoose(self, request, context):
        session_id = request.session_id
        user_key = request.user_key
        choose_player = request.choose_player

        ok = self.sessions[session_id].detective_choose(user_key, choose_player)

        return DetectiveChooseResponse(ok=ok)
