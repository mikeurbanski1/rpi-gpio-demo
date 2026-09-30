from signal import pause

from .hardware import create_hardware


def run() -> None:
    button, led = create_hardware()

    button.when_pressed = led.toggle

    pause()


if __name__ == "__main__":
    run()
