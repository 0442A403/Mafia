import enum


class DayStage(enum.Enum):
    DAY = 0
    NIGHT_MAFIA = 1
    NIGHT_DETECTIVE = 2

    def __str__(self):
        if self == DayStage.DAY:
            return "day"
        elif self == DayStage.NIGHT_MAFIA:
            return "night, mafia is choosing"
        elif self == DayStage.NIGHT_DETECTIVE:
            return "night, detective is choosing"

