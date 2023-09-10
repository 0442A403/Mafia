import enum


class SessionState(enum.Enum):
    NOT_STARTED = 0
    PLAYING = 1
    FINISHED = 2
