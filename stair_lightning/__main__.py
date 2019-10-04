import RPi.GPIO as GPIO

from stair_lightning.logging import setup_logging
from stair_lightning.logging import logging_sample
from stair_lightning.ultrasound import UltrasoundDistanceReader

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    setup_logging()
    logging_sample()
    first_ultrasound_sensor = UltrasoundDistanceReader(trigger_gpio=8, echo_gpio=7)
    second_ultrasound_sensor = UltrasoundDistanceReader(trigger_gpio=14, echo_gpio=15)

    try:
        while True:
            dist = first_ultrasound_sensor.distance()
            print ("Entfernung = %.1f cm" % dist)
            time.sleep(0.01)
    except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
        GPIO.cleanup()                 # resets all GPIO ports used by this program 
