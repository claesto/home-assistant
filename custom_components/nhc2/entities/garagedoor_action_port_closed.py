from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass

from ..const import DOMAIN, BRAND

from ..nhccoco.devices.garagedoor_action import CocoGaragedoorAction


class Nhc2GaragedoorActionPortClosedEntity(BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoGaragedoorAction, hub, gateway):
        """Initialize a binary sensor."""
        self._device = device_instance
        self._hub = hub
        self._gateway = gateway

        self._device.after_change_callbacks.append(self.on_change)

        self._attr_available = self._device.is_online
        self._attr_unique_id = device_instance.uuid + '_port_closed'
        self._attr_should_poll = False

        self._attr_state = self._device.is_port_open
        self._attr_state_class = None
        self._attr_device_class = BinarySensorDeviceClass.GARAGE_DOOR

    @property
    def name(self) -> str:
        return 'Port Closed'

    @property
    def device_info(self):
        """Return the device info."""
        return {
            'identifiers': {
                (DOMAIN, self._device.uuid)
            },
            'name': self._device.name,
            'manufacturer': BRAND,
            'model': str.title(f'{self._device.model} ({self._device.type})'),
            'via_device': self._hub
        }

    @property
    def is_on(self) -> bool:
        return self._device.is_port_open

    def on_change(self):
        self.schedule_update_ha_state()
