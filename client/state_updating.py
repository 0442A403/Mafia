import time

from common.day_stage import DayStage
from common.player import Player
from common.player_role import PlayerRole
from common.session_state import SessionState
from scheme.engine_pb2 import GetStateRequest


def loop_state_updater(engine, session_id, user_key, client):
    for request in get_client_request(session_id, user_key):
        response = engine.GetState(request)

        players = []
        for player in response.players:
            players.append(Player(player.username, player.is_alive, PlayerRole(player.role)))
            if client.username == player.username:
                client.me = players[-1]

        client.players = players
        client.session_state = SessionState(response.session_state)
        client.day_stage = DayStage(response.day_stage)

        if client.mafia_chat_id is None \
                and client.detective_chat_id is None \
                and (response.mafia_chat or response.detective_chat):
            client.mafia_chat_id = response.mafia_chat
            client.detective_chat_id = response.detective_chat
            client.update_chats()

        time.sleep(0.25)


def get_client_request(session_id, user_key):
    while True:
        yield GetStateRequest(session_id=session_id, user_key=user_key)
