from ..const import PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES, \
    PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES_VALUE_TRUE, PROPERTY_BASIC_STATE, PROPERTY_BASIC_STATE_VALUE_ON, \
    PROPERTY_BASIC_STATE_VALUE_TRIGGERED, PROPERTY_DOORLOCK, PROPERTY_DOORLOCK_VALUE_OPEN, \
    PROPERTY_DOORLOCK_VALUE_CLOSED, PROPERTY_CALL_PENDING, PROPERTY_CALL_PENDING_VALUE_TRUE, PROPERTY_CALL_ANSWERED, \
    PROPERTY_CALL_ANSWERED_VALUE_TRUE

from .device import CoCoDevice


class CocoAccesscontrolAction(CoCoDevice):
    @property
    def supports_basicstate(self) -> bool:
        return self.has_property(PROPERTY_BASIC_STATE)

    @property
    def basic_state(self) -> str:
        return self.extract_property_value(PROPERTY_BASIC_STATE)

    @property
    def possible_basic_states(self) -> list:
        return self.extract_property_definition_description_choices(PROPERTY_BASIC_STATE)

    @property
    def is_basic_state_on(self) -> bool:
        return self.basic_state == PROPERTY_BASIC_STATE_VALUE_ON

    @property
    def supports_doorlock(self) -> bool:
        return self.has_property(PROPERTY_DOORLOCK)

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
    def supports_call_pending(self) -> bool:
        return self.has_property(PROPERTY_CALL_PENDING)

    @property
    def call_pending(self) -> str:
        return self.extract_property_value(PROPERTY_CALL_PENDING)

    @property
    def is_call_pending(self) -> bool:
        return self.call_pending == PROPERTY_CALL_PENDING_VALUE_TRUE

    @property
    def supports_call_answered(self) -> bool:
        return self.has_property(PROPERTY_CALL_ANSWERED)

    @property
    def call_answered(self) -> str:
        return self.extract_property_value(PROPERTY_CALL_ANSWERED)

    @property
    def is_call_answered(self) -> bool:
        return self.call_answered == PROPERTY_CALL_ANSWERED_VALUE_TRUE

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
