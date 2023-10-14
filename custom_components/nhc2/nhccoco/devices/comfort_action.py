from ..const import DEVICE_DESCRIPTOR_PROPERTIES, PROPERTY_BASIC_STATE, PROPERTY_BASIC_STATE_VALUE_ON, \
    PROPERTY_MOOD_ACTIVE, PROPERTY_MOOD_ACTIVE_VALUE_TRUE, PROPERTY_BASIC_STATE_VALUE_TRIGGERED

from .device import CoCoDevice

import logging

_LOGGER = logging.getLogger(__name__)


class CocoComfortAction(CoCoDevice):
    @property
    def basic_state(self) -> str:
        return self.extract_property_value(PROPERTY_BASIC_STATE)

    @property
    def is_basic_state_on(self) -> bool:
        return self.basic_state == PROPERTY_BASIC_STATE_VALUE_ON

    @property
    def mood_active(self) -> bool:
        return self.extract_property_value(PROPERTY_MOOD_ACTIVE)

    @property
    def is_mood_active(self) -> bool:
        return self.mood_active == PROPERTY_MOOD_ACTIVE_VALUE_TRUE

    def on_change(self, topic: str, payload: dict):
        _LOGGER.debug(f'{self.name} changed. Topic: {topic} | Data: {payload}')
        if DEVICE_DESCRIPTOR_PROPERTIES in payload:
            self.merge_properties(payload[DEVICE_DESCRIPTOR_PROPERTIES])

        if self._after_change_callbacks:
            for callback in self._after_change_callbacks:
                callback()

    def press(self, gateway):
        gateway.add_device_control(
            self.uuid,
            PROPERTY_BASIC_STATE,
            PROPERTY_BASIC_STATE_VALUE_TRIGGERED
        )
