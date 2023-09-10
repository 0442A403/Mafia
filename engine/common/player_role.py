import enum


class PlayerRole(enum.Enum):
    CITIZEN = 0
    MAFIA = 1
    DETECTIVE = 2

    def __str__(self):
        if self == PlayerRole.CITIZEN:
            return "citizen"
        elif self == PlayerRole.MAFIA:
            return "mafia"
        elif self == PlayerRole.DETECTIVE:
            return "detective"
