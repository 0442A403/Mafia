import time

from common.day_stage import DayStage
from common.player import Player
from common.session_state import SessionState
from scheme.engine_pb2 import GetStateRequest


def loop_state_updater(engine, session_id, user_key, client):
    for request in get_client_request(session_id, user_key):
        response = engine.GetState(request)

        client.session_state = SessionState(response.session_state)
        client.day_stage = DayStage(response.day_stage)
        players = []
        for player in response.players:
            players.append(Player(player.username, player.is_alive, None if not player.role else player.role))
            if client.username == player.username:
                client.me = player

        time.sleep(0.5)


def get_client_request(session_id, user_key):
    while True:
        yield GetStateRequest(session_id=session_id, user_key=user_key)
