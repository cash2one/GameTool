# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GameProtocol.World.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import GameProtocol.Common_pb2
import GameProtocol.USERDB_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GameProtocol.World.proto',
  package='',
  serialized_pb='\n\x18GameProtocol.World.proto\x1a\x19GameProtocol.Common.proto\x1a\x19GameProtocol.USERDB.proto\"G\n\x18World_ZoneChanged_Notify\x12\x0f\n\x07worldID\x18\x01 \x01(\r\x12\x1a\n\x07stZones\x18\x02 \x01(\x0b\x32\t.ZoneList\"Z\n\x18World_CreateRole_Request\x12\x0b\n\x03uin\x18\x01 \x01(\r\x12\r\n\x05world\x18\x02 \x01(\r\x12\"\n\x0bstBirthData\x18\x04 \x01(\x0b\x32\r.GameUserInfo\"G\n\x19World_CreateRole_Response\x12\x0f\n\x07iResult\x18\x01 \x01(\x05\x12\x19\n\x08stRoleID\x18\x02 \x01(\x0b\x32\x07.RoleID\"V\n\x17World_FetchRole_Request\x12\x19\n\x08stRoleID\x18\x01 \x01(\x0b\x32\x07.RoleID\x12\x10\n\x08\x62IsLogin\x18\x02 \x01(\x08\x12\x0e\n\x06iReqID\x18\x04 \x01(\x05\"{\n\x18World_FetchRole_Response\x12\x19\n\x08stRoleID\x18\x01 \x01(\x0b\x32\x07.RoleID\x12\x0f\n\x07iResult\x18\x02 \x01(\x05\x12!\n\nstUserInfo\x18\x03 \x01(\x0b\x32\r.GameUserInfo\x12\x10\n\x08\x62IsLogin\x18\x04 \x01(\x08\"\x7f\n\x18World_UpdateRole_Request\x12\x19\n\x08stRoleID\x18\x01 \x01(\x0b\x32\x07.RoleID\x12\x0e\n\x06iReqID\x18\x02 \x01(\x05\x12!\n\nstUserInfo\x18\x03 \x01(\x0b\x32\r.GameUserInfo\x12\x15\n\rbNeedResponse\x18\x04 \x01(\x08\"G\n\x19World_UpdateRole_Response\x12\x19\n\x08stRoleID\x18\x01 \x01(\x0b\x32\x07.RoleID\x12\x0f\n\x07iResult\x18\x02 \x01(\x05\"\x8a\x01\n\x16World_KickRole_Request\x12\x14\n\x0ciFromWorldID\x18\x01 \x01(\x05\x12\x13\n\x0biFromZoneID\x18\x02 \x01(\x05\x12\x12\n\niSessionID\x18\x03 \x01(\x05\x12\x1f\n\x0estKickedRoleID\x18\x04 \x01(\x0b\x32\x07.RoleID\x12\x10\n\x08\x62IsLogin\x18\x05 \x01(\x08\"\x9c\x01\n\x17World_KickRole_Response\x12\x0f\n\x07iResult\x18\x01 \x01(\x05\x12\x14\n\x0ciFromWorldID\x18\x02 \x01(\x05\x12\x13\n\x0biFromZoneID\x18\x03 \x01(\x05\x12\x12\n\niSessionID\x18\x04 \x01(\x05\x12\x1f\n\x0estKickedRoleID\x18\x05 \x01(\x0b\x32\x07.RoleID\x12\x10\n\x08\x62IsLogin\x18\x06 \x01(\x08\"3\n\x0eZoneOnlineInfo\x12\x0f\n\x07iZoneID\x18\x01 \x01(\x05\x12\x10\n\x08iRoleNum\x18\x02 \x01(\x05\"\xbf\x01\n\x0fWorldOnlineInfo\x12\x10\n\x08iWorldID\x18\x01 \x01(\x05\x12\x16\n\x0eiOnlineRoleNum\x18\x02 \x01(\x05\x12\x14\n\x0ciRegisterNum\x18\x03 \x01(\x05\x12\x15\n\riMaxOnlineNum\x18\x04 \x01(\x05\x12\x17\n\x0fiMaxRegisterNum\x18\x05 \x01(\x05\x12\x16\n\x0eiActiveZoneNum\x18\x06 \x01(\x05\x12$\n\x0bstZoneInfos\x18\x07 \x03(\x0b\x32\x0f.ZoneOnlineInfo\"h\n\x18World_OnlineStat_Request\x12\x10\n\x08iWorldID\x18\x01 \x01(\x05\x12%\n\x0bstWorldInfo\x18\x02 \x01(\x0b\x32\x10.WorldOnlineInfo\x12\x13\n\x0buRecordTime\x18\x03 \x01(\x05\"B\n\x19World_OnlineStat_Response\x12\x10\n\x08iWorldID\x18\x01 \x01(\x05\x12\x13\n\x0biInstanceID\x18\x02 \x01(\x05\"\xa9\x01\n\x11World_Chat_Notify\x12\x38\n\x08iChannel\x18\x01 \x01(\x0e\x32\x10.ChatChannelType:\x14\x43HAT_CHANNEL_INVALID\x12\x19\n\x08stRoleID\x18\x02 \x01(\x0b\x32\x07.RoleID\x12\x0f\n\x07iZoneID\x18\x04 \x01(\x05\x12\x1b\n\nstTargetID\x18\x05 \x01(\x0b\x32\x07.RoleID\x12\x11\n\tszMessage\x18\x06 \x01(\t')




_WORLD_ZONECHANGED_NOTIFY = _descriptor.Descriptor(
  name='World_ZoneChanged_Notify',
  full_name='World_ZoneChanged_Notify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='worldID', full_name='World_ZoneChanged_Notify.worldID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stZones', full_name='World_ZoneChanged_Notify.stZones', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=82,
  serialized_end=153,
)


_WORLD_CREATEROLE_REQUEST = _descriptor.Descriptor(
  name='World_CreateRole_Request',
  full_name='World_CreateRole_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uin', full_name='World_CreateRole_Request.uin', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world', full_name='World_CreateRole_Request.world', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stBirthData', full_name='World_CreateRole_Request.stBirthData', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=155,
  serialized_end=245,
)


_WORLD_CREATEROLE_RESPONSE = _descriptor.Descriptor(
  name='World_CreateRole_Response',
  full_name='World_CreateRole_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iResult', full_name='World_CreateRole_Response.iResult', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stRoleID', full_name='World_CreateRole_Response.stRoleID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=247,
  serialized_end=318,
)


_WORLD_FETCHROLE_REQUEST = _descriptor.Descriptor(
  name='World_FetchRole_Request',
  full_name='World_FetchRole_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stRoleID', full_name='World_FetchRole_Request.stRoleID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bIsLogin', full_name='World_FetchRole_Request.bIsLogin', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iReqID', full_name='World_FetchRole_Request.iReqID', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=320,
  serialized_end=406,
)


_WORLD_FETCHROLE_RESPONSE = _descriptor.Descriptor(
  name='World_FetchRole_Response',
  full_name='World_FetchRole_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stRoleID', full_name='World_FetchRole_Response.stRoleID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iResult', full_name='World_FetchRole_Response.iResult', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stUserInfo', full_name='World_FetchRole_Response.stUserInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bIsLogin', full_name='World_FetchRole_Response.bIsLogin', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=408,
  serialized_end=531,
)


_WORLD_UPDATEROLE_REQUEST = _descriptor.Descriptor(
  name='World_UpdateRole_Request',
  full_name='World_UpdateRole_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stRoleID', full_name='World_UpdateRole_Request.stRoleID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iReqID', full_name='World_UpdateRole_Request.iReqID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stUserInfo', full_name='World_UpdateRole_Request.stUserInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bNeedResponse', full_name='World_UpdateRole_Request.bNeedResponse', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=533,
  serialized_end=660,
)


_WORLD_UPDATEROLE_RESPONSE = _descriptor.Descriptor(
  name='World_UpdateRole_Response',
  full_name='World_UpdateRole_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stRoleID', full_name='World_UpdateRole_Response.stRoleID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iResult', full_name='World_UpdateRole_Response.iResult', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=662,
  serialized_end=733,
)


_WORLD_KICKROLE_REQUEST = _descriptor.Descriptor(
  name='World_KickRole_Request',
  full_name='World_KickRole_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iFromWorldID', full_name='World_KickRole_Request.iFromWorldID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iFromZoneID', full_name='World_KickRole_Request.iFromZoneID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iSessionID', full_name='World_KickRole_Request.iSessionID', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stKickedRoleID', full_name='World_KickRole_Request.stKickedRoleID', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bIsLogin', full_name='World_KickRole_Request.bIsLogin', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=736,
  serialized_end=874,
)


_WORLD_KICKROLE_RESPONSE = _descriptor.Descriptor(
  name='World_KickRole_Response',
  full_name='World_KickRole_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iResult', full_name='World_KickRole_Response.iResult', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iFromWorldID', full_name='World_KickRole_Response.iFromWorldID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iFromZoneID', full_name='World_KickRole_Response.iFromZoneID', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iSessionID', full_name='World_KickRole_Response.iSessionID', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stKickedRoleID', full_name='World_KickRole_Response.stKickedRoleID', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bIsLogin', full_name='World_KickRole_Response.bIsLogin', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=877,
  serialized_end=1033,
)


_ZONEONLINEINFO = _descriptor.Descriptor(
  name='ZoneOnlineInfo',
  full_name='ZoneOnlineInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iZoneID', full_name='ZoneOnlineInfo.iZoneID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRoleNum', full_name='ZoneOnlineInfo.iRoleNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1035,
  serialized_end=1086,
)


_WORLDONLINEINFO = _descriptor.Descriptor(
  name='WorldOnlineInfo',
  full_name='WorldOnlineInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iWorldID', full_name='WorldOnlineInfo.iWorldID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iOnlineRoleNum', full_name='WorldOnlineInfo.iOnlineRoleNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRegisterNum', full_name='WorldOnlineInfo.iRegisterNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iMaxOnlineNum', full_name='WorldOnlineInfo.iMaxOnlineNum', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iMaxRegisterNum', full_name='WorldOnlineInfo.iMaxRegisterNum', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iActiveZoneNum', full_name='WorldOnlineInfo.iActiveZoneNum', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stZoneInfos', full_name='WorldOnlineInfo.stZoneInfos', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1089,
  serialized_end=1280,
)


_WORLD_ONLINESTAT_REQUEST = _descriptor.Descriptor(
  name='World_OnlineStat_Request',
  full_name='World_OnlineStat_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iWorldID', full_name='World_OnlineStat_Request.iWorldID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stWorldInfo', full_name='World_OnlineStat_Request.stWorldInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uRecordTime', full_name='World_OnlineStat_Request.uRecordTime', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1282,
  serialized_end=1386,
)


_WORLD_ONLINESTAT_RESPONSE = _descriptor.Descriptor(
  name='World_OnlineStat_Response',
  full_name='World_OnlineStat_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iWorldID', full_name='World_OnlineStat_Response.iWorldID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iInstanceID', full_name='World_OnlineStat_Response.iInstanceID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1388,
  serialized_end=1454,
)


_WORLD_CHAT_NOTIFY = _descriptor.Descriptor(
  name='World_Chat_Notify',
  full_name='World_Chat_Notify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iChannel', full_name='World_Chat_Notify.iChannel', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stRoleID', full_name='World_Chat_Notify.stRoleID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iZoneID', full_name='World_Chat_Notify.iZoneID', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stTargetID', full_name='World_Chat_Notify.stTargetID', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='szMessage', full_name='World_Chat_Notify.szMessage', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1457,
  serialized_end=1626,
)

_WORLD_ZONECHANGED_NOTIFY.fields_by_name['stZones'].message_type = GameProtocol.Common_pb2._ZONELIST
_WORLD_CREATEROLE_REQUEST.fields_by_name['stBirthData'].message_type = GameProtocol.USERDB_pb2._GAMEUSERINFO
_WORLD_CREATEROLE_RESPONSE.fields_by_name['stRoleID'].message_type = GameProtocol.Common_pb2._ROLEID
_WORLD_FETCHROLE_REQUEST.fields_by_name['stRoleID'].message_type = GameProtocol.Common_pb2._ROLEID
_WORLD_FETCHROLE_RESPONSE.fields_by_name['stRoleID'].message_type = GameProtocol.Common_pb2._ROLEID
_WORLD_FETCHROLE_RESPONSE.fields_by_name['stUserInfo'].message_type = GameProtocol.USERDB_pb2._GAMEUSERINFO
_WORLD_UPDATEROLE_REQUEST.fields_by_name['stRoleID'].message_type = GameProtocol.Common_pb2._ROLEID
_WORLD_UPDATEROLE_REQUEST.fields_by_name['stUserInfo'].message_type = GameProtocol.USERDB_pb2._GAMEUSERINFO
_WORLD_UPDATEROLE_RESPONSE.fields_by_name['stRoleID'].message_type = GameProtocol.Common_pb2._ROLEID
_WORLD_KICKROLE_REQUEST.fields_by_name['stKickedRoleID'].message_type = GameProtocol.Common_pb2._ROLEID
_WORLD_KICKROLE_RESPONSE.fields_by_name['stKickedRoleID'].message_type = GameProtocol.Common_pb2._ROLEID
_WORLDONLINEINFO.fields_by_name['stZoneInfos'].message_type = _ZONEONLINEINFO
_WORLD_ONLINESTAT_REQUEST.fields_by_name['stWorldInfo'].message_type = _WORLDONLINEINFO
_WORLD_CHAT_NOTIFY.fields_by_name['iChannel'].enum_type = GameProtocol.Common_pb2._CHATCHANNELTYPE
_WORLD_CHAT_NOTIFY.fields_by_name['stRoleID'].message_type = GameProtocol.Common_pb2._ROLEID
_WORLD_CHAT_NOTIFY.fields_by_name['stTargetID'].message_type = GameProtocol.Common_pb2._ROLEID
DESCRIPTOR.message_types_by_name['World_ZoneChanged_Notify'] = _WORLD_ZONECHANGED_NOTIFY
DESCRIPTOR.message_types_by_name['World_CreateRole_Request'] = _WORLD_CREATEROLE_REQUEST
DESCRIPTOR.message_types_by_name['World_CreateRole_Response'] = _WORLD_CREATEROLE_RESPONSE
DESCRIPTOR.message_types_by_name['World_FetchRole_Request'] = _WORLD_FETCHROLE_REQUEST
DESCRIPTOR.message_types_by_name['World_FetchRole_Response'] = _WORLD_FETCHROLE_RESPONSE
DESCRIPTOR.message_types_by_name['World_UpdateRole_Request'] = _WORLD_UPDATEROLE_REQUEST
DESCRIPTOR.message_types_by_name['World_UpdateRole_Response'] = _WORLD_UPDATEROLE_RESPONSE
DESCRIPTOR.message_types_by_name['World_KickRole_Request'] = _WORLD_KICKROLE_REQUEST
DESCRIPTOR.message_types_by_name['World_KickRole_Response'] = _WORLD_KICKROLE_RESPONSE
DESCRIPTOR.message_types_by_name['ZoneOnlineInfo'] = _ZONEONLINEINFO
DESCRIPTOR.message_types_by_name['WorldOnlineInfo'] = _WORLDONLINEINFO
DESCRIPTOR.message_types_by_name['World_OnlineStat_Request'] = _WORLD_ONLINESTAT_REQUEST
DESCRIPTOR.message_types_by_name['World_OnlineStat_Response'] = _WORLD_ONLINESTAT_RESPONSE
DESCRIPTOR.message_types_by_name['World_Chat_Notify'] = _WORLD_CHAT_NOTIFY

class World_ZoneChanged_Notify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_ZONECHANGED_NOTIFY

  # @@protoc_insertion_point(class_scope:World_ZoneChanged_Notify)

class World_CreateRole_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_CREATEROLE_REQUEST

  # @@protoc_insertion_point(class_scope:World_CreateRole_Request)

class World_CreateRole_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_CREATEROLE_RESPONSE

  # @@protoc_insertion_point(class_scope:World_CreateRole_Response)

class World_FetchRole_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_FETCHROLE_REQUEST

  # @@protoc_insertion_point(class_scope:World_FetchRole_Request)

class World_FetchRole_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_FETCHROLE_RESPONSE

  # @@protoc_insertion_point(class_scope:World_FetchRole_Response)

class World_UpdateRole_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_UPDATEROLE_REQUEST

  # @@protoc_insertion_point(class_scope:World_UpdateRole_Request)

class World_UpdateRole_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_UPDATEROLE_RESPONSE

  # @@protoc_insertion_point(class_scope:World_UpdateRole_Response)

class World_KickRole_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_KICKROLE_REQUEST

  # @@protoc_insertion_point(class_scope:World_KickRole_Request)

class World_KickRole_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_KICKROLE_RESPONSE

  # @@protoc_insertion_point(class_scope:World_KickRole_Response)

class ZoneOnlineInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ZONEONLINEINFO

  # @@protoc_insertion_point(class_scope:ZoneOnlineInfo)

class WorldOnlineInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLDONLINEINFO

  # @@protoc_insertion_point(class_scope:WorldOnlineInfo)

class World_OnlineStat_Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_ONLINESTAT_REQUEST

  # @@protoc_insertion_point(class_scope:World_OnlineStat_Request)

class World_OnlineStat_Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_ONLINESTAT_RESPONSE

  # @@protoc_insertion_point(class_scope:World_OnlineStat_Response)

class World_Chat_Notify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORLD_CHAT_NOTIFY

  # @@protoc_insertion_point(class_scope:World_Chat_Notify)


# @@protoc_insertion_point(module_scope)
