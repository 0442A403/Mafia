import copy
import random
import uuid
from typing import Dict

from common.day_stage import DayStage
from common.player import Player
from common.player_role import PlayerRole
from common.session_state import SessionState


class Session:
    def __init__(self, session_id, max_players=None):
        self.session_id = session_id
        self.players: Dict[str, Player] = {}
        self.notifications = {}
        self.day_stage = DayStage.DAY
        self.session_state = SessionState.NOT_STARTED
        self.max_players = max_players
        self.username_to_user_key = {}
        self.voting = {}
        self.votes = {}
        self.innocents = []
        self.mafia_chat = None
        self.detective_chat = None
        self.chose_detective = set()

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

        return True

    def pop_notifications(self, user_key):
        notifications = self.notifications[user_key]
        self.notifications[user_key] = []
        return notifications

    def start(self, mafia_count, detective_count):
        player_count = len(self.players)
        if player_count < mafia_count + detective_count or mafia_count * 2 >= player_count:
            return False

        self.mafia_count = mafia_count
        self.detective_count = detective_count

        roles = [PlayerRole.MAFIA] * mafia_count \
                + [PlayerRole.DETECTIVE] * detective_count \
                + [PlayerRole.CITIZEN] * (player_count - mafia_count - detective_count)
        random.shuffle(roles)

        for i, player_key in enumerate(list(self.players.keys())):
            self.players[player_key].role = roles[i]
            self.notify(f"Your role is {roles[i]}", [player_key])

        self.day_stage = DayStage.DAY
        self.session_state = SessionState.PLAYING
        self.mafia_chat = str(uuid.uuid4())
        self.detective_chat = str(uuid.uuid4())

        return True

    def lynch(self, user_key, choose_player):
        if self.day_stage != DayStage.DAY \
                or user_key not in self.players \
                or choose_player not in self.username_to_user_key \
                or not self.players[user_key].is_alive \
                or user_key == self.username_to_user_key[choose_player] \
                or user_key in self.votes:
            return False

        username = self.players[user_key].username
        self.notify(f"Player {username} choose {choose_player}")

        choose_player_key = self.username_to_user_key[choose_player]
        if choose_player_key not in self.voting:
            self.voting[choose_player_key] = 0
        self.voting[choose_player_key] += 1
        self.votes[user_key] = choose_player_key

        if len(self.votes) == sum(map(lambda x: x.is_alive, self.players.values())):
            max_votes = max(self.voting.values())
            candidates = list(map(lambda x: x[0],
                                  filter(lambda candidate: candidate[1] == max_votes, self.voting.items())))

            choose_user_key = random.choice(candidates)
            choose_username = self.players[choose_user_key].username
            self.players[choose_user_key].is_alive = False
            self.day_stage = DayStage.NIGHT_MAFIA

            self.notify(f"Player {choose_username} is lynched")
            self.notify("You are dead but you can still watch the game", [choose_user_key])
            if self.check_game_finish():
                return True

            self.notify("Night comes, mafia is choosing innocents")

        return True

    def mafia_choose(self, user_key, choose_player):
        if self.day_stage != DayStage.NIGHT_MAFIA \
                or user_key not in self.players \
                or choose_player not in self.username_to_user_key \
                or self.players[user_key].role != PlayerRole.MAFIA \
                or not self.players[user_key].is_alive \
                or user_key == self.username_to_user_key[choose_player] \
                or self.username_to_user_key[choose_player] in self.innocents:
            return False

        choose_player_key = self.username_to_user_key[choose_player]
        self.players[choose_player_key].is_alive = False
        self.innocents.append(choose_player)

        alive_mafia = list(map(lambda x: x[0],
                                    filter(lambda x: x[1].is_alive and x[1].role == PlayerRole.MAFIA,
                                           self.players.items())))
        self.notify(f"Player {self.players[user_key].username} chose {choose_player}", alive_mafia)

        if len(self.innocents) == len(alive_mafia):
            self.notify("Mafia chose innocents")
            self.notify("You are dead but you can still watch the game", [choose_player_key])
            self.notify("Night continues, detective is choosing suspect")

            if any(map(lambda x: x.role == PlayerRole.DETECTIVE and x.is_alive, self.players.values())):
                self.day_stage = DayStage.NIGHT_DETECTIVE
                self.check_game_finish()
            else:
                self.notify("Detective choose suspect")
                self.notify(f"Day comes, city awakes but without {', '.join(self.innocents)}")
                self.check_game_finish()
                self.start_day()

    def check_game_finish(self):
        if not any(map(lambda x: x.role == PlayerRole.MAFIA and x.is_alive, self.players.values())):
            self.notify("City won! Mafia is dead!")
            self.session_state = SessionState.FINISHED
            return True

        alive_count = sum(map(lambda x: x.is_alive, self.players.values()))
        mafia_count = sum(map(lambda x: x.is_alive and x.role == PlayerRole.MAFIA, self.players.values()))
        if alive_count - mafia_count <= mafia_count:
            self.notify("Mafia is won!")
            self.session_state = SessionState.FINISHED
            return True

        return False

    def start_day(self):
        self.day_stage = DayStage.DAY
        self.voting = {}
        self.votes = {}
        self.innocents = []
        self.chose_detective = set()

    def detective_choose(self, user_key, choose_player):
        if self.day_stage != DayStage.NIGHT_DETECTIVE \
                or user_key not in self.players \
                or choose_player not in self.username_to_user_key \
                or self.players[user_key].role != PlayerRole.DETECTIVE \
                or not self.players[user_key].is_alive \
                or user_key == self.username_to_user_key[choose_player] \
                or user_key in self.chose_detective:
            return False

        choose_player_key = self.username_to_user_key[choose_player]
        choose_player_role = self.players[choose_player_key].role

        alive_detectives = list(map(lambda x: x[0],
                                filter(lambda x: x[1].is_alive and x[1].role == PlayerRole.DETECTIVE,
                                       self.players.items())))
        self.notify(f"Player {choose_player} is {choose_player_role}", alive_detectives)
        self.chose_detective.add(user_key)

        if len(alive_detectives) == len(self.chose_detective):
            self.notify("Detective choose suspects")
            self.notify(f"Day comes, city awakes but without {', '.join(self.innocents)}")
            self.start_day()

        return True
