import RPi.GPIO as GPIO

# definieer pinnen
ARD26 = 26
ARD19 = 19
ARD13 = 13
LED_PIN1 = 11
LED_PIN2 = 9
BUTTON_PIN = 10

# pinmode
GPIO.setmode(GPIO.BCM)
# zet knop als input en de rest als output
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(ARD26, GPIO.OUT)
GPIO.setup(ARD19, GPIO.OUT)
GPIO.setup(ARD13, GPIO.OUT)

while True:
    # als arduino pin aan is, ook pin aanzetten
    if GPIO.input(ARD26) == GPIO.HIGH:
        GPIO.output(LED_PIN1, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN1, GPIO.LOW)
    if GPIO.input(ARD19) == GPIO.HIGH:
        GPIO.output(LED_PIN2, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN2, GPIO.LOW)
    # doorsturen van button status naar arduino
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(ARD13, GPIO.HIGH)
    else:
        GPIO.output(ARD13, GPIO.LOW)
