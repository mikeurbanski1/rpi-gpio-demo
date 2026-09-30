from gpiozero import Button, LED

BUTTON_PIN = 18
LED_PIN = 17


def create_hardware() -> tuple[Button, LED]:
    button = Button(BUTTON_PIN)
    led = LED(LED_PIN)

    return button, led
