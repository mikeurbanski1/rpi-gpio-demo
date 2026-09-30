import pytest
from gpiozero import Device
from gpiozero.pins.mock import MockFactory


@pytest.fixture(autouse=True)
def mock_gpio():
    Device.pin_factory = MockFactory()
    yield
    Device.pin_factory = None
