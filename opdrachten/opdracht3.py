import RPi.GPIO as GPIO
import time

# definieer pinnen
LED_PIN1 = 16
LED_PIN2 = 11

GPIO.setmode(GPIO.BCM)
# zet pinnen als output
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

while True:
    # verstreken tijd in milliseconden
    milliseconds = int(round(time.time() * 1000))
    # aan bij totaal knipper tijd
    if milliseconds % 2000 == 0:
        GPIO.output(LED_PIN1, GPIO.HIGH)
    if milliseconds % 2500 == 0:
        GPIO.output(LED_PIN2, GPIO.HIGH)
    # uit na zoveel miliseconden voorbij totale knippertijd
    if milliseconds % 2000 == 1300:
        GPIO.output(LED_PIN1, GPIO.LOW)
    if milliseconds % 2500 == 800:
        GPIO.output(LED_PIN2, GPIO.LOW)
