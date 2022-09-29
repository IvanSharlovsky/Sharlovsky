import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        inp = input()
        number_bits = [int(bit_str) for bit_str in inp]
        GPIO.output(dac, number_bits)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()