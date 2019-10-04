import RPi.GPIO as GPIO
import time
import logging
from stair_lightning.logging import setup_logging
from stair_lightning.logging import logging_sample
from stair_lightning.sensors import UltrasoundDistanceReader
from stair_lightning.rpi import OutputGPIO

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    logger = logging.getLogger(__name__)

    setup_logging()
    logging_sample()
    gpio_list = [17, 27, 22, 5, 6, 13, 19, 26, 18, 23, 24, 25, 12, 16, 20, 23]
    for gpio in gpio_list:
        g = OutputGPIO(gpio=gpio, logic=False)
        print("Current: ", gpio)
        time.sleep(1)
        g.on()
        print(gpio, "on")
        time.sleep(2)
        print(gpio, "off")
        g.off()
        
    first_ultrasound_sensor = UltrasoundDistanceReader(trigger_gpio=8, echo_gpio=7)
    second_ultrasound_sensor = UltrasoundDistanceReader(trigger_gpio=14, echo_gpio=15)

    try:
        while True:
            dist = first_ultrasound_sensor.distance()
            logger.info ("Entfernung = %.1f cm" % dist)
            time.sleep(0.5)
    except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
        GPIO.cleanup()                 # resets all GPIO ports used by this program 
