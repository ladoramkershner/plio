# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ControlNetFileHeaderV0005.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ControlNetFileHeaderV0005.proto',
  package='Isis',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1f\x43ontrolNetFileHeaderV0005.proto\x12\x04Isis\"\xb8\x01\n\x19\x43ontrolNetFileHeaderV0005\x12\x11\n\tnetworkId\x18\x01 \x02(\t\x12\x12\n\ntargetName\x18\x02 \x02(\t\x12\x0f\n\x07\x63reated\x18\x03 \x01(\t\x12\x14\n\x0clastModified\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x10\n\x08userName\x18\x06 \x01(\t\x12\x11\n\tnumPoints\x18\x07 \x01(\x05\x12\x13\n\x0btargetRadii\x18\n \x03(\x01')
)




_CONTROLNETFILEHEADERV0005 = _descriptor.Descriptor(
  name='ControlNetFileHeaderV0005',
  full_name='Isis.ControlNetFileHeaderV0005',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='networkId', full_name='Isis.ControlNetFileHeaderV0005.networkId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetName', full_name='Isis.ControlNetFileHeaderV0005.targetName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='Isis.ControlNetFileHeaderV0005.created', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastModified', full_name='Isis.ControlNetFileHeaderV0005.lastModified', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Isis.ControlNetFileHeaderV0005.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='Isis.ControlNetFileHeaderV0005.userName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numPoints', full_name='Isis.ControlNetFileHeaderV0005.numPoints', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetRadii', full_name='Isis.ControlNetFileHeaderV0005.targetRadii', index=7,
      number=10, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=226,
)

DESCRIPTOR.message_types_by_name['ControlNetFileHeaderV0005'] = _CONTROLNETFILEHEADERV0005
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlNetFileHeaderV0005 = _reflection.GeneratedProtocolMessageType('ControlNetFileHeaderV0005', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLNETFILEHEADERV0005,
  __module__ = 'ControlNetFileHeaderV0005_pb2'
  # @@protoc_insertion_point(class_scope:Isis.ControlNetFileHeaderV0005)
  ))
_sym_db.RegisterMessage(ControlNetFileHeaderV0005)


# @@protoc_insertion_point(module_scope)
