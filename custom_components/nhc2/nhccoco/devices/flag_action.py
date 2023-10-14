from ..const import DEVICE_DESCRIPTOR_PROPERTIES, PROPERTY_STATUS, PROPERTY_STATUS_VALUE_TRUE, PROPERTY_STATUS_VALUE_FALSE
from .device import CoCoDevice

import logging

_LOGGER = logging.getLogger(__name__)


class CocoFlagAction(CoCoDevice):
    @property
    def status(self) -> str:
        return self.extract_property_value(PROPERTY_STATUS)

    @property
    def is_status_on(self) -> bool:
        return self.status == PROPERTY_STATUS_VALUE_TRUE

    def on_change(self, topic: str, payload: dict):
        _LOGGER.debug(f'{self.name} changed. Topic: {topic} | Data: {payload}')
        if DEVICE_DESCRIPTOR_PROPERTIES in payload:
            self.merge_properties(payload[DEVICE_DESCRIPTOR_PROPERTIES])

        if self._after_change_callbacks:
            for callback in self._after_change_callbacks:
                callback()

    def turn_on(self, gateway):
        gateway.add_device_control(self.uuid, PROPERTY_STATUS, PROPERTY_STATUS_VALUE_TRUE)

    def turn_off(self, gateway):
        gateway.add_device_control(self.uuid, PROPERTY_STATUS, PROPERTY_STATUS_VALUE_FALSE)
