# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"2\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x03\")\n\x06\x46\x61\x63tor\x12\t\n\x01\x61\x18\x01 \x01(\x03\x12\t\n\x01\x62\x18\x02 \x01(\x03\x12\t\n\x01\x63\x18\x03 \x01(\x03\"\x13\n\x06Result\x12\t\n\x01x\x18\x01 \x03(\t2\x80\x02\n\x07Greeter\x12>\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12\x39\n\rSayHelloAgain\x12\x12.helloworld.Person\x1a\x12.helloworld.Person\"\x00\x12\x37\n\x0b\x43\x61lculation\x12\x12.helloworld.Factor\x1a\x12.helloworld.Result\"\x00\x12\x41\n\x07\x42idirec\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00(\x01\x30\x01\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')



_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLOREPLY = DESCRIPTOR.message_types_by_name['HelloReply']
_PERSON = DESCRIPTOR.message_types_by_name['Person']
_FACTOR = DESCRIPTOR.message_types_by_name['Factor']
_RESULT = DESCRIPTOR.message_types_by_name['Result']
HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Person)
  })
_sym_db.RegisterMessage(Person)

Factor = _reflection.GeneratedProtocolMessageType('Factor', (_message.Message,), {
  'DESCRIPTOR' : _FACTOR,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Factor)
  })
_sym_db.RegisterMessage(Factor)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Result)
  })
_sym_db.RegisterMessage(Result)

_GREETER = DESCRIPTOR.services_by_name['Greeter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _HELLOREQUEST._serialized_start=32
  _HELLOREQUEST._serialized_end=60
  _HELLOREPLY._serialized_start=62
  _HELLOREPLY._serialized_end=91
  _PERSON._serialized_start=93
  _PERSON._serialized_end=143
  _FACTOR._serialized_start=145
  _FACTOR._serialized_end=186
  _RESULT._serialized_start=188
  _RESULT._serialized_end=207
  _GREETER._serialized_start=210
  _GREETER._serialized_end=466
# @@protoc_insertion_point(module_scope)
