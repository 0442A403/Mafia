from common.day_stage import DayStage


class Session:
    def __init__(self, session_id):
        self.session_id = session_id
        self.players = {}
        self.notifications = {}
        self.day_stage = DayStage.DAY

    def notify(self, notification, targets=None):
        if not targets:
            targets = self.players.keys()

        for target in targets:
            self.notifications[target].append(notification)

    def connect(self, user_key, player):
        self.players[user_key] = player
        self.notifications[user_key] = []

    def pop_notifications(self, user_key):
        notifications = self.notifications[user_key]
        self.notifications[user_key] = []
        return notifications

    def start(self):
        pass
