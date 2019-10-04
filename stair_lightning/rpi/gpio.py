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

