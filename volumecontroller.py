import RPi.GPIO as GPIO
import config
import alsaaudio


class VolumeController:

    def __init__(self, state="high"):
        super().__init__()
        self._set_gpio_pins()

        self._state = state

    def _set_gpio_pins(self):
        if "low" in config.GPIO_VOLUME_SWITCH:
            GPIO.setup(config.GPIO_VOLUME_SWITCH["low"], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        if "medium" in config.GPIO_VOLUME_SWITCH:
            GPIO.setup(config.GPIO_VOLUME_SWITCH["medium"], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        if "high" in config.GPIO_VOLUME_SWITCH:
            GPIO.setup(config.GPIO_VOLUME_SWITCH["high"], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def set_volume(self, value):
        mixer = alsaaudio.Mixer()
        mixer.setvolume(value)

    def get_state(self):
        return self._state

    def handle(self):
        if "low" in config.GPIO_VOLUME_SWITCH and GPIO.input(config.GPIO_VOLUME_SWITCH["low"]) == GPIO.HIGH:
            self._state = "low"
            self.set_volume(25)
        elif "medium" in config.GPIO_VOLUME_SWITCH and GPIO.input(config.GPIO_VOLUME_SWITCH["medium"]) == GPIO.HIGH:
            self._state = "medium"
            self.set_volume(60)
        elif "high" in config.GPIO_VOLUME_SWITCH and GPIO.input(config.GPIO_VOLUME_SWITCH["high"]) == GPIO.HIGH:
            self._state = "high"
            self.set_volume(100)
