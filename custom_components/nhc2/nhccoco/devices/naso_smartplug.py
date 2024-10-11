from ..const import PROPERTY_ELECTRICAL_POWER, PROPERTY_REPORT_INSTANT_USAGE, PROPERTY_REPORT_INSTANT_USAGE_VALUE_TRUE, \
    PROPERTY_STATUS, PROPERTY_STATUS_VALUE_ON, PROPERTY_STATUS_VALUE_OFF, PARAMETER_FEEDBACK_ENABLED, \
    PARAMETER_FEEDBACK_ENABLED_VALUE_TRUE, PARAMETER_MEASURING_ONLY, PARAMETER_MEASURING_ONLY_VALUE_TRUE, \
    PARAMETER_SWITCHING_ONLY, PARAMETER_SWITCHING_ONLY_VALUE_TRUE
from ..helpers import to_float_or_none
from .device import CoCoDevice


class CocoNasoSmartplug(CoCoDevice):
    @property
    def electrical_power(self) -> float:
        return to_float_or_none(self.extract_property_value(PROPERTY_ELECTRICAL_POWER))

    @property
    def is_report_instant_usage(self) -> bool:
        return self.extract_property_value(PROPERTY_REPORT_INSTANT_USAGE) == PROPERTY_REPORT_INSTANT_USAGE_VALUE_TRUE

    @property
    def status(self) -> str:
        return self.extract_property_value(PROPERTY_STATUS)

    @property
    def is_status_on(self) -> bool:
        return self.status == PROPERTY_STATUS_VALUE_ON

    @property
    def supports_status(self) -> bool:
        return self.has_property(PROPERTY_STATUS)

    @property
    def is_feedback_enabled(self) -> bool:
        return self.extract_parameter_value(PARAMETER_FEEDBACK_ENABLED) == PARAMETER_FEEDBACK_ENABLED_VALUE_TRUE

    @property
    def is_measuring_only(self) -> bool:
        return self.extract_parameter_value(PARAMETER_MEASURING_ONLY) == PARAMETER_MEASURING_ONLY_VALUE_TRUE

    @property
    def is_switching_only(self) -> bool:
        return self.extract_parameter_value(PARAMETER_SWITCHING_ONLY) == PARAMETER_SWITCHING_ONLY_VALUE_TRUE

    def enable_report_instant_usage(self, gateway):
        gateway.add_device_control(self.uuid, PROPERTY_REPORT_INSTANT_USAGE, PROPERTY_REPORT_INSTANT_USAGE_VALUE_TRUE)

    def turn_on(self, gateway):
        gateway.add_device_control(self.uuid, PROPERTY_STATUS, PROPERTY_STATUS_VALUE_ON)

    def turn_off(self, gateway):
        gateway.add_device_control(self.uuid, PROPERTY_STATUS, PROPERTY_STATUS_VALUE_OFF)
