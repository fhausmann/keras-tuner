# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kerastuner/protos/service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kerastuner.protos import kerastuner_pb2 as kerastuner_dot_protos_dot_kerastuner__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kerastuner/protos/service.proto',
  package='kerastuner',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fkerastuner/protos/service.proto\x12\nkerastuner\x1a\"kerastuner/protos/kerastuner.proto\"\x11\n\x0fGetSpaceRequest\"H\n\x10GetSpaceResponse\x12\x34\n\x0fhyperparameters\x18\x01 \x01(\x0b\x32\x1b.kerastuner.HyperParameters\"J\n\x12UpdateSpaceRequest\x12\x34\n\x0fhyperparameters\x18\x01 \x01(\x0b\x32\x1b.kerastuner.HyperParameters\"\x15\n\x13UpdateSpaceResponse\"&\n\x12\x43reateTrialRequest\x12\x10\n\x08tuner_id\x18\x01 \x01(\t\"7\n\x13\x43reateTrialResponse\x12 \n\x05trial\x18\x01 \x01(\x0b\x32\x11.kerastuner.Trial\"\xa2\x01\n\x12UpdateTrialRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\t\x12<\n\x07metrics\x18\x02 \x03(\x0b\x32+.kerastuner.UpdateTrialRequest.MetricsEntry\x12\x0c\n\x04step\x18\x03 \x01(\x03\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\">\n\x13UpdateTrialResponse\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.kerastuner.TrialStatus\"L\n\x0f\x45ndTrialRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\t\x12\'\n\x06status\x18\x02 \x01(\x0e\x32\x17.kerastuner.TrialStatus\"\x12\n\x10\x45ndTrialResponse\"*\n\x14GetBestTrialsRequest\x12\x12\n\nnum_trials\x18\x01 \x01(\x03\":\n\x15GetBestTrialsResponse\x12!\n\x06trials\x18\x01 \x03(\x0b\x32\x11.kerastuner.Trial\"#\n\x0fGetTrialRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\t\"4\n\x10GetTrialResponse\x12 \n\x05trial\x18\x01 \x01(\x0b\x32\x11.kerastuner.Trial2\xb1\x04\n\x06Oracle\x12G\n\x08GetSpace\x12\x1b.kerastuner.GetSpaceRequest\x1a\x1c.kerastuner.GetSpaceResponse\"\x00\x12P\n\x0bUpdateSpace\x12\x1e.kerastuner.UpdateSpaceRequest\x1a\x1f.kerastuner.UpdateSpaceResponse\"\x00\x12P\n\x0b\x43reateTrial\x12\x1e.kerastuner.CreateTrialRequest\x1a\x1f.kerastuner.CreateTrialResponse\"\x00\x12P\n\x0bUpdateTrial\x12\x1e.kerastuner.UpdateTrialRequest\x1a\x1f.kerastuner.UpdateTrialResponse\"\x00\x12G\n\x08\x45ndTrial\x12\x1b.kerastuner.EndTrialRequest\x1a\x1c.kerastuner.EndTrialResponse\"\x00\x12V\n\rGetBestTrials\x12 .kerastuner.GetBestTrialsRequest\x1a!.kerastuner.GetBestTrialsResponse\"\x00\x12G\n\x08GetTrial\x12\x1b.kerastuner.GetTrialRequest\x1a\x1c.kerastuner.GetTrialResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[kerastuner_dot_protos_dot_kerastuner__pb2.DESCRIPTOR,])




_GETSPACEREQUEST = _descriptor.Descriptor(
  name='GetSpaceRequest',
  full_name='kerastuner.GetSpaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=83,
  serialized_end=100,
)


_GETSPACERESPONSE = _descriptor.Descriptor(
  name='GetSpaceResponse',
  full_name='kerastuner.GetSpaceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hyperparameters', full_name='kerastuner.GetSpaceResponse.hyperparameters', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=174,
)


_UPDATESPACEREQUEST = _descriptor.Descriptor(
  name='UpdateSpaceRequest',
  full_name='kerastuner.UpdateSpaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hyperparameters', full_name='kerastuner.UpdateSpaceRequest.hyperparameters', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=250,
)


_UPDATESPACERESPONSE = _descriptor.Descriptor(
  name='UpdateSpaceResponse',
  full_name='kerastuner.UpdateSpaceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=252,
  serialized_end=273,
)


_CREATETRIALREQUEST = _descriptor.Descriptor(
  name='CreateTrialRequest',
  full_name='kerastuner.CreateTrialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tuner_id', full_name='kerastuner.CreateTrialRequest.tuner_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=313,
)


_CREATETRIALRESPONSE = _descriptor.Descriptor(
  name='CreateTrialResponse',
  full_name='kerastuner.CreateTrialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trial', full_name='kerastuner.CreateTrialResponse.trial', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=370,
)


_UPDATETRIALREQUEST_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='kerastuner.UpdateTrialRequest.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kerastuner.UpdateTrialRequest.MetricsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.UpdateTrialRequest.MetricsEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=489,
  serialized_end=535,
)

_UPDATETRIALREQUEST = _descriptor.Descriptor(
  name='UpdateTrialRequest',
  full_name='kerastuner.UpdateTrialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trial_id', full_name='kerastuner.UpdateTrialRequest.trial_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='kerastuner.UpdateTrialRequest.metrics', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='kerastuner.UpdateTrialRequest.step', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATETRIALREQUEST_METRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=535,
)


_UPDATETRIALRESPONSE = _descriptor.Descriptor(
  name='UpdateTrialResponse',
  full_name='kerastuner.UpdateTrialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='kerastuner.UpdateTrialResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=537,
  serialized_end=599,
)


_ENDTRIALREQUEST = _descriptor.Descriptor(
  name='EndTrialRequest',
  full_name='kerastuner.EndTrialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trial_id', full_name='kerastuner.EndTrialRequest.trial_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='kerastuner.EndTrialRequest.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=601,
  serialized_end=677,
)


_ENDTRIALRESPONSE = _descriptor.Descriptor(
  name='EndTrialResponse',
  full_name='kerastuner.EndTrialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=679,
  serialized_end=697,
)


_GETBESTTRIALSREQUEST = _descriptor.Descriptor(
  name='GetBestTrialsRequest',
  full_name='kerastuner.GetBestTrialsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_trials', full_name='kerastuner.GetBestTrialsRequest.num_trials', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=699,
  serialized_end=741,
)


_GETBESTTRIALSRESPONSE = _descriptor.Descriptor(
  name='GetBestTrialsResponse',
  full_name='kerastuner.GetBestTrialsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trials', full_name='kerastuner.GetBestTrialsResponse.trials', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=801,
)


_GETTRIALREQUEST = _descriptor.Descriptor(
  name='GetTrialRequest',
  full_name='kerastuner.GetTrialRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trial_id', full_name='kerastuner.GetTrialRequest.trial_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=803,
  serialized_end=838,
)


_GETTRIALRESPONSE = _descriptor.Descriptor(
  name='GetTrialResponse',
  full_name='kerastuner.GetTrialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trial', full_name='kerastuner.GetTrialResponse.trial', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=840,
  serialized_end=892,
)

_GETSPACERESPONSE.fields_by_name['hyperparameters'].message_type = kerastuner_dot_protos_dot_kerastuner__pb2._HYPERPARAMETERS
_UPDATESPACEREQUEST.fields_by_name['hyperparameters'].message_type = kerastuner_dot_protos_dot_kerastuner__pb2._HYPERPARAMETERS
_CREATETRIALRESPONSE.fields_by_name['trial'].message_type = kerastuner_dot_protos_dot_kerastuner__pb2._TRIAL
_UPDATETRIALREQUEST_METRICSENTRY.containing_type = _UPDATETRIALREQUEST
_UPDATETRIALREQUEST.fields_by_name['metrics'].message_type = _UPDATETRIALREQUEST_METRICSENTRY
_UPDATETRIALRESPONSE.fields_by_name['status'].enum_type = kerastuner_dot_protos_dot_kerastuner__pb2._TRIALSTATUS
_ENDTRIALREQUEST.fields_by_name['status'].enum_type = kerastuner_dot_protos_dot_kerastuner__pb2._TRIALSTATUS
_GETBESTTRIALSRESPONSE.fields_by_name['trials'].message_type = kerastuner_dot_protos_dot_kerastuner__pb2._TRIAL
_GETTRIALRESPONSE.fields_by_name['trial'].message_type = kerastuner_dot_protos_dot_kerastuner__pb2._TRIAL
DESCRIPTOR.message_types_by_name['GetSpaceRequest'] = _GETSPACEREQUEST
DESCRIPTOR.message_types_by_name['GetSpaceResponse'] = _GETSPACERESPONSE
DESCRIPTOR.message_types_by_name['UpdateSpaceRequest'] = _UPDATESPACEREQUEST
DESCRIPTOR.message_types_by_name['UpdateSpaceResponse'] = _UPDATESPACERESPONSE
DESCRIPTOR.message_types_by_name['CreateTrialRequest'] = _CREATETRIALREQUEST
DESCRIPTOR.message_types_by_name['CreateTrialResponse'] = _CREATETRIALRESPONSE
DESCRIPTOR.message_types_by_name['UpdateTrialRequest'] = _UPDATETRIALREQUEST
DESCRIPTOR.message_types_by_name['UpdateTrialResponse'] = _UPDATETRIALRESPONSE
DESCRIPTOR.message_types_by_name['EndTrialRequest'] = _ENDTRIALREQUEST
DESCRIPTOR.message_types_by_name['EndTrialResponse'] = _ENDTRIALRESPONSE
DESCRIPTOR.message_types_by_name['GetBestTrialsRequest'] = _GETBESTTRIALSREQUEST
DESCRIPTOR.message_types_by_name['GetBestTrialsResponse'] = _GETBESTTRIALSRESPONSE
DESCRIPTOR.message_types_by_name['GetTrialRequest'] = _GETTRIALREQUEST
DESCRIPTOR.message_types_by_name['GetTrialResponse'] = _GETTRIALRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSpaceRequest = _reflection.GeneratedProtocolMessageType('GetSpaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSPACEREQUEST,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.GetSpaceRequest)
  })
_sym_db.RegisterMessage(GetSpaceRequest)

GetSpaceResponse = _reflection.GeneratedProtocolMessageType('GetSpaceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSPACERESPONSE,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.GetSpaceResponse)
  })
_sym_db.RegisterMessage(GetSpaceResponse)

UpdateSpaceRequest = _reflection.GeneratedProtocolMessageType('UpdateSpaceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESPACEREQUEST,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.UpdateSpaceRequest)
  })
_sym_db.RegisterMessage(UpdateSpaceRequest)

UpdateSpaceResponse = _reflection.GeneratedProtocolMessageType('UpdateSpaceResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESPACERESPONSE,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.UpdateSpaceResponse)
  })
_sym_db.RegisterMessage(UpdateSpaceResponse)

CreateTrialRequest = _reflection.GeneratedProtocolMessageType('CreateTrialRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETRIALREQUEST,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.CreateTrialRequest)
  })
_sym_db.RegisterMessage(CreateTrialRequest)

CreateTrialResponse = _reflection.GeneratedProtocolMessageType('CreateTrialResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATETRIALRESPONSE,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.CreateTrialResponse)
  })
_sym_db.RegisterMessage(CreateTrialResponse)

UpdateTrialRequest = _reflection.GeneratedProtocolMessageType('UpdateTrialRequest', (_message.Message,), {

  'MetricsEntry' : _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATETRIALREQUEST_METRICSENTRY,
    '__module__' : 'kerastuner.protos.service_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.UpdateTrialRequest.MetricsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATETRIALREQUEST,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.UpdateTrialRequest)
  })
_sym_db.RegisterMessage(UpdateTrialRequest)
_sym_db.RegisterMessage(UpdateTrialRequest.MetricsEntry)

UpdateTrialResponse = _reflection.GeneratedProtocolMessageType('UpdateTrialResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETRIALRESPONSE,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.UpdateTrialResponse)
  })
_sym_db.RegisterMessage(UpdateTrialResponse)

EndTrialRequest = _reflection.GeneratedProtocolMessageType('EndTrialRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENDTRIALREQUEST,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.EndTrialRequest)
  })
_sym_db.RegisterMessage(EndTrialRequest)

EndTrialResponse = _reflection.GeneratedProtocolMessageType('EndTrialResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENDTRIALRESPONSE,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.EndTrialResponse)
  })
_sym_db.RegisterMessage(EndTrialResponse)

GetBestTrialsRequest = _reflection.GeneratedProtocolMessageType('GetBestTrialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBESTTRIALSREQUEST,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.GetBestTrialsRequest)
  })
_sym_db.RegisterMessage(GetBestTrialsRequest)

GetBestTrialsResponse = _reflection.GeneratedProtocolMessageType('GetBestTrialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBESTTRIALSRESPONSE,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.GetBestTrialsResponse)
  })
_sym_db.RegisterMessage(GetBestTrialsResponse)

GetTrialRequest = _reflection.GeneratedProtocolMessageType('GetTrialRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRIALREQUEST,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.GetTrialRequest)
  })
_sym_db.RegisterMessage(GetTrialRequest)

GetTrialResponse = _reflection.GeneratedProtocolMessageType('GetTrialResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTRIALRESPONSE,
  '__module__' : 'kerastuner.protos.service_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.GetTrialResponse)
  })
_sym_db.RegisterMessage(GetTrialResponse)


_UPDATETRIALREQUEST_METRICSENTRY._options = None

_ORACLE = _descriptor.ServiceDescriptor(
  name='Oracle',
  full_name='kerastuner.Oracle',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=895,
  serialized_end=1456,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSpace',
    full_name='kerastuner.Oracle.GetSpace',
    index=0,
    containing_service=None,
    input_type=_GETSPACEREQUEST,
    output_type=_GETSPACERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateSpace',
    full_name='kerastuner.Oracle.UpdateSpace',
    index=1,
    containing_service=None,
    input_type=_UPDATESPACEREQUEST,
    output_type=_UPDATESPACERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTrial',
    full_name='kerastuner.Oracle.CreateTrial',
    index=2,
    containing_service=None,
    input_type=_CREATETRIALREQUEST,
    output_type=_CREATETRIALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTrial',
    full_name='kerastuner.Oracle.UpdateTrial',
    index=3,
    containing_service=None,
    input_type=_UPDATETRIALREQUEST,
    output_type=_UPDATETRIALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EndTrial',
    full_name='kerastuner.Oracle.EndTrial',
    index=4,
    containing_service=None,
    input_type=_ENDTRIALREQUEST,
    output_type=_ENDTRIALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBestTrials',
    full_name='kerastuner.Oracle.GetBestTrials',
    index=5,
    containing_service=None,
    input_type=_GETBESTTRIALSREQUEST,
    output_type=_GETBESTTRIALSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTrial',
    full_name='kerastuner.Oracle.GetTrial',
    index=6,
    containing_service=None,
    input_type=_GETTRIALREQUEST,
    output_type=_GETTRIALRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORACLE)

DESCRIPTOR.services_by_name['Oracle'] = _ORACLE

# @@protoc_insertion_point(module_scope)