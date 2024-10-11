"""Config flow for Volkswagen We Connect ID integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from weconnect.errors import AuthentificationError

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError

from . import get_we_connect_api, update
from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL_SECONDS, MINIMUM_UPDATE_INTERVAL_SECONDS

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("username"): str,
        vol.Required("password"): str,
        vol.Optional(
            "update_interval", default=DEFAULT_UPDATE_INTERVAL_SECONDS
        ): vol.All(vol.Coerce(int), vol.Range(min=MINIMUM_UPDATE_INTERVAL_SECONDS)),
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect."""

    we_connect = get_we_connect_api(
        username=data["username"],
        password=data["password"],
    )

    await hass.async_add_executor_job(we_connect.login)
    await hass.async_add_executor_job(update, we_connect)

    # vin = next(iter(we_connect.vehicles.items()))[0]

    return {"title": "Volkswagen We Connect ID"}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Volkswagen We Connect ID."""

    VERSION = 1
    MINOR_VERSION = 2

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(
                step_id="user", data_schema=STEP_USER_DATA_SCHEMA
            )

        errors = {}

        try:
            info = await validate_input(self.hass, user_input)
        except CannotConnect:
            errors["base"] = "cannot_connect"
        except AuthentificationError:
            errors["base"] = "invalid_auth"
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Unexpected exception")
            errors["base"] = "unknown"
        else:
            return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""
