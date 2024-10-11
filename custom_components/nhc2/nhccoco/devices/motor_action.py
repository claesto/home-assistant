from ..const import PROPERTY_ACTION, PROPERTY_ALIGNED, PROPERTY_ALIGNED_VALUE_TRUE, PROPERTY_MOVING, \
    PROPERTY_MOVING_VALUE_TRUE, PROPERTY_POSITION, PROPERTY_LAST_DIRECTION, PROPERTY_LAST_DIRECTION_VALUE_CLOSE, \
    PROPERTY_LAST_DIRECTION_VALUE_OPEN
from ..helpers import to_int_or_none
from .device import CoCoDevice


class CocoMotorAction(CoCoDevice):
    @property
    def position(self) -> int:
        return to_int_or_none(self.extract_property_value(PROPERTY_POSITION))

    @property
    def aligned(self) -> str:
        return self.extract_property_value(PROPERTY_ALIGNED)

    @property
    def is_aligned(self) -> bool:
        return self.aligned == PROPERTY_ALIGNED_VALUE_TRUE

    @property
    def moving(self) -> str:
        return self.extract_property_value(PROPERTY_MOVING)

    @property
    def is_moving(self) -> bool:
        return self.moving == PROPERTY_MOVING_VALUE_TRUE

    @property
    def last_direction(self) -> str:
        return self.extract_property_value(PROPERTY_LAST_DIRECTION)

    @property
    def possible_last_directions(self) -> list:
        return self.extract_property_definition_description_choices(PROPERTY_LAST_DIRECTION)

    @property
    def supports_last_direction(self) -> bool:
        return self.has_property(PROPERTY_LAST_DIRECTION)

    @property
    def is_opening(self) -> bool | None:
        if not self.supports_last_direction:
            return None

        # The next line may be wierd, but it is correct.
        # It seems that the last_direction property is updated directly instead of after the moving is done.
        if self.is_moving and self.last_direction == PROPERTY_LAST_DIRECTION_VALUE_OPEN:
            return True

        return False

    @property
    def is_closing(self) -> bool | None:
        if not self.supports_last_direction:
            return None

        # The next line may be wierd, but it is correct.
        # It seems that the last_direction property is updated directly instead of after the moving is done.
        if self.is_moving and self.last_direction == PROPERTY_LAST_DIRECTION_VALUE_CLOSE:
            return True

        return False

    def set_action(self, gateway, action: str):
        gateway.add_device_control(
            self.uuid,
            PROPERTY_ACTION,
            action
        )

    def set_position(self, gateway, position: int):
        gateway.add_device_control(
            self.uuid,
            PROPERTY_POSITION,
            str(position)
        )
