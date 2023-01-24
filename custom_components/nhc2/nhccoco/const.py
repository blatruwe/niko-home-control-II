import paho.mqtt.client as mqtt

from enum import Enum

MQTT_PROTOCOL = mqtt.MQTTv311
MQTT_TRANSPORT = 'tcp'
MQTT_CERT_FILE = '/coco_ca.pem'

DEVICE_CONTROL_BUFFER_SIZE = 16
DEVICE_CONTROL_BUFFER_COMMAND_SIZE = 32

KEY_ACTION = 'Action'
KEY_DEVICES = 'Devices'
KEY_DISPLAY_NAME = 'DisplayName'
KEY_FAN_SPEED = 'FanSpeed'
KEY_METHOD = 'Method'
KEY_MODEL = 'Model'
KEY_NAME = 'Name'
KEY_ONLINE = 'Online'
KEY_PARAMS = 'Params'
KEY_PROPERTIES = 'Properties'
KEY_POSITION = 'Position'
KEY_STATUS = 'Status'
KEY_TYPE = 'Type'
KEY_UUID = 'Uuid'
KEY_BASICSTATE = "BasicState"

VALUE_ON = 'On'
VALUE_OFF = 'Off'
VALUE_OPEN = 'Open'
VALUE_STOP = 'Stop'
VALUE_CLOSE = 'Close'
VALUE_TRIGGERED = 'Triggered'

GATE_VALUE_OPEN = 'On'
GATE_VALUE_CLOSE = 'Off'
GATE_VALUE_TRIGGERED = 'Triggered'
GATE_MOVING = 'Intermediate'
KEY_ALIGNED = "Aligned"

THERM_PROGRAM = 'Program'
THERM_OVERRULEACTION = 'OverruleActive'
THERM_OVERRULESETPOINT = 'OverruleSetpoint'
THERM_OVERRULETIME = 'OverruleTime'
THERM_ECOSAVE = 'EcoSave'

ENERGY_REPORT = 'ReportInstantUsage'
ENERGY_POWER = 'ElectricalPower'

INTERNAL_KEY_CALLBACK = 'callbackHolder'

MQTT_METHOD_SYSINFO_PUBLISH = 'systeminfo.publish'
MQTT_METHOD_SYSINFO_PUBLISHED = 'systeminfo.published'
MQTT_METHOD_DEVICES_LIST = 'devices.list'
MQTT_METHOD_DEVICES_CONTROL = 'devices.control'
MQTT_METHOD_DEVICES_STATUS = 'devices.status'
MQTT_METHOD_DEVICES_CHANGED = 'devices.changed'

MQTT_RC_CODES = ['',
                 'Connection refused - incorrect protocol version',
                 'Connection refused - invalid client identifier',
                 'Connection refused - server unavailable',
                 'Connection refused - bad username or password',
                 'Connection refused - not authorised']

MQTT_TOPIC_PUBLIC_AUTH_CMD = 'public/authentication/cmd'
MQTT_TOPIC_PUBLIC_AUTH_RSP = 'public/authentication/rsp'
MQTT_TOPIC_SUFFIX_SYS_EVT = '/system/evt'
MQTT_TOPIC_PUBLIC_CMD = '/system/cmd'
MQTT_TOPIC_PUBLIC_RSP = '/system/rsp'
MQTT_TOPIC_SUFFIX_CMD = '/control/devices/cmd'
MQTT_TOPIC_SUFFIX_RSP = '/control/devices/rsp'
MQTT_TOPIC_SUFFIX_EVT = '/control/devices/evt'

DEVICE_DESCRIPTOR_UUID = 'Uuid'
DEVICE_DESCRIPTOR_TYPE = 'Type'
DEVICE_DESCRIPTOR_TECHNOLOGY = 'Technology'
DEVICE_DESCRIPTOR_MODEL = 'Model'
DEVICE_DESCRIPTOR_IDENTIFIER = 'Identifier'
DEVICE_DESCRIPTOR_NAME = 'Name'
DEVICE_DESCRIPTOR_TRAITS = 'Traits'
DEVICE_DESCRIPTOR_PARAMETERS = 'Parameters'
DEVICE_DESCRIPTOR_PROPERTIES = 'Properties'
DEVICE_DESCRIPTOR_ONLINE = 'Online'
DEVICE_DESCRIPTOR_ONLINE_VALUE_TRUE = 'True'

PARAMETER_ACTION = 'Action'
PARAMETER_BUTTON_ID = 'ButtonId'
PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES = 'DeclineCallAppliedOnAllDevices'
PROPERTY_DECLINE_CALL_APPLIED_ON_ALL_DEVICES_VALUE_TRUE = 'True'
PARAMETER_FEEDBACK_ENABLED = 'FeedbackEnabled'
PARAMETER_FEEDBACK_ENABLED_VALUE_TRUE = 'True'
PARAMETER_MEASURING_ONLY = 'MeasuringOnly'
PARAMETER_MEASURING_ONLY_VALUE_TRUE = 'True'
PARAMETER_RINGTONE = 'Ringtone'

PROPERTY_ALIGNED = 'Aligned'
PROPERTY_ALIGNED_VALUE_TRUE = 'True'
PROPERTY_ALL_OFF_ACTIVE = 'AllOffActive'
PROPERTY_ALL_OFF_ACTIVE_VALUE_TRUE = 'True'
PROPERTY_AMBIENT_TEMPERATURE = 'AmbientTemperature'
PROPERTY_BASIC_STATE = 'BasicState'
PROPERTY_BASIC_STATE_VALUE_INTERMEDIATE = 'Intermediate'
PROPERTY_BASIC_STATE_VALUE_ON = 'On'
PROPERTY_BASIC_STATE_VALUE_OFF = 'Off'
PROPERTY_BASIC_STATE_VALUE_TRIGGERED = 'Triggered'
PROPERTY_BRIGHTNESS = 'Brightness'
PROPERTY_DEMAND = 'Demand'
PROPERTY_DEMAND_VALUE_COOLING = 'Cooling'
PROPERTY_DEMAND_VALUE_HEATING = 'Heating'
PROPERTY_DEMAND_VALUE_NONE = 'None'
PROPERTY_DOORLOCK = 'DoorLock'
PROPERTY_DOORLOCK_VALUE_OPEN = 'Open'
PROPERTY_DOORLOCK_VALUE_CLOSED = 'Closed'
PROPERTY_ECOSAVE = 'EcoSave'
PROPERTY_ECOSAVE_VALUE_FALSE = 'False'
PROPERTY_ECOSAVE_VALUE_TRUE = 'True'
PROPERTY_ELECTRICAL_POWER = 'ElectricalPower'
PROPERTY_FAN_SPEED = 'FanSpeed'
PROPERTY_FAN_SPEED_VALUE_HIGH = 'High'
PROPERTY_FAN_SPEED_VALUE_LOW = 'Low'
PROPERTY_FAN_SPEED_VALUE_MEDIUM = 'Medium'
PROPERTY_HVAC_ON = 'HvacOn'
PROPERTY_HVAC_ON_VALUE_TRUE = 'True'
PROPERTY_OPERATION_MODE = 'OperationMode'
PROPERTY_OPERATION_MODE_VALUE_COOLING = 'Cooling'
PROPERTY_OPERATION_MODE_VALUE_HEATING = 'Heating'
PROPERTY_OVERRULE_ACTIVE = 'OverruleActive'
PROPERTY_OVERRULE_ACTIVE_VALUE_FALSE = 'False'
PROPERTY_OVERRULE_ACTIVE_VALUE_TRUE = 'True'
PROPERTY_OVERRULE_SETPOINT = 'OverruleSetpoint'
PROPERTY_OVERRULE_TIME = 'OverruleTime'
PROPERTY_PROGRAM = 'Program'
PROPERTY_PROGRAM_VALUE_CUSTOM = 'Custom'
PROPERTY_PROGRAM_VALUE_DAY = 'Day'
PROPERTY_PROGRAM_VALUE_ECO = 'Eco'
PROPERTY_PROGRAM_VALUE_NIGHT = 'Night'
PROPERTY_PROGRAM_VALUE_OFF = 'Off'
PROPERTY_PROGRAM_VALUE_PROG_1 = 'Prog1'
PROPERTY_PROGRAM_VALUE_PROG_2 = 'Prog2'
PROPERTY_PROGRAM_VALUE_PROG_3 = 'Prog3'
PROPERTY_PROTECT_MODE = 'ProtectMode'
PROPERTY_PROTECT_MODE_VALUE_TRUE = 'True'
PROPERTY_REPORT_INSTANT_USAGE = 'ReportInstantUsage'
PROPERTY_REPORT_INSTANT_USAGE_VALUE_TRUE = 'True'
PROPERTY_REPORT_INSTANT_USAGE_VALUE_FALSE = 'False'
PROPERTY_SETPOINT_TEMPERATURE = 'SetpointTemperature'
PROPERTY_STATUS = 'Status'
PROPERTY_STATUS_VALUE_ON = 'On'
PROPERTY_STATUS_VALUE_OFF = 'Off'
PROPERTY_THERMOSTAT_ON = 'ThermostatOn'
PROPERTY_THERMOSTAT_ON_VALUE_TRUE = 'True'
