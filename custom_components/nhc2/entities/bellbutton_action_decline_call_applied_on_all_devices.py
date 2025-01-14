from homeassistant.components.binary_sensor import BinarySensorEntity

from ..nhccoco.devices.bellbutton_action import CocoBellbuttonAction
from .nhc_entity import NHCBaseEntity


class Nhc2BellbuttonActionDeclineCallAppliedOnAllDevicesEntity(NHCBaseEntity, BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoBellbuttonAction, hub, gateway):
        """Initialize a binary sensor."""
        super().__init__(device_instance, hub, gateway)

        self._attr_unique_id = device_instance.uuid + '_decline_call_applied_on_all_devices'
        self._attr_state = self._device.is_decline_call_applied_on_all_devices

    @property
    def name(self) -> str:
        return 'Decline call applied on all devices'

    @property
    def is_on(self) -> bool:
        return self._device.is_decline_call_applied_on_all_devices
