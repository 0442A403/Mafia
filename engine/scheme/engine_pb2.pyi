from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DayStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DAY_STAGE_DAY: _ClassVar[DayStage]
    DAY_STAGE_NIGHT_MAFIA: _ClassVar[DayStage]
    DAY_STAGE_NIGHT_DETECTIVE: _ClassVar[DayStage]

class PlayerRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PLAYER_ROLE_CITIZEN: _ClassVar[PlayerRole]
    PLAYER_ROLE_MAFIA: _ClassVar[PlayerRole]
    PLAYER_ROLE_DETECTIVE: _ClassVar[PlayerRole]

class SessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SESSION_STATE_NOT_STARTED: _ClassVar[SessionState]
    SESSION_STATE_PLAYING: _ClassVar[SessionState]
    SESSION_STATE_FINISHED: _ClassVar[SessionState]
DAY_STAGE_DAY: DayStage
DAY_STAGE_NIGHT_MAFIA: DayStage
DAY_STAGE_NIGHT_DETECTIVE: DayStage
PLAYER_ROLE_CITIZEN: PlayerRole
PLAYER_ROLE_MAFIA: PlayerRole
PLAYER_ROLE_DETECTIVE: PlayerRole
SESSION_STATE_NOT_STARTED: SessionState
SESSION_STATE_PLAYING: SessionState
SESSION_STATE_FINISHED: SessionState

class CreateGameRequest(_message.Message):
    __slots__ = ["max_player_number"]
    MAX_PLAYER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    max_player_number: int
    def __init__(self, max_player_number: _Optional[int] = ...) -> None: ...

class CreateGameResponse(_message.Message):
    __slots__ = ["session_id"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class ConnectRequest(_message.Message):
    __slots__ = ["session_id", "username"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    username: str
    def __init__(self, session_id: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class ConnectResponse(_message.Message):
    __slots__ = ["ok", "user_key"]
    OK_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    user_key: str
    def __init__(self, ok: bool = ..., user_key: _Optional[str] = ...) -> None: ...

class StartGameRequest(_message.Message):
    __slots__ = ["session_id", "user_key", "mafia_count", "detective_count"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    MAFIA_COUNT_FIELD_NUMBER: _ClassVar[int]
    DETECTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_key: str
    mafia_count: int
    detective_count: int
    def __init__(self, session_id: _Optional[str] = ..., user_key: _Optional[str] = ..., mafia_count: _Optional[int] = ..., detective_count: _Optional[int] = ...) -> None: ...

class StartGameResponse(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class GetStateRequest(_message.Message):
    __slots__ = ["session_id", "user_key"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_key: str
    def __init__(self, session_id: _Optional[str] = ..., user_key: _Optional[str] = ...) -> None: ...

class GetStateResponse(_message.Message):
    __slots__ = ["day_stage", "session_state", "players", "session_id", "mafia_chat", "detective_chat"]
    DAY_STAGE_FIELD_NUMBER: _ClassVar[int]
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MAFIA_CHAT_FIELD_NUMBER: _ClassVar[int]
    DETECTIVE_CHAT_FIELD_NUMBER: _ClassVar[int]
    day_stage: DayStage
    session_state: SessionState
    players: _containers.RepeatedCompositeFieldContainer[PlayerState]
    session_id: str
    mafia_chat: str
    detective_chat: str
    def __init__(self, day_stage: _Optional[_Union[DayStage, str]] = ..., session_state: _Optional[_Union[SessionState, str]] = ..., players: _Optional[_Iterable[_Union[PlayerState, _Mapping]]] = ..., session_id: _Optional[str] = ..., mafia_chat: _Optional[str] = ..., detective_chat: _Optional[str] = ...) -> None: ...

class PlayerState(_message.Message):
    __slots__ = ["username", "is_alive", "role"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    IS_ALIVE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    username: str
    is_alive: bool
    role: PlayerRole
    def __init__(self, username: _Optional[str] = ..., is_alive: bool = ..., role: _Optional[_Union[PlayerRole, str]] = ...) -> None: ...

class GetNotificationsRequest(_message.Message):
    __slots__ = ["session_id", "user_key"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_key: str
    def __init__(self, session_id: _Optional[str] = ..., user_key: _Optional[str] = ...) -> None: ...

class GetNotificationsResponse(_message.Message):
    __slots__ = ["notifications"]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, notifications: _Optional[_Iterable[str]] = ...) -> None: ...

class MafiaChooseRequest(_message.Message):
    __slots__ = ["session_id", "user_key", "choose_player"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_PLAYER_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_key: str
    choose_player: str
    def __init__(self, session_id: _Optional[str] = ..., user_key: _Optional[str] = ..., choose_player: _Optional[str] = ...) -> None: ...

class MafiaChooseResponse(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class DetectiveChooseRequest(_message.Message):
    __slots__ = ["session_id", "user_key", "choose_player"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_PLAYER_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_key: str
    choose_player: str
    def __init__(self, session_id: _Optional[str] = ..., user_key: _Optional[str] = ..., choose_player: _Optional[str] = ...) -> None: ...

class DetectiveChooseResponse(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class LynchChooseRequest(_message.Message):
    __slots__ = ["session_id", "user_key", "choose_player"]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_KEY_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_PLAYER_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_key: str
    choose_player: str
    def __init__(self, session_id: _Optional[str] = ..., user_key: _Optional[str] = ..., choose_player: _Optional[str] = ...) -> None: ...

class LynchChooseResponse(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...
