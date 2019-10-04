import time

from stair_lightning.rpi import OutputGPIO, InputGPIO


class UltrasoundDistanceReader:
    def __init__(self, trigger_gpio:int, echo_gpio:int):
        self.trigger = OutputGPIO(trigger_gpio)
        self.echo = InputGPIO(echo_gpio)
    
    def distance(self):
        # set Trigger High
        self.trigger.on()
        
        # set Trigger after 0.1ms low
        time.sleep(0.00001)
        self.trigger.off()
    
        start_time = time.time()
        end_time = time.time()
    
        # store start time
        while self.echo.read() == 0:
            start_time = time.time()
    
        # store arrival
        while self.echo.read() == 1:
            end_time = time.time()
    
        # elapsed time
        time_elapsed = end_time - start_time
        # multiply with speed of sound (34300 cm/s)
        # and division by two
        distance = (time_elapsed * 34300) / 2
    
        return distance
