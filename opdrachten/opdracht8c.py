import RPi.GPIO as GPIO

# definieer pinnen
gpioPins = [26, 19]
KNOP_PIN = 13

GPIO.setmode(GPIO.BCM)
# zet pinnen als output
for i in gpioPins:
    GPIO.setup(i, GPIO.OUT)
GPIO.setup(KNOP_PIN, GPIO.IN)

while True:
    # als je de knop indrukt
    if GPIO.input(KNOP_PIN) == GPIO.HIGH:
        GPIO.output(gpioPins[0], GPIO.HIGH)
        GPIO.output(gpioPins[1], GPIO.LOW) # tweede led tegenovergesteld
    else:
        GPIO.output(gpioPins[0], GPIO.LOW)
        GPIO.output(gpioPins[1], GPIO.HIGH) # tweede led tegenovergesteld
