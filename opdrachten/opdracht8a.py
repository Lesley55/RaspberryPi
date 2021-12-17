import RPi.GPIO as GPIO
import time

# definieer pinnen
gpioPins = [26, 19]

GPIO.setmode(GPIO.BCM)
# zet pinnen als output
for i in gpioPins:
    GPIO.setup(i, GPIO.OUT)

while True:
    # verstreken tijd in milliseconden
    milliseconds = int(round(time.time() * 1000))

    if milliseconds % 2000 == 0:
        GPIO.output(gpioPins[0], GPIO.HIGH)
        GPIO.output(gpioPins[1], GPIO.LOW) # tweede led tegenovergesteld
    # uit na zoveel miliseconden voorbij totale knippertijd
    elif milliseconds % 2000 == 1000:
        GPIO.output(gpioPins[0], GPIO.LOW)
        GPIO.output(gpioPins[1], GPIO.HIGH) # tweede led tegenovergesteld
