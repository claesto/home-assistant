from ..const import PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES, \
    PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES_VALUE_TRUE, PROPERTY_BASIC_STATE, PROPERTY_BASIC_STATE_VALUE_ON, \
    PROPERTY_BASIC_STATE_VALUE_TRIGGERED, PROPERTY_DOORLOCK, PROPERTY_DOORLOCK_VALUE_OPEN, \
    PROPERTY_DOORLOCK_VALUE_CLOSED
from .device import CoCoDevice


class CocoBellbuttonAction(CoCoDevice):
    @property
    def basic_state(self) -> str:
        return self.extract_property_value(PROPERTY_BASIC_STATE)

    @property
    def is_basic_state_on(self) -> bool:
        return self.basic_state == PROPERTY_BASIC_STATE_VALUE_ON

    @property
    def possible_basic_states(self) -> list:
        return self.extract_property_definition_description_choices(PROPERTY_BASIC_STATE)

    @property
    def doorlock(self) -> str:
        return self.extract_property_value(PROPERTY_DOORLOCK)

    @property
    def is_doorlock_open(self) -> bool:
        return self.doorlock == PROPERTY_DOORLOCK_VALUE_OPEN

    @property
    def is_doorlock_closed(self) -> bool:
        return self.doorlock == PROPERTY_DOORLOCK_VALUE_CLOSED

    @property
    def decline_call_applied_on_all_devices(self) -> str:
        return self.extract_parameter_value(PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES)

    @property
    def is_decline_call_applied_on_all_devices(self) -> bool:
        return self.decline_call_applied_on_all_devices == PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES_VALUE_TRUE

    def press(self, gateway):
        gateway.add_device_control(self.uuid, PROPERTY_BASIC_STATE, PROPERTY_BASIC_STATE_VALUE_TRIGGERED)

    def open_doorlock(self, gateway):
        gateway.add_device_control(self.uuid, PROPERTY_DOORLOCK, PROPERTY_DOORLOCK_VALUE_OPEN)
