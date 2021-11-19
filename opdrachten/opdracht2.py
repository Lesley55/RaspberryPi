import RPi.GPIO as GPIO
import time

# definieer pinnen
LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) # zet pin als output

while True:
    GPIO.output(LED_PIN, GPIO.HIGH) # aan
    time.sleep(0.1) # wacht 100 ms
    GPIO.output(LED_PIN, GPIO.LOW) # uit
    time.sleep(0.1) # wacht 100 ms
