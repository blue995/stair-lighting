import RPi.GPIO as GPIO
import time
import logging
from stair_lighting.logging import setup_logging
from stair_lighting.logging import logging_sample
from stair_lighting.sensors import UltrasoundDistanceReader
from stair_lighting.rpi import OutputGPIO
from stair_lighting.config import StairConfig

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    logger = logging.getLogger(__name__)
    setup_logging()

    config = StairConfig('/data/stair_settings.json')
    stairs = config.settings.stairs
    stair_lights = []
    for stair in stairs:
        gpio = stair.gpio
        number = stair.number
        stair_light = OutputGPIO(gpio=gpio, logic=False, initial=True)
        stair_lights.append(stair_light)

        print("Current: ", gpio, "Stair: ", number)
        time.sleep(1)
        stair_light.on()
        print(gpio, "on")
        time.sleep(2)
        print(gpio, "off")
        stair_light.off()
        
    first_ultrasound_sensor = UltrasoundDistanceReader(trigger_gpio=8, echo_gpio=7)
    second_ultrasound_sensor = UltrasoundDistanceReader(trigger_gpio=14, echo_gpio=15)

    try:
        while True:
            dist = first_ultrasound_sensor.distance()
            logger.info ("Distance = %.1f cm" % dist)
            time.sleep(0.5)
    except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
        GPIO.cleanup()                 # resets all GPIO ports used by this program 
