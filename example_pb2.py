# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='example',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rexample.proto\x12\x07\x65xample\"*\n\x06\x41mount\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x10\n\x08\x63urrency\x18\x02 \x01(\tb\x06proto3'
)




_AMOUNT = _descriptor.Descriptor(
  name='Amount',
  full_name='example.Amount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='example.Amount.amount', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='example.Amount.currency', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['Amount'] = _AMOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Amount = _reflection.GeneratedProtocolMessageType('Amount', (_message.Message,), {
  'DESCRIPTOR' : _AMOUNT,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Amount)
  })
_sym_db.RegisterMessage(Amount)


# @@protoc_insertion_point(module_scope)