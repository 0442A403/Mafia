import random
import time

from common.day_stage import DayStage
from common.player_role import PlayerRole
from common.session_state import SessionState
from scheme.engine_pb2 import DAY_STAGE_DAY, DAY_STAGE_NIGHT_MAFIA, DAY_STAGE_NIGHT_DETECTIVE
from client import Client


BOT_USERNAMES = ["Olivia", "Amelia", "Isla", "Ava", "Ivy", "Florence", "Lily", "Freya", "Mia", "Willow"]


class MafiaClient(Client):
    def __init__(self, host, session_id):
        super().__init__(host)
        self.session_id = session_id

    def next_command(self):
        while not self.is_connected:
            yield ["connect", str(self.session_id), random.choice(BOT_USERNAMES)]

        while True:
            time.sleep(1)
            available_commands = self.get_available_commands()
            if not available_commands:
                yield []
            else:
                yield random.choice(available_commands)

    def get_available_commands(self):
        if self.me is not None and not self.me.is_alive:
            return []

        commands = []

        if self.session_state == SessionState.PLAYING:
            if self.day_stage == DayStage.DAY:
                for player in self.get_alive_players():
                    commands.append(["lynch", player])
            elif self.day_stage == DayStage.NIGHT_MAFIA:
                if self.me.role == PlayerRole.MAFIA:
                    for player in self.get_alive_players():
                        commands.append(["mafia_choose", player])
            elif self.day_stage == DayStage.NIGHT_DETECTIVE:
                if self.me.role == PlayerRole.DETECTIVE:
                    for player in self.get_alive_players():
                        pass
                        #commands.append(["detective_choose", player])

        return commands

    def get_alive_players(self, me=False):
        result = []
        for player in self.players:
            if player.is_alive and (me or player.username != self.me.username):
                result.append(player.username)
        return result
