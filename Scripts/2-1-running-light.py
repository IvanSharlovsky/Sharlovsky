import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

for circle in range(3):
    for diod in range(8):
        GPIO.output(leds[diod], 1)
        time.sleep(0.2)
        GPIO.output(leds[diod], 0)
    time.sleep(1)

GPIO.output(leds, 0)

GPIO.cleanup()