import RPi.GPIO as GPIO
import time

# definieer pinnen
LED_PIN1 = 16
LED_PIN2 = 11
KNOP_PIN1 = 10
KNOP_PIN2 = 6

GPIO.setmode(GPIO.BCM)
# zet pinnen als output
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(KNOP_PIN1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KNOP_PIN2, GPIO.IN, GPIO.PUD_DOWN)

while True:
    # kijk of de knop word ingedrukt
    buttonState1 = GPIO.input(KNOP_PIN1)
    buttonState2 = GPIO.input(KNOP_PIN2) # word niet gebruikt in deze opdracht

    # verstreken tijd in milliseconden
    milliseconds = int(round(time.time() * 1000))

    # als op knop 1 gedrukt word
    if buttonState1 == GPIO.HIGH:
        # aan bij totaal knipper tijd
        if milliseconds % 2000 == 0:
            GPIO.output(LED_PIN1, GPIO.HIGH)
            GPIO.output(LED_PIN2, GPIO.LOW) # tweede led tegenovergesteld
        # uit na zoveel miliseconden voorbij totale knippertijd
        elif milliseconds % 2000 == 1000:
            GPIO.output(LED_PIN1, GPIO.LOW)
            GPIO.output(LED_PIN2, GPIO.HIGH) # tweede led tegenovergesteld
    # opdracht b als op knop 2 gedrukt word
    else:
        # aan bij totaal knipper tijd
        if milliseconds % 2000 == 0:
            GPIO.output(LED_PIN1, GPIO.HIGH)
            GPIO.output(LED_PIN2, GPIO.LOW) # tweede led tegenovergesteld
        # uit na zoveel miliseconden voorbij totale knippertijd
        elif milliseconds % 2000 == 1300:
            GPIO.output(LED_PIN1, GPIO.LOW)
            GPIO.output(LED_PIN2, GPIO.HIGH) # tweede led tegenovergesteld