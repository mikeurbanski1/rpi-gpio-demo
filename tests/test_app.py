from gpiozero import Button, LED


def test_button_toggles_led():
    button = Button(18)
    led = LED(17)

    button.when_pressed = led.toggle

    assert not led.is_active

    # Press
    button.pin.drive_low()
    assert led.is_active

    # Release
    button.pin.drive_high()

    # Press again
    button.pin.drive_low()
    assert not led.is_active

    # Release
    button.pin.drive_high()
