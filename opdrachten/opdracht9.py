import RPi.GPIO as GPIO

# definieer pinnen
ardPins = [9, 10, 22, 27]
ledPins = [26, 19, 13, 6]

# pinmode
GPIO.setmode(GPIO.BCM)
# zet arduino pinnen als input
for i in ardPins:
    GPIO.setup(i, GPIO.IN)
# zet ledjes als output
for i in ledPins:
    GPIO.setup(i, GPIO.OUT)

while True:
    # als arduino pin aan is, zet led ook aan
    for i in range(len(ardPins)):
        if GPIO.input(ardPins[i]) == GPIO.HIGH:
            GPIO.output(ledPins[i], GPIO.HIGH)
        else:
            GPIO.output(ledPins[i], GPIO.LOW)
