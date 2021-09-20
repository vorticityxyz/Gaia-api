# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gaia.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gaia.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ngaia.proto\"\x17\n\x05\x43hunk\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\"K\n\nBatchChunk\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x12\x0c\n\x04shot\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x10\n\x08progress\x18\x04 \x01(\x02\" \n\x0f\x44ownloadRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\x1d\n\x0bUploadReply\x12\x0e\n\x06length\x18\x01 \x01(\x03\"\x1e\n\rStatusRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\x1d\n\x0bStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x1f\n\x0e\x45xecuteRequest\x12\r\n\x05token\x18\x01 \x01(\t\"!\n\rProgressReply\x12\x10\n\x08progress\x18\x01 \x01(\x02\"\x1f\n\x0e\x43leanUpRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\x1d\n\x0bSanityReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x1d\n\x0cResetRequest\x12\r\n\x05token\x18\x01 \x01(\t\"5\n\x12\x42\x61tchStatusRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"e\n\x10\x42\x61tchStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04shot\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x10\n\x08progress\x18\x04 \x01(\x02\x12\x12\n\nfileExists\x18\x05 \x01(\x08\"7\n\x14\x42\x61tchDownloadRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t2\xd0\n\n\nGaiaServer\x12-\n\x0bStatusCheck\x12\x0e.StatusRequest\x1a\x0c.StatusReply\"\x00\x12&\n\x05Reset\x12\r.ResetRequest\x1a\x0c.StatusReply\"\x00\x12\'\n\x0bSanityCheck\x12\x06.Chunk\x1a\x0c.SanityReply\"\x00(\x01\x12\"\n\x06Upload\x12\x06.Chunk\x1a\x0c.UploadReply\"\x00(\x01\x12.\n\x07\x45xecute\x12\x0f.ExecuteRequest\x1a\x0e.ProgressReply\"\x00\x30\x01\x12(\n\x08\x44ownload\x12\x10.DownloadRequest\x1a\x06.Chunk\"\x00\x30\x01\x12*\n\x07\x43leanUp\x12\x0f.CleanUpRequest\x1a\x0c.StatusReply\"\x00\x12*\n\x0ertmSanityCheck\x12\x06.Chunk\x1a\x0c.SanityReply\"\x00(\x01\x12%\n\trtmUpload\x12\x06.Chunk\x1a\x0c.UploadReply\"\x00(\x01\x12\x31\n\nrtmExecute\x12\x0f.ExecuteRequest\x1a\x0e.ProgressReply\"\x00\x30\x01\x12+\n\x0brtmDownload\x12\x10.DownloadRequest\x1a\x06.Chunk\"\x00\x30\x01\x12-\n\nrtmCleanUp\x12\x0f.CleanUpRequest\x1a\x0c.StatusReply\"\x00\x12/\n\x13\x65\x46orwardSanityCheck\x12\x06.Chunk\x1a\x0c.SanityReply\"\x00(\x01\x12*\n\x0e\x65\x46orwardUpload\x12\x06.Chunk\x1a\x0c.UploadReply\"\x00(\x01\x12\x36\n\x0f\x65\x46orwardExecute\x12\x0f.ExecuteRequest\x1a\x0e.ProgressReply\"\x00\x30\x01\x12\x30\n\x10\x65\x46orwardDownload\x12\x10.DownloadRequest\x1a\x06.Chunk\"\x00\x30\x01\x12\x32\n\x0f\x65\x46orwardCleanUp\x12\x0f.CleanUpRequest\x1a\x0c.StatusReply\"\x00\x12+\n\x0f\x65RTMSanityCheck\x12\x06.Chunk\x1a\x0c.SanityReply\"\x00(\x01\x12&\n\neRTMUpload\x12\x06.Chunk\x1a\x0c.UploadReply\"\x00(\x01\x12\x32\n\x0b\x65RTMExecute\x12\x0f.ExecuteRequest\x1a\x0e.ProgressReply\"\x00\x30\x01\x12,\n\x0c\x65RTMDownload\x12\x10.DownloadRequest\x1a\x06.Chunk\"\x00\x30\x01\x12.\n\x0b\x65RTMCleanUp\x12\x0f.CleanUpRequest\x1a\x0c.StatusReply\"\x00\x12\x33\n\x17\x42\x61tchForwardSanityCheck\x12\x06.Chunk\x1a\x0c.SanityReply\"\x00(\x01\x12.\n\x12\x42\x61tchForwardUpload\x12\x06.Chunk\x1a\x0c.UploadReply\"\x00(\x01\x12\x37\n\x14\x42\x61tchForwardInitExec\x12\x0f.ExecuteRequest\x1a\x0c.StatusReply\"\x00\x12>\n\x12\x42\x61tchForwardStatus\x12\x13.BatchStatusRequest\x1a\x11.BatchStatusReply\"\x00\x12>\n\x14\x42\x61tchForwardDownload\x12\x15.BatchDownloadRequest\x1a\x0b.BatchChunk\"\x00\x30\x01\x12\x36\n\x13\x42\x61tchForwardCleanUp\x12\x0f.CleanUpRequest\x1a\x0c.StatusReply\"\x00\x62\x06proto3'
)




_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='Chunk.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=14,
  serialized_end=37,
)


_BATCHCHUNK = _descriptor.Descriptor(
  name='BatchChunk',
  full_name='BatchChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='BatchChunk.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shot', full_name='BatchChunk.shot', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='BatchChunk.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress', full_name='BatchChunk.progress', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=39,
  serialized_end=114,
)


_DOWNLOADREQUEST = _descriptor.Descriptor(
  name='DownloadRequest',
  full_name='DownloadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='DownloadRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=116,
  serialized_end=148,
)


_UPLOADREPLY = _descriptor.Descriptor(
  name='UploadReply',
  full_name='UploadReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='UploadReply.length', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=150,
  serialized_end=179,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='StatusRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=181,
  serialized_end=211,
)


_STATUSREPLY = _descriptor.Descriptor(
  name='StatusReply',
  full_name='StatusReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='StatusReply.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=213,
  serialized_end=242,
)


_EXECUTEREQUEST = _descriptor.Descriptor(
  name='ExecuteRequest',
  full_name='ExecuteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='ExecuteRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=244,
  serialized_end=275,
)


_PROGRESSREPLY = _descriptor.Descriptor(
  name='ProgressReply',
  full_name='ProgressReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='progress', full_name='ProgressReply.progress', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=277,
  serialized_end=310,
)


_CLEANUPREQUEST = _descriptor.Descriptor(
  name='CleanUpRequest',
  full_name='CleanUpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='CleanUpRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=312,
  serialized_end=343,
)


_SANITYREPLY = _descriptor.Descriptor(
  name='SanityReply',
  full_name='SanityReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanityReply.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=345,
  serialized_end=374,
)


_RESETREQUEST = _descriptor.Descriptor(
  name='ResetRequest',
  full_name='ResetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='ResetRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=376,
  serialized_end=405,
)


_BATCHSTATUSREQUEST = _descriptor.Descriptor(
  name='BatchStatusRequest',
  full_name='BatchStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='BatchStatusRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename', full_name='BatchStatusRequest.filename', index=1,
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
  serialized_start=407,
  serialized_end=460,
)


_BATCHSTATUSREPLY = _descriptor.Descriptor(
  name='BatchStatusReply',
  full_name='BatchStatusReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='BatchStatusReply.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shot', full_name='BatchStatusReply.shot', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='BatchStatusReply.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress', full_name='BatchStatusReply.progress', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileExists', full_name='BatchStatusReply.fileExists', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=462,
  serialized_end=563,
)


_BATCHDOWNLOADREQUEST = _descriptor.Descriptor(
  name='BatchDownloadRequest',
  full_name='BatchDownloadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='BatchDownloadRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename', full_name='BatchDownloadRequest.filename', index=1,
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
  serialized_start=565,
  serialized_end=620,
)

DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['BatchChunk'] = _BATCHCHUNK
DESCRIPTOR.message_types_by_name['DownloadRequest'] = _DOWNLOADREQUEST
DESCRIPTOR.message_types_by_name['UploadReply'] = _UPLOADREPLY
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusReply'] = _STATUSREPLY
DESCRIPTOR.message_types_by_name['ExecuteRequest'] = _EXECUTEREQUEST
DESCRIPTOR.message_types_by_name['ProgressReply'] = _PROGRESSREPLY
DESCRIPTOR.message_types_by_name['CleanUpRequest'] = _CLEANUPREQUEST
DESCRIPTOR.message_types_by_name['SanityReply'] = _SANITYREPLY
DESCRIPTOR.message_types_by_name['ResetRequest'] = _RESETREQUEST
DESCRIPTOR.message_types_by_name['BatchStatusRequest'] = _BATCHSTATUSREQUEST
DESCRIPTOR.message_types_by_name['BatchStatusReply'] = _BATCHSTATUSREPLY
DESCRIPTOR.message_types_by_name['BatchDownloadRequest'] = _BATCHDOWNLOADREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:Chunk)
  })
_sym_db.RegisterMessage(Chunk)

BatchChunk = _reflection.GeneratedProtocolMessageType('BatchChunk', (_message.Message,), {
  'DESCRIPTOR' : _BATCHCHUNK,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:BatchChunk)
  })
_sym_db.RegisterMessage(BatchChunk)

DownloadRequest = _reflection.GeneratedProtocolMessageType('DownloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADREQUEST,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:DownloadRequest)
  })
_sym_db.RegisterMessage(DownloadRequest)

UploadReply = _reflection.GeneratedProtocolMessageType('UploadReply', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADREPLY,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:UploadReply)
  })
_sym_db.RegisterMessage(UploadReply)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

StatusReply = _reflection.GeneratedProtocolMessageType('StatusReply', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREPLY,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:StatusReply)
  })
_sym_db.RegisterMessage(StatusReply)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEREQUEST,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:ExecuteRequest)
  })
_sym_db.RegisterMessage(ExecuteRequest)

ProgressReply = _reflection.GeneratedProtocolMessageType('ProgressReply', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSREPLY,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:ProgressReply)
  })
_sym_db.RegisterMessage(ProgressReply)

CleanUpRequest = _reflection.GeneratedProtocolMessageType('CleanUpRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEANUPREQUEST,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:CleanUpRequest)
  })
_sym_db.RegisterMessage(CleanUpRequest)

SanityReply = _reflection.GeneratedProtocolMessageType('SanityReply', (_message.Message,), {
  'DESCRIPTOR' : _SANITYREPLY,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:SanityReply)
  })
_sym_db.RegisterMessage(SanityReply)

ResetRequest = _reflection.GeneratedProtocolMessageType('ResetRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETREQUEST,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:ResetRequest)
  })
_sym_db.RegisterMessage(ResetRequest)

BatchStatusRequest = _reflection.GeneratedProtocolMessageType('BatchStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHSTATUSREQUEST,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:BatchStatusRequest)
  })
_sym_db.RegisterMessage(BatchStatusRequest)

BatchStatusReply = _reflection.GeneratedProtocolMessageType('BatchStatusReply', (_message.Message,), {
  'DESCRIPTOR' : _BATCHSTATUSREPLY,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:BatchStatusReply)
  })
_sym_db.RegisterMessage(BatchStatusReply)

BatchDownloadRequest = _reflection.GeneratedProtocolMessageType('BatchDownloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHDOWNLOADREQUEST,
  '__module__' : 'gaia_pb2'
  # @@protoc_insertion_point(class_scope:BatchDownloadRequest)
  })
_sym_db.RegisterMessage(BatchDownloadRequest)



_GAIASERVER = _descriptor.ServiceDescriptor(
  name='GaiaServer',
  full_name='GaiaServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=623,
  serialized_end=1983,
  methods=[
  _descriptor.MethodDescriptor(
    name='StatusCheck',
    full_name='GaiaServer.StatusCheck',
    index=0,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Reset',
    full_name='GaiaServer.Reset',
    index=1,
    containing_service=None,
    input_type=_RESETREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SanityCheck',
    full_name='GaiaServer.SanityCheck',
    index=2,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_SANITYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='GaiaServer.Upload',
    index=3,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_UPLOADREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Execute',
    full_name='GaiaServer.Execute',
    index=4,
    containing_service=None,
    input_type=_EXECUTEREQUEST,
    output_type=_PROGRESSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Download',
    full_name='GaiaServer.Download',
    index=5,
    containing_service=None,
    input_type=_DOWNLOADREQUEST,
    output_type=_CHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CleanUp',
    full_name='GaiaServer.CleanUp',
    index=6,
    containing_service=None,
    input_type=_CLEANUPREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='rtmSanityCheck',
    full_name='GaiaServer.rtmSanityCheck',
    index=7,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_SANITYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='rtmUpload',
    full_name='GaiaServer.rtmUpload',
    index=8,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_UPLOADREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='rtmExecute',
    full_name='GaiaServer.rtmExecute',
    index=9,
    containing_service=None,
    input_type=_EXECUTEREQUEST,
    output_type=_PROGRESSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='rtmDownload',
    full_name='GaiaServer.rtmDownload',
    index=10,
    containing_service=None,
    input_type=_DOWNLOADREQUEST,
    output_type=_CHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='rtmCleanUp',
    full_name='GaiaServer.rtmCleanUp',
    index=11,
    containing_service=None,
    input_type=_CLEANUPREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eForwardSanityCheck',
    full_name='GaiaServer.eForwardSanityCheck',
    index=12,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_SANITYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eForwardUpload',
    full_name='GaiaServer.eForwardUpload',
    index=13,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_UPLOADREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eForwardExecute',
    full_name='GaiaServer.eForwardExecute',
    index=14,
    containing_service=None,
    input_type=_EXECUTEREQUEST,
    output_type=_PROGRESSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eForwardDownload',
    full_name='GaiaServer.eForwardDownload',
    index=15,
    containing_service=None,
    input_type=_DOWNLOADREQUEST,
    output_type=_CHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eForwardCleanUp',
    full_name='GaiaServer.eForwardCleanUp',
    index=16,
    containing_service=None,
    input_type=_CLEANUPREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eRTMSanityCheck',
    full_name='GaiaServer.eRTMSanityCheck',
    index=17,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_SANITYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eRTMUpload',
    full_name='GaiaServer.eRTMUpload',
    index=18,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_UPLOADREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eRTMExecute',
    full_name='GaiaServer.eRTMExecute',
    index=19,
    containing_service=None,
    input_type=_EXECUTEREQUEST,
    output_type=_PROGRESSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eRTMDownload',
    full_name='GaiaServer.eRTMDownload',
    index=20,
    containing_service=None,
    input_type=_DOWNLOADREQUEST,
    output_type=_CHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='eRTMCleanUp',
    full_name='GaiaServer.eRTMCleanUp',
    index=21,
    containing_service=None,
    input_type=_CLEANUPREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BatchForwardSanityCheck',
    full_name='GaiaServer.BatchForwardSanityCheck',
    index=22,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_SANITYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BatchForwardUpload',
    full_name='GaiaServer.BatchForwardUpload',
    index=23,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_UPLOADREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BatchForwardInitExec',
    full_name='GaiaServer.BatchForwardInitExec',
    index=24,
    containing_service=None,
    input_type=_EXECUTEREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BatchForwardStatus',
    full_name='GaiaServer.BatchForwardStatus',
    index=25,
    containing_service=None,
    input_type=_BATCHSTATUSREQUEST,
    output_type=_BATCHSTATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BatchForwardDownload',
    full_name='GaiaServer.BatchForwardDownload',
    index=26,
    containing_service=None,
    input_type=_BATCHDOWNLOADREQUEST,
    output_type=_BATCHCHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BatchForwardCleanUp',
    full_name='GaiaServer.BatchForwardCleanUp',
    index=27,
    containing_service=None,
    input_type=_CLEANUPREQUEST,
    output_type=_STATUSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAIASERVER)

DESCRIPTOR.services_by_name['GaiaServer'] = _GAIASERVER

# @@protoc_insertion_point(module_scope)
