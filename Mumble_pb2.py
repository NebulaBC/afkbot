# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mumble.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cMumble.proto\x12\x0bMumbleProto\"K\n\x07Version\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0f\n\x07release\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\x12\n\nos_version\x18\x04 \x01(\t\"\x1b\n\tUDPTunnel\x12\x0e\n\x06packet\x18\x01 \x02(\x0c\"n\n\x0c\x41uthenticate\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0e\n\x06tokens\x18\x03 \x03(\t\x12\x15\n\rcelt_versions\x18\x04 \x03(\x05\x12\x13\n\x04opus\x18\x05 \x01(\x08:\x05\x66\x61lse\"\xd5\x01\n\x04Ping\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x0c\n\x04good\x18\x02 \x01(\r\x12\x0c\n\x04late\x18\x03 \x01(\r\x12\x0c\n\x04lost\x18\x04 \x01(\r\x12\x0e\n\x06resync\x18\x05 \x01(\r\x12\x13\n\x0budp_packets\x18\x06 \x01(\r\x12\x13\n\x0btcp_packets\x18\x07 \x01(\r\x12\x14\n\x0cudp_ping_avg\x18\x08 \x01(\x02\x12\x14\n\x0cudp_ping_var\x18\t \x01(\x02\x12\x14\n\x0ctcp_ping_avg\x18\n \x01(\x02\x12\x14\n\x0ctcp_ping_var\x18\x0b \x01(\x02\"\xf7\x01\n\x06Reject\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.MumbleProto.Reject.RejectType\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\xae\x01\n\nRejectType\x12\x08\n\x04None\x10\x00\x12\x10\n\x0cWrongVersion\x10\x01\x12\x13\n\x0fInvalidUsername\x10\x02\x12\x0f\n\x0bWrongUserPW\x10\x03\x12\x11\n\rWrongServerPW\x10\x04\x12\x11\n\rUsernameInUse\x10\x05\x12\x0e\n\nServerFull\x10\x06\x12\x11\n\rNoCertificate\x10\x07\x12\x15\n\x11\x41uthenticatorFail\x10\x08\"_\n\nServerSync\x12\x0f\n\x07session\x18\x01 \x01(\r\x12\x15\n\rmax_bandwidth\x18\x02 \x01(\r\x12\x14\n\x0cwelcome_text\x18\x03 \x01(\t\x12\x13\n\x0bpermissions\x18\x04 \x01(\x04\"#\n\rChannelRemove\x12\x12\n\nchannel_id\x18\x01 \x02(\r\"\x99\x02\n\x0c\x43hannelState\x12\x12\n\nchannel_id\x18\x01 \x01(\r\x12\x0e\n\x06parent\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05links\x18\x04 \x03(\r\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x11\n\tlinks_add\x18\x06 \x03(\r\x12\x14\n\x0clinks_remove\x18\x07 \x03(\r\x12\x18\n\ttemporary\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x08position\x18\t \x01(\x05:\x01\x30\x12\x18\n\x10\x64\x65scription_hash\x18\n \x01(\x0c\x12\x11\n\tmax_users\x18\x0b \x01(\r\x12\x1b\n\x13is_enter_restricted\x18\x0c \x01(\x08\x12\x11\n\tcan_enter\x18\r \x01(\x08\"I\n\nUserRemove\x12\x0f\n\x07session\x18\x01 \x02(\r\x12\r\n\x05\x61\x63tor\x18\x02 \x01(\r\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x0b\n\x03\x62\x61n\x18\x04 \x01(\x08\"\xce\x03\n\tUserState\x12\x0f\n\x07session\x18\x01 \x01(\r\x12\r\n\x05\x61\x63tor\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\r\x12\x12\n\nchannel_id\x18\x05 \x01(\r\x12\x0c\n\x04mute\x18\x06 \x01(\x08\x12\x0c\n\x04\x64\x65\x61\x66\x18\x07 \x01(\x08\x12\x10\n\x08suppress\x18\x08 \x01(\x08\x12\x11\n\tself_mute\x18\t \x01(\x08\x12\x11\n\tself_deaf\x18\n \x01(\x08\x12\x0f\n\x07texture\x18\x0b \x01(\x0c\x12\x16\n\x0eplugin_context\x18\x0c \x01(\x0c\x12\x17\n\x0fplugin_identity\x18\r \x01(\t\x12\x0f\n\x07\x63omment\x18\x0e \x01(\t\x12\x0c\n\x04hash\x18\x0f \x01(\t\x12\x14\n\x0c\x63omment_hash\x18\x10 \x01(\x0c\x12\x14\n\x0ctexture_hash\x18\x11 \x01(\x0c\x12\x18\n\x10priority_speaker\x18\x12 \x01(\x08\x12\x11\n\trecording\x18\x13 \x01(\x08\x12\x1f\n\x17temporary_access_tokens\x18\x14 \x03(\t\x12\x1d\n\x15listening_channel_add\x18\x15 \x03(\r\x12 \n\x18listening_channel_remove\x18\x16 \x03(\r\"\xc4\x01\n\x07\x42\x61nList\x12+\n\x04\x62\x61ns\x18\x01 \x03(\x0b\x32\x1d.MumbleProto.BanList.BanEntry\x12\x14\n\x05query\x18\x02 \x01(\x08:\x05\x66\x61lse\x1av\n\x08\x42\x61nEntry\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\x0c\x12\x0c\n\x04mask\x18\x02 \x02(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x0e\n\x06reason\x18\x05 \x01(\t\x12\r\n\x05start\x18\x06 \x01(\t\x12\x10\n\x08\x64uration\x18\x07 \x01(\r\"c\n\x0bTextMessage\x12\r\n\x05\x61\x63tor\x18\x01 \x01(\r\x12\x0f\n\x07session\x18\x02 \x03(\r\x12\x12\n\nchannel_id\x18\x03 \x03(\r\x12\x0f\n\x07tree_id\x18\x04 \x03(\r\x12\x0f\n\x07message\x18\x05 \x02(\t\"\xa7\x03\n\x10PermissionDenied\x12\x12\n\npermission\x18\x01 \x01(\r\x12\x12\n\nchannel_id\x18\x02 \x01(\r\x12\x0f\n\x07session\x18\x03 \x01(\r\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x34\n\x04type\x18\x05 \x01(\x0e\x32&.MumbleProto.PermissionDenied.DenyType\x12\x0c\n\x04name\x18\x06 \x01(\t\"\x85\x02\n\x08\x44\x65nyType\x12\x08\n\x04Text\x10\x00\x12\x0e\n\nPermission\x10\x01\x12\r\n\tSuperUser\x10\x02\x12\x0f\n\x0b\x43hannelName\x10\x03\x12\x0f\n\x0bTextTooLong\x10\x04\x12\x07\n\x03H9K\x10\x05\x12\x14\n\x10TemporaryChannel\x10\x06\x12\x16\n\x12MissingCertificate\x10\x07\x12\x0c\n\x08UserName\x10\x08\x12\x0f\n\x0b\x43hannelFull\x10\t\x12\x10\n\x0cNestingLimit\x10\n\x12\x15\n\x11\x43hannelCountLimit\x10\x0b\x12\x18\n\x14\x43hannelListenerLimit\x10\x0c\x12\x15\n\x11UserListenerLimit\x10\r\"\xd4\x03\n\x03\x41\x43L\x12\x12\n\nchannel_id\x18\x01 \x02(\r\x12\x1a\n\x0cinherit_acls\x18\x02 \x01(\x08:\x04true\x12*\n\x06groups\x18\x03 \x03(\x0b\x32\x1a.MumbleProto.ACL.ChanGroup\x12&\n\x04\x61\x63ls\x18\x04 \x03(\x0b\x32\x18.MumbleProto.ACL.ChanACL\x12\x14\n\x05query\x18\x05 \x01(\x08:\x05\x66\x61lse\x1a\x9c\x01\n\tChanGroup\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x17\n\tinherited\x18\x02 \x01(\x08:\x04true\x12\x15\n\x07inherit\x18\x03 \x01(\x08:\x04true\x12\x19\n\x0binheritable\x18\x04 \x01(\x08:\x04true\x12\x0b\n\x03\x61\x64\x64\x18\x05 \x03(\r\x12\x0e\n\x06remove\x18\x06 \x03(\r\x12\x19\n\x11inherited_members\x18\x07 \x03(\r\x1a\x93\x01\n\x07\x43hanACL\x12\x18\n\napply_here\x18\x01 \x01(\x08:\x04true\x12\x18\n\napply_subs\x18\x02 \x01(\x08:\x04true\x12\x17\n\tinherited\x18\x03 \x01(\x08:\x04true\x12\x0f\n\x07user_id\x18\x04 \x01(\r\x12\r\n\x05group\x18\x05 \x01(\t\x12\r\n\x05grant\x18\x06 \x01(\r\x12\x0c\n\x04\x64\x65ny\x18\x07 \x01(\r\"(\n\nQueryUsers\x12\x0b\n\x03ids\x18\x01 \x03(\r\x12\r\n\x05names\x18\x02 \x03(\t\"E\n\nCryptSetup\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x14\n\x0c\x63lient_nonce\x18\x02 \x01(\x0c\x12\x14\n\x0cserver_nonce\x18\x03 \x01(\x0c\"\xd3\x01\n\x13\x43ontextActionModify\x12\x0e\n\x06\x61\x63tion\x18\x01 \x02(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x03 \x01(\r\x12=\n\toperation\x18\x04 \x01(\x0e\x32*.MumbleProto.ContextActionModify.Operation\",\n\x07\x43ontext\x12\n\n\x06Server\x10\x01\x12\x0b\n\x07\x43hannel\x10\x02\x12\x08\n\x04User\x10\x04\" \n\tOperation\x12\x07\n\x03\x41\x64\x64\x10\x00\x12\n\n\x06Remove\x10\x01\"D\n\rContextAction\x12\x0f\n\x07session\x18\x01 \x01(\r\x12\x12\n\nchannel_id\x18\x02 \x01(\r\x12\x0e\n\x06\x61\x63tion\x18\x03 \x02(\t\"\x85\x01\n\x08UserList\x12)\n\x05users\x18\x01 \x03(\x0b\x32\x1a.MumbleProto.UserList.User\x1aN\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tlast_seen\x18\x03 \x01(\t\x12\x14\n\x0clast_channel\x18\x04 \x01(\r\"\xb8\x01\n\x0bVoiceTarget\x12\n\n\x02id\x18\x01 \x01(\r\x12\x30\n\x07targets\x18\x02 \x03(\x0b\x32\x1f.MumbleProto.VoiceTarget.Target\x1ak\n\x06Target\x12\x0f\n\x07session\x18\x01 \x03(\r\x12\x12\n\nchannel_id\x18\x02 \x01(\r\x12\r\n\x05group\x18\x03 \x01(\t\x12\x14\n\x05links\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x08\x63hildren\x18\x05 \x01(\x08:\x05\x66\x61lse\"P\n\x0fPermissionQuery\x12\x12\n\nchannel_id\x18\x01 \x01(\r\x12\x13\n\x0bpermissions\x18\x02 \x01(\r\x12\x14\n\x05\x66lush\x18\x03 \x01(\x08:\x05\x66\x61lse\"\\\n\x0c\x43odecVersion\x12\r\n\x05\x61lpha\x18\x01 \x02(\x05\x12\x0c\n\x04\x62\x65ta\x18\x02 \x02(\x05\x12\x1a\n\x0cprefer_alpha\x18\x03 \x02(\x08:\x04true\x12\x13\n\x04opus\x18\x04 \x01(\x08:\x05\x66\x61lse\"\xb8\x04\n\tUserStats\x12\x0f\n\x07session\x18\x01 \x01(\r\x12\x19\n\nstats_only\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x0c\x63\x65rtificates\x18\x03 \x03(\x0c\x12\x31\n\x0b\x66rom_client\x18\x04 \x01(\x0b\x32\x1c.MumbleProto.UserStats.Stats\x12\x31\n\x0b\x66rom_server\x18\x05 \x01(\x0b\x32\x1c.MumbleProto.UserStats.Stats\x12\x13\n\x0budp_packets\x18\x06 \x01(\r\x12\x13\n\x0btcp_packets\x18\x07 \x01(\r\x12\x14\n\x0cudp_ping_avg\x18\x08 \x01(\x02\x12\x14\n\x0cudp_ping_var\x18\t \x01(\x02\x12\x14\n\x0ctcp_ping_avg\x18\n \x01(\x02\x12\x14\n\x0ctcp_ping_var\x18\x0b \x01(\x02\x12%\n\x07version\x18\x0c \x01(\x0b\x32\x14.MumbleProto.Version\x12\x15\n\rcelt_versions\x18\r \x03(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x0e \x01(\x0c\x12\x11\n\tbandwidth\x18\x0f \x01(\r\x12\x12\n\nonlinesecs\x18\x10 \x01(\r\x12\x10\n\x08idlesecs\x18\x11 \x01(\r\x12!\n\x12strong_certificate\x18\x12 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x04opus\x18\x13 \x01(\x08:\x05\x66\x61lse\x1a\x41\n\x05Stats\x12\x0c\n\x04good\x18\x01 \x01(\r\x12\x0c\n\x04late\x18\x02 \x01(\r\x12\x0c\n\x04lost\x18\x03 \x01(\r\x12\x0e\n\x06resync\x18\x04 \x01(\r\"\\\n\x0bRequestBlob\x12\x17\n\x0fsession_texture\x18\x01 \x03(\r\x12\x17\n\x0fsession_comment\x18\x02 \x03(\r\x12\x1b\n\x13\x63hannel_description\x18\x03 \x03(\r\"\xb3\x01\n\x0cServerConfig\x12\x15\n\rmax_bandwidth\x18\x01 \x01(\r\x12\x14\n\x0cwelcome_text\x18\x02 \x01(\t\x12\x12\n\nallow_html\x18\x03 \x01(\x08\x12\x16\n\x0emessage_length\x18\x04 \x01(\r\x12\x1c\n\x14image_message_length\x18\x05 \x01(\r\x12\x11\n\tmax_users\x18\x06 \x01(\r\x12\x19\n\x11recording_allowed\x18\x07 \x01(\x08\"J\n\rSuggestConfig\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x12\n\npositional\x18\x02 \x01(\x08\x12\x14\n\x0cpush_to_talk\x18\x03 \x01(\x08\"k\n\x16PluginDataTransmission\x12\x15\n\rsenderSession\x18\x01 \x01(\r\x12\x1c\n\x10receiverSessions\x18\x02 \x03(\rB\x02\x10\x01\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x0e\n\x06\x64\x61taID\x18\x04 \x01(\tB\x02H\x01')



_VERSION = DESCRIPTOR.message_types_by_name['Version']
_UDPTUNNEL = DESCRIPTOR.message_types_by_name['UDPTunnel']
_AUTHENTICATE = DESCRIPTOR.message_types_by_name['Authenticate']
_PING = DESCRIPTOR.message_types_by_name['Ping']
_REJECT = DESCRIPTOR.message_types_by_name['Reject']
_SERVERSYNC = DESCRIPTOR.message_types_by_name['ServerSync']
_CHANNELREMOVE = DESCRIPTOR.message_types_by_name['ChannelRemove']
_CHANNELSTATE = DESCRIPTOR.message_types_by_name['ChannelState']
_USERREMOVE = DESCRIPTOR.message_types_by_name['UserRemove']
_USERSTATE = DESCRIPTOR.message_types_by_name['UserState']
_BANLIST = DESCRIPTOR.message_types_by_name['BanList']
_BANLIST_BANENTRY = _BANLIST.nested_types_by_name['BanEntry']
_TEXTMESSAGE = DESCRIPTOR.message_types_by_name['TextMessage']
_PERMISSIONDENIED = DESCRIPTOR.message_types_by_name['PermissionDenied']
_ACL = DESCRIPTOR.message_types_by_name['ACL']
_ACL_CHANGROUP = _ACL.nested_types_by_name['ChanGroup']
_ACL_CHANACL = _ACL.nested_types_by_name['ChanACL']
_QUERYUSERS = DESCRIPTOR.message_types_by_name['QueryUsers']
_CRYPTSETUP = DESCRIPTOR.message_types_by_name['CryptSetup']
_CONTEXTACTIONMODIFY = DESCRIPTOR.message_types_by_name['ContextActionModify']
_CONTEXTACTION = DESCRIPTOR.message_types_by_name['ContextAction']
_USERLIST = DESCRIPTOR.message_types_by_name['UserList']
_USERLIST_USER = _USERLIST.nested_types_by_name['User']
_VOICETARGET = DESCRIPTOR.message_types_by_name['VoiceTarget']
_VOICETARGET_TARGET = _VOICETARGET.nested_types_by_name['Target']
_PERMISSIONQUERY = DESCRIPTOR.message_types_by_name['PermissionQuery']
_CODECVERSION = DESCRIPTOR.message_types_by_name['CodecVersion']
_USERSTATS = DESCRIPTOR.message_types_by_name['UserStats']
_USERSTATS_STATS = _USERSTATS.nested_types_by_name['Stats']
_REQUESTBLOB = DESCRIPTOR.message_types_by_name['RequestBlob']
_SERVERCONFIG = DESCRIPTOR.message_types_by_name['ServerConfig']
_SUGGESTCONFIG = DESCRIPTOR.message_types_by_name['SuggestConfig']
_PLUGINDATATRANSMISSION = DESCRIPTOR.message_types_by_name['PluginDataTransmission']
_REJECT_REJECTTYPE = _REJECT.enum_types_by_name['RejectType']
_PERMISSIONDENIED_DENYTYPE = _PERMISSIONDENIED.enum_types_by_name['DenyType']
_CONTEXTACTIONMODIFY_CONTEXT = _CONTEXTACTIONMODIFY.enum_types_by_name['Context']
_CONTEXTACTIONMODIFY_OPERATION = _CONTEXTACTIONMODIFY.enum_types_by_name['Operation']
Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.Version)
  })
_sym_db.RegisterMessage(Version)

UDPTunnel = _reflection.GeneratedProtocolMessageType('UDPTunnel', (_message.Message,), {
  'DESCRIPTOR' : _UDPTUNNEL,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.UDPTunnel)
  })
_sym_db.RegisterMessage(UDPTunnel)

Authenticate = _reflection.GeneratedProtocolMessageType('Authenticate', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATE,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.Authenticate)
  })
_sym_db.RegisterMessage(Authenticate)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), {
  'DESCRIPTOR' : _PING,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.Ping)
  })
_sym_db.RegisterMessage(Ping)

Reject = _reflection.GeneratedProtocolMessageType('Reject', (_message.Message,), {
  'DESCRIPTOR' : _REJECT,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.Reject)
  })
_sym_db.RegisterMessage(Reject)

ServerSync = _reflection.GeneratedProtocolMessageType('ServerSync', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSYNC,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.ServerSync)
  })
_sym_db.RegisterMessage(ServerSync)

ChannelRemove = _reflection.GeneratedProtocolMessageType('ChannelRemove', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELREMOVE,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.ChannelRemove)
  })
_sym_db.RegisterMessage(ChannelRemove)

ChannelState = _reflection.GeneratedProtocolMessageType('ChannelState', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELSTATE,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.ChannelState)
  })
_sym_db.RegisterMessage(ChannelState)

UserRemove = _reflection.GeneratedProtocolMessageType('UserRemove', (_message.Message,), {
  'DESCRIPTOR' : _USERREMOVE,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.UserRemove)
  })
_sym_db.RegisterMessage(UserRemove)

UserState = _reflection.GeneratedProtocolMessageType('UserState', (_message.Message,), {
  'DESCRIPTOR' : _USERSTATE,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.UserState)
  })
_sym_db.RegisterMessage(UserState)

BanList = _reflection.GeneratedProtocolMessageType('BanList', (_message.Message,), {

  'BanEntry' : _reflection.GeneratedProtocolMessageType('BanEntry', (_message.Message,), {
    'DESCRIPTOR' : _BANLIST_BANENTRY,
    '__module__' : 'Mumble_pb2'
    # @@protoc_insertion_point(class_scope:MumbleProto.BanList.BanEntry)
    })
  ,
  'DESCRIPTOR' : _BANLIST,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.BanList)
  })
_sym_db.RegisterMessage(BanList)
_sym_db.RegisterMessage(BanList.BanEntry)

TextMessage = _reflection.GeneratedProtocolMessageType('TextMessage', (_message.Message,), {
  'DESCRIPTOR' : _TEXTMESSAGE,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.TextMessage)
  })
_sym_db.RegisterMessage(TextMessage)

PermissionDenied = _reflection.GeneratedProtocolMessageType('PermissionDenied', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONDENIED,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.PermissionDenied)
  })
_sym_db.RegisterMessage(PermissionDenied)

ACL = _reflection.GeneratedProtocolMessageType('ACL', (_message.Message,), {

  'ChanGroup' : _reflection.GeneratedProtocolMessageType('ChanGroup', (_message.Message,), {
    'DESCRIPTOR' : _ACL_CHANGROUP,
    '__module__' : 'Mumble_pb2'
    # @@protoc_insertion_point(class_scope:MumbleProto.ACL.ChanGroup)
    })
  ,

  'ChanACL' : _reflection.GeneratedProtocolMessageType('ChanACL', (_message.Message,), {
    'DESCRIPTOR' : _ACL_CHANACL,
    '__module__' : 'Mumble_pb2'
    # @@protoc_insertion_point(class_scope:MumbleProto.ACL.ChanACL)
    })
  ,
  'DESCRIPTOR' : _ACL,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.ACL)
  })
_sym_db.RegisterMessage(ACL)
_sym_db.RegisterMessage(ACL.ChanGroup)
_sym_db.RegisterMessage(ACL.ChanACL)

QueryUsers = _reflection.GeneratedProtocolMessageType('QueryUsers', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUSERS,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.QueryUsers)
  })
_sym_db.RegisterMessage(QueryUsers)

CryptSetup = _reflection.GeneratedProtocolMessageType('CryptSetup', (_message.Message,), {
  'DESCRIPTOR' : _CRYPTSETUP,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.CryptSetup)
  })
_sym_db.RegisterMessage(CryptSetup)

ContextActionModify = _reflection.GeneratedProtocolMessageType('ContextActionModify', (_message.Message,), {
  'DESCRIPTOR' : _CONTEXTACTIONMODIFY,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.ContextActionModify)
  })
_sym_db.RegisterMessage(ContextActionModify)

ContextAction = _reflection.GeneratedProtocolMessageType('ContextAction', (_message.Message,), {
  'DESCRIPTOR' : _CONTEXTACTION,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.ContextAction)
  })
_sym_db.RegisterMessage(ContextAction)

UserList = _reflection.GeneratedProtocolMessageType('UserList', (_message.Message,), {

  'User' : _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
    'DESCRIPTOR' : _USERLIST_USER,
    '__module__' : 'Mumble_pb2'
    # @@protoc_insertion_point(class_scope:MumbleProto.UserList.User)
    })
  ,
  'DESCRIPTOR' : _USERLIST,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.UserList)
  })
_sym_db.RegisterMessage(UserList)
_sym_db.RegisterMessage(UserList.User)

VoiceTarget = _reflection.GeneratedProtocolMessageType('VoiceTarget', (_message.Message,), {

  'Target' : _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
    'DESCRIPTOR' : _VOICETARGET_TARGET,
    '__module__' : 'Mumble_pb2'
    # @@protoc_insertion_point(class_scope:MumbleProto.VoiceTarget.Target)
    })
  ,
  'DESCRIPTOR' : _VOICETARGET,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.VoiceTarget)
  })
_sym_db.RegisterMessage(VoiceTarget)
_sym_db.RegisterMessage(VoiceTarget.Target)

PermissionQuery = _reflection.GeneratedProtocolMessageType('PermissionQuery', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONQUERY,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.PermissionQuery)
  })
_sym_db.RegisterMessage(PermissionQuery)

CodecVersion = _reflection.GeneratedProtocolMessageType('CodecVersion', (_message.Message,), {
  'DESCRIPTOR' : _CODECVERSION,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.CodecVersion)
  })
_sym_db.RegisterMessage(CodecVersion)

UserStats = _reflection.GeneratedProtocolMessageType('UserStats', (_message.Message,), {

  'Stats' : _reflection.GeneratedProtocolMessageType('Stats', (_message.Message,), {
    'DESCRIPTOR' : _USERSTATS_STATS,
    '__module__' : 'Mumble_pb2'
    # @@protoc_insertion_point(class_scope:MumbleProto.UserStats.Stats)
    })
  ,
  'DESCRIPTOR' : _USERSTATS,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.UserStats)
  })
_sym_db.RegisterMessage(UserStats)
_sym_db.RegisterMessage(UserStats.Stats)

RequestBlob = _reflection.GeneratedProtocolMessageType('RequestBlob', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTBLOB,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.RequestBlob)
  })
_sym_db.RegisterMessage(RequestBlob)

ServerConfig = _reflection.GeneratedProtocolMessageType('ServerConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVERCONFIG,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.ServerConfig)
  })
_sym_db.RegisterMessage(ServerConfig)

SuggestConfig = _reflection.GeneratedProtocolMessageType('SuggestConfig', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTCONFIG,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.SuggestConfig)
  })
_sym_db.RegisterMessage(SuggestConfig)

PluginDataTransmission = _reflection.GeneratedProtocolMessageType('PluginDataTransmission', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINDATATRANSMISSION,
  '__module__' : 'Mumble_pb2'
  # @@protoc_insertion_point(class_scope:MumbleProto.PluginDataTransmission)
  })
_sym_db.RegisterMessage(PluginDataTransmission)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001'
  _PLUGINDATATRANSMISSION.fields_by_name['receiverSessions']._options = None
  _PLUGINDATATRANSMISSION.fields_by_name['receiverSessions']._serialized_options = b'\020\001'
  _VERSION._serialized_start=29
  _VERSION._serialized_end=104
  _UDPTUNNEL._serialized_start=106
  _UDPTUNNEL._serialized_end=133
  _AUTHENTICATE._serialized_start=135
  _AUTHENTICATE._serialized_end=245
  _PING._serialized_start=248
  _PING._serialized_end=461
  _REJECT._serialized_start=464
  _REJECT._serialized_end=711
  _REJECT_REJECTTYPE._serialized_start=537
  _REJECT_REJECTTYPE._serialized_end=711
  _SERVERSYNC._serialized_start=713
  _SERVERSYNC._serialized_end=808
  _CHANNELREMOVE._serialized_start=810
  _CHANNELREMOVE._serialized_end=845
  _CHANNELSTATE._serialized_start=848
  _CHANNELSTATE._serialized_end=1129
  _USERREMOVE._serialized_start=1131
  _USERREMOVE._serialized_end=1204
  _USERSTATE._serialized_start=1207
  _USERSTATE._serialized_end=1669
  _BANLIST._serialized_start=1672
  _BANLIST._serialized_end=1868
  _BANLIST_BANENTRY._serialized_start=1750
  _BANLIST_BANENTRY._serialized_end=1868
  _TEXTMESSAGE._serialized_start=1870
  _TEXTMESSAGE._serialized_end=1969
  _PERMISSIONDENIED._serialized_start=1972
  _PERMISSIONDENIED._serialized_end=2395
  _PERMISSIONDENIED_DENYTYPE._serialized_start=2134
  _PERMISSIONDENIED_DENYTYPE._serialized_end=2395
  _ACL._serialized_start=2398
  _ACL._serialized_end=2866
  _ACL_CHANGROUP._serialized_start=2560
  _ACL_CHANGROUP._serialized_end=2716
  _ACL_CHANACL._serialized_start=2719
  _ACL_CHANACL._serialized_end=2866
  _QUERYUSERS._serialized_start=2868
  _QUERYUSERS._serialized_end=2908
  _CRYPTSETUP._serialized_start=2910
  _CRYPTSETUP._serialized_end=2979
  _CONTEXTACTIONMODIFY._serialized_start=2982
  _CONTEXTACTIONMODIFY._serialized_end=3193
  _CONTEXTACTIONMODIFY_CONTEXT._serialized_start=3115
  _CONTEXTACTIONMODIFY_CONTEXT._serialized_end=3159
  _CONTEXTACTIONMODIFY_OPERATION._serialized_start=3161
  _CONTEXTACTIONMODIFY_OPERATION._serialized_end=3193
  _CONTEXTACTION._serialized_start=3195
  _CONTEXTACTION._serialized_end=3263
  _USERLIST._serialized_start=3266
  _USERLIST._serialized_end=3399
  _USERLIST_USER._serialized_start=3321
  _USERLIST_USER._serialized_end=3399
  _VOICETARGET._serialized_start=3402
  _VOICETARGET._serialized_end=3586
  _VOICETARGET_TARGET._serialized_start=3479
  _VOICETARGET_TARGET._serialized_end=3586
  _PERMISSIONQUERY._serialized_start=3588
  _PERMISSIONQUERY._serialized_end=3668
  _CODECVERSION._serialized_start=3670
  _CODECVERSION._serialized_end=3762
  _USERSTATS._serialized_start=3765
  _USERSTATS._serialized_end=4333
  _USERSTATS_STATS._serialized_start=4268
  _USERSTATS_STATS._serialized_end=4333
  _REQUESTBLOB._serialized_start=4335
  _REQUESTBLOB._serialized_end=4427
  _SERVERCONFIG._serialized_start=4430
  _SERVERCONFIG._serialized_end=4609
  _SUGGESTCONFIG._serialized_start=4611
  _SUGGESTCONFIG._serialized_end=4685
  _PLUGINDATATRANSMISSION._serialized_start=4687
  _PLUGINDATATRANSMISSION._serialized_end=4794
# @@protoc_insertion_point(module_scope)
