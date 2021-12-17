import RPi.GPIO as GPIO
import time

# definieer pinnen
LED_PIN1 = 16
LED_PIN2 = 11
KNOP_PIN = 10

GPIO.setmode(GPIO.BCM)
# zet pinnen als output
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(KNOP_PIN, GPIO.IN, GPIO.PUD_DOWN)

while True:
    # kijk of de knop word ingedrukt
    buttonState = GPIO.input(KNOP_PIN)

    # als op knop gedrukt word
    if buttonState == GPIO.HIGH:
        # verstreken tijd in milliseconden
        milliseconds = int(round(time.time() * 1000))

        # aan bij totaal knipper tijd
        if milliseconds % 2000 == 0:
            GPIO.output(LED_PIN1, GPIO.HIGH)
        # uit na zoveel miliseconden voorbij totale knippertijd
        elif milliseconds % 2000 == 1300:
            GPIO.output(LED_PIN1, GPIO.LOW)

        # tweede led uit
        GPIO.output(LED_PIN2, GPIO.LOW)
    else:
        # als niet op knop gedrukt word, tweede led aan
        GPIO.output(LED_PIN2, GPIO.HIGH)