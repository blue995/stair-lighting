import RPi.GPIO as GPIO

class OutputGPIO:
    def __init__(self, gpio:int, logic:bool=True):
        self.logic = GPIO.HIGH if logic else GPIO.LOW
        self.gpio = gpio
        self._setup = False
    
    def setup(self):
        if (self._setup):
            return
        GPIO.setup(self.gpio, GPIO.OUT)
        self._setup = True
    
    def cleanup(self):
        GPIO.cleanup(self.gpio)
        self._setup = False

    def on(self):
        self.setup()
        GPIO.output(self.gpio, self.logic)
    
    def off(self):
        self.setup()
        GPIO.output(self.gpio, not self.logic)
        self.cleanup()

class InputGPIO:
    def __init__(self, gpio:int, pull_up_down=GPIO.PUD_UP):
        self.pull_up_down = pull_up_down
        self.gpio = gpio
        self._setup = False
    
    def setup(self):
        if (self._setup):
            return
        GPIO.setup(self.gpio, GPIO.IN, pull_up_down=self.pull_up_down)
        self._setup = True
    
    def cleanup(self):
        GPIO.cleanup(self.gpio)
        self._setup = False

    def read(self) -> int:
        self.setup()
        value = GPIO.input(self.gpio)
        self.cleanup()
        return value
