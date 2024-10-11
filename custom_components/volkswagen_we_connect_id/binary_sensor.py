"""Binary_sensor integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from weconnect import weconnect
from weconnect.elements.plug_status import PlugStatus
from weconnect.elements.lights_status import LightsStatus
from weconnect.elements.window_heating_status import WindowHeatingStatus

from homeassistant.config_entries import ConfigEntry
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from . import DomainEntry, VolkswagenIDBaseEntity
from .const import DOMAIN


@dataclass
class VolkswagenIdBinaryEntityDescription(BinarySensorEntityDescription):
    """Describes Volkswagen ID binary sensor entity."""

    value: Callable = lambda x, y: x
    on_value: object | None = None
    enabled: Callable = lambda x, y: x


SENSORS: tuple[VolkswagenIdBinaryEntityDescription, ...] = (
    VolkswagenIdBinaryEntityDescription(
        key="climatisationWithoutExternalPower",
        name="Climatisation Without External Power",
        icon="mdi:fan",
        value=lambda data: data["climatisation"][
            "climatisationSettings"
        ].climatisationWithoutExternalPower,
    ),
    VolkswagenIdBinaryEntityDescription(
        key="climatizationAtUnlock",
        name="Climatisation At Unlock",
        icon="mdi:fan",
        value=lambda data: data["climatisation"][
            "climatisationSettings"
        ].climatizationAtUnlock,
    ),
    VolkswagenIdBinaryEntityDescription(
        key="zoneFrontLeftEnabled",
        name="Zone Front Left Enabled",
        icon="mdi:car-seat",
        value=lambda data: data["climatisation"][
            "climatisationSettings"
        ].zoneFrontLeftEnabled,
    ),
    VolkswagenIdBinaryEntityDescription(
        key="zoneFrontRightEnabled",
        name="Zone Front Right Enabled",
        icon="mdi:car-seat",
        value=lambda data: data["climatisation"][
            "climatisationSettings"
        ].zoneFrontRightEnabled,
    ),
    VolkswagenIdBinaryEntityDescription(
        key="windowHeatingEnabled",
        name="Window Heating Enabled",
        icon="mdi:car-defrost-front",
        value=lambda data: data["climatisation"][
            "climatisationSettings"
        ].windowHeatingEnabled,
    ),
    VolkswagenIdBinaryEntityDescription(
        key="frontWindowHeatingState",
        name="Front Window Heating State",
        icon="mdi:car-defrost-front",
        value=lambda data: data["climatisation"]["windowHeatingStatus"]
        .windows["front"]
        .windowHeatingState,
        on_value=WindowHeatingStatus.Window.WindowHeatingState.ON,
    ),
    VolkswagenIdBinaryEntityDescription(
        key="rearWindowHeatingState",
        name="Rear Window Heating State",
        icon="mdi:car-defrost-rear",
        value=lambda data: data["climatisation"]["windowHeatingStatus"]
        .windows["rear"]
        .windowHeatingState,
        on_value=WindowHeatingStatus.Window.WindowHeatingState.ON,
    ),
    VolkswagenIdBinaryEntityDescription(
        key="insufficientBatteryLevelWarning",
        name="Insufficient Battery Level Warning",
        icon="mdi:battery-alert-variant-outline",
        value=lambda data: data["readiness"][
            "readinessStatus"
        ].connectionWarning.insufficientBatteryLevelWarning,
    ),
    VolkswagenIdBinaryEntityDescription(
        name="Car Is Online",
        key="isOnline",
        value=lambda data: data["readiness"][
            "readinessStatus"
        ].connectionState.isOnline,
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
    VolkswagenIdBinaryEntityDescription(
        name="Car Is Active",
        key="isActive",
        icon="mdi:car-side",
        value=lambda data: data["readiness"][
            "readinessStatus"
        ].connectionState.isActive,
    ),
    VolkswagenIdBinaryEntityDescription(
        name="Lights Right",
        key="lightsRight",
        icon="mdi:car-light-dimmed",
        value=lambda data: data["vehicleLights"]["lightsStatus"].lights["right"].status,
        on_value=LightsStatus.Light.LightState.ON,
    ),
    VolkswagenIdBinaryEntityDescription(
        name="Lights Left",
        key="lightsLeft",
        icon="mdi:car-light-dimmed",
        value=lambda data: data["vehicleLights"]["lightsStatus"].lights["left"].status,
        on_value=LightsStatus.Light.LightState.ON,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Add sensors for passed config_entry in HA."""
    domain_entry: DomainEntry = hass.data[DOMAIN][config_entry.entry_id]
    we_connect = domain_entry.we_connect
    coordinator = domain_entry.coordinator

    # Fetch initial data so we have data when entities subscribe
    await coordinator.async_config_entry_first_refresh()

    entities: list[VolkswagenIDSensor] = []

    for index, vehicle in enumerate(coordinator.data):
        for sensor in SENSORS:
            entities.append(VolkswagenIDSensor(sensor, we_connect, coordinator, index))
    if entities:
        async_add_entities(entities)


class VolkswagenIDSensor(VolkswagenIDBaseEntity, BinarySensorEntity):
    """Representation of a VolkswagenID vehicle sensor."""

    entity_description: VolkswagenIdBinaryEntityDescription

    def __init__(
        self,
        sensor: VolkswagenIdBinaryEntityDescription,
        we_connect: weconnect.WeConnect,
        coordinator: DataUpdateCoordinator,
        index: int,
    ) -> None:
        """Initialize VolkswagenID vehicle sensor."""
        super().__init__(we_connect, coordinator, index)

        self.entity_description = sensor
        self._coordinator = coordinator
        self._attr_name = f"{self.data.nickname} {sensor.name}"
        self._attr_unique_id = f"{self.data.vin}-{sensor.key}"

    @property
    def is_on(self) -> bool:
        """Return true if sensor is on."""
        try:
            state = self.entity_description.value(self.data.domains)
            if state.enabled and isinstance(state.value, bool):
                return state.value

            return False

        except KeyError:
            return None
