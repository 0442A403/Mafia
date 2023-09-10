# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65ngine.proto\"\x13\n\x11\x43reateGameRequest\"(\n\x12\x43reateGameResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\"6\n\x0e\x43onnectRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"/\n\x0f\x43onnectResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x10\n\x08user_key\x18\x02 \x01(\t\"M\n\x10StartGameRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x10\n\x08user_key\x18\x02 \x01(\t\x12\x13\n\x0b\x62ot_players\x18\x03 \x01(\x05\"\x1f\n\x11StartGameResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\"7\n\x0fGetStateRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x10\n\x08user_key\x18\x02 \x01(\t\"u\n\x10GetStateResponse\x12\x1c\n\tday_stage\x18\x01 \x01(\x0e\x32\t.DayStage\x12$\n\rsession_state\x18\x02 \x01(\x0e\x32\r.SessionState\x12\x1d\n\x07players\x18\x03 \x03(\x0b\x32\x0c.PlayerState\"Z\n\x0bPlayerState\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08is_alive\x18\x02 \x01(\x08\x12\x1e\n\x04role\x18\x03 \x01(\x0e\x32\x0b.PlayerRoleH\x00\x88\x01\x01\x42\x07\n\x05_role\"?\n\x17GetNotificationsRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x10\n\x08user_key\x18\x02 \x01(\t\"1\n\x18GetNotificationsResponse\x12\x15\n\rnotifications\x18\x01 \x03(\t\"Q\n\x12MafiaChooseRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x10\n\x08user_key\x18\x02 \x01(\t\x12\x15\n\rchoose_player\x18\x03 \x01(\t\"!\n\x13MafiaChooseResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\"U\n\x16\x44\x65tectiveChooseRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x10\n\x08user_key\x18\x02 \x01(\t\x12\x15\n\rchoose_player\x18\x03 \x01(\t\"%\n\x17\x44\x65tectiveChooseResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\"Q\n\x12LynchChooseRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x10\n\x08user_key\x18\x02 \x01(\t\x12\x15\n\rchoose_player\x18\x03 \x01(\t\"!\n\x13LynchChooseResponse\x12\n\n\x02ok\x18\x01 \x01(\x08*W\n\x08\x44\x61yStage\x12\x11\n\rDAY_STAGE_DAY\x10\x00\x12\x19\n\x15\x44\x41Y_STAGE_NIGHT_MAFIA\x10\x01\x12\x1d\n\x19\x44\x41Y_STAGE_NIGHT_DETECTIVE\x10\x02*W\n\nPlayerRole\x12\x17\n\x13PLAYER_ROLE_CITIZEN\x10\x00\x12\x15\n\x11PLAYER_ROLE_MAFIA\x10\x01\x12\x19\n\x15PLAYER_ROLE_DETECTIVE\x10\x02*d\n\x0cSessionState\x12\x1d\n\x19SESSION_STATE_NOT_STARTED\x10\x00\x12\x19\n\x15SESSION_STATE_PLAYING\x10\x01\x12\x1a\n\x16SESSION_STATE_FINISHED\x10\x02\x32\xea\x03\n\x0bMafiaEngine\x12\x37\n\nCreateGame\x12\x12.CreateGameRequest\x1a\x13.CreateGameResponse\"\x00\x12.\n\x07\x43onnect\x12\x0f.ConnectRequest\x1a\x10.ConnectResponse\"\x00\x12\x34\n\tStartGame\x12\x11.StartGameRequest\x1a\x12.StartGameResponse\"\x00\x12\x31\n\x08GetState\x12\x10.GetStateRequest\x1a\x11.GetStateResponse\"\x00\x12I\n\x10GetNotifications\x12\x18.GetNotificationsRequest\x1a\x19.GetNotificationsResponse\"\x00\x12:\n\x0bMafiaChoose\x12\x13.MafiaChooseRequest\x1a\x14.MafiaChooseResponse\"\x00\x12\x46\n\x0f\x44\x65tectiveChoose\x12\x17.DetectiveChooseRequest\x1a\x18.DetectiveChooseResponse\"\x00\x12:\n\x0bLynchChoose\x12\x13.LynchChooseRequest\x1a\x14.LynchChooseResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'engine_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DAYSTAGE']._serialized_start=1042
  _globals['_DAYSTAGE']._serialized_end=1129
  _globals['_PLAYERROLE']._serialized_start=1131
  _globals['_PLAYERROLE']._serialized_end=1218
  _globals['_SESSIONSTATE']._serialized_start=1220
  _globals['_SESSIONSTATE']._serialized_end=1320
  _globals['_CREATEGAMEREQUEST']._serialized_start=16
  _globals['_CREATEGAMEREQUEST']._serialized_end=35
  _globals['_CREATEGAMERESPONSE']._serialized_start=37
  _globals['_CREATEGAMERESPONSE']._serialized_end=77
  _globals['_CONNECTREQUEST']._serialized_start=79
  _globals['_CONNECTREQUEST']._serialized_end=133
  _globals['_CONNECTRESPONSE']._serialized_start=135
  _globals['_CONNECTRESPONSE']._serialized_end=182
  _globals['_STARTGAMEREQUEST']._serialized_start=184
  _globals['_STARTGAMEREQUEST']._serialized_end=261
  _globals['_STARTGAMERESPONSE']._serialized_start=263
  _globals['_STARTGAMERESPONSE']._serialized_end=294
  _globals['_GETSTATEREQUEST']._serialized_start=296
  _globals['_GETSTATEREQUEST']._serialized_end=351
  _globals['_GETSTATERESPONSE']._serialized_start=353
  _globals['_GETSTATERESPONSE']._serialized_end=470
  _globals['_PLAYERSTATE']._serialized_start=472
  _globals['_PLAYERSTATE']._serialized_end=562
  _globals['_GETNOTIFICATIONSREQUEST']._serialized_start=564
  _globals['_GETNOTIFICATIONSREQUEST']._serialized_end=627
  _globals['_GETNOTIFICATIONSRESPONSE']._serialized_start=629
  _globals['_GETNOTIFICATIONSRESPONSE']._serialized_end=678
  _globals['_MAFIACHOOSEREQUEST']._serialized_start=680
  _globals['_MAFIACHOOSEREQUEST']._serialized_end=761
  _globals['_MAFIACHOOSERESPONSE']._serialized_start=763
  _globals['_MAFIACHOOSERESPONSE']._serialized_end=796
  _globals['_DETECTIVECHOOSEREQUEST']._serialized_start=798
  _globals['_DETECTIVECHOOSEREQUEST']._serialized_end=883
  _globals['_DETECTIVECHOOSERESPONSE']._serialized_start=885
  _globals['_DETECTIVECHOOSERESPONSE']._serialized_end=922
  _globals['_LYNCHCHOOSEREQUEST']._serialized_start=924
  _globals['_LYNCHCHOOSEREQUEST']._serialized_end=1005
  _globals['_LYNCHCHOOSERESPONSE']._serialized_start=1007
  _globals['_LYNCHCHOOSERESPONSE']._serialized_end=1040
  _globals['_MAFIAENGINE']._serialized_start=1323
  _globals['_MAFIAENGINE']._serialized_end=1813
# @@protoc_insertion_point(module_scope)
