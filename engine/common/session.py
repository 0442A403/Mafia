import copy
import random
from typing import Dict

from common.day_stage import DayStage
from common.player import Player
from common.player_role import PlayerRole
from common.session_state import SessionState


class Session:
    def __init__(self, session_id, max_players):
        self.session_id = session_id
        self.players: Dict[str, Player] = {}
        self.notifications = {}
        self.day_stage = DayStage.DAY
        self.session_state = SessionState.NOT_STARTED
        self.max_players = max_players
        self.username_to_user_key = {}
        self.voting = {}
        self.votes = 0

    def notify(self, notification, targets=None):
        if not targets:
            targets = self.players.keys()

        for target in targets:
            self.notifications[target].append(notification)

    def connect(self, user_key, player):
        if player.username in self.username_to_user_key:
            return False

        self.players[user_key] = player
        self.username_to_user_key[player.username] = user_key
        self.notifications[user_key] = []

        self.notify(f"Player {player.username} connected")

        if len(self.players) == self.max_players:
            self.start()

        return True

    def pop_notifications(self, user_key):
        notifications = self.notifications[user_key]
        self.notifications[user_key] = []
        return notifications

    def start(self):
        player_count = len(self.players)
        if player_count < 3:
            return

        roles = [PlayerRole.CITIZEN] * (player_count - 2) + [PlayerRole.MAFIA, PlayerRole.DETECTIVE]
        random.shuffle(roles)

        for i, player_key in enumerate(list(self.players.keys())):
            self.players[player_key].role = roles[i]
            self.notify(f"Your role is {roles[i]}", [player_key])

        self.day_stage = DayStage.DAY
        self.session_state = SessionState.PLAYING

    def lynch(self, user_key, choose_player):
        if self.day_stage != DayStage.DAY \
                or user_key not in self.players \
                or choose_player not in self.username_to_user_key:
            return False

        username = self.players[user_key].username
        self.notify(f"Player {username} choose {choose_player}")

        choose_player_key = self.username_to_user_key[choose_player]
        if choose_player_key not in self.voting:
            self.voting[choose_player_key] = 0
        self.voting[choose_player_key] += 1
        self.votes += 1

        if self.votes == len(self.players):
            max_votes = max(self.voting.values())
            candidates = list(map(lambda x: x[0],
                                  filter(lambda candidate: candidate[1] == max_votes, self.voting.items())))

            choose_user_key = random.choice(candidates)
            choose_username = self.players[choose_user_key].username
            self.players[choose_user_key].is_alive = False
            self.day_stage = DayStage.NIGHT_MAFIA

            self.notify(f"Player {choose_username} is lynched")
            self.notify("You are dead but you can still watch the game", [choose_user_key])
            self.notify(f"Night comes, mafia is choosing innocent")

        return True
