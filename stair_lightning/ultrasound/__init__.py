import RPi.GPIO as GPIO
import time


class UltrasoundDistanceReader:
    def __init__(self, trigger_gpio, echo_gpio):
        self.trigger_gpio = trigger_gpio
        self.echo_gpio = echo_gpio
        GPIO.setup(trigger_gpio, GPIO.OUT)
        GPIO.setup(echo_gpio, GPIO.IN)
    
    def distance():
        # set Trigger High
        GPIO.output(self.trigger_gpio, True)
        
        # set Trigger after 0.1ms low
        time.sleep(0.00001)
        GPIO.output(self.trigger_gpio, False)
    
        start_time = time.time()
        end_time = time.time()
    
        # store start time
        while GPIO.input(self.echo_gpio) == 0:
            start_time = time.time()
    
        # store arrival
        while GPIO.input(self.echo_gpio) == 1:
            end_time = time.time()
    
        # elapsed time
        time_elapsed = end_time - start_time
        # multiply with speed of sound (34300 cm/s)
        # and division by two
        distance = (time_elapsed * 34300) / 2
    
        return distance
