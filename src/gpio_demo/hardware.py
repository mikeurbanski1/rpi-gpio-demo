from gpiozero import Button, LED

BUTTON_PIN = 23
LED_PIN = 24


def create_hardware() -> tuple[Button, LED]:
    button = Button(BUTTON_PIN)
    led = LED(LED_PIN)

    return button, led
