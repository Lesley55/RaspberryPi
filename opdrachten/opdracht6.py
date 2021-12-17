import RPi.GPIO as GPIO
from RpiMotorLib import rpiservolib

# definieer pinnen
SERVO_PIN = 10
KNOP_PIN1 = 5
KNOP_PIN2 = 6

GPIO.setmode(GPIO.BCM)
# zet pinnen als output
GPIO.setup(KNOP_PIN1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KNOP_PIN2, GPIO.IN, GPIO.PUD_DOWN)

# creeer servo, naam, hz, laag en hoog
servo = rpiservolib.SG90servo("servoone", 50, 2, 12)

try:
    while True:
        if GPIO.input(KNOP_PIN1) == GPIO.HIGH:
            # van 0 naar 120 graden met stappen van 1 graden en 0.005 sec tussend de stappen
            servo.servo_move_step(SERVO_PIN, 0, 120, 0.005, 1, 0.01)
            # van 120 naar 0 graden
            servo.servo_move_step(SERVO_PIN, 120, 0, 0.005, 1, 0.01)
        elif GPIO.input(KNOP_PIN2) == GPIO.HIGH:
            # van 0 naar 120 graden
            servo.servo_move_step(SERVO_PIN, 0, 120, 0.01, 1, 0.01)
            # van 0 naar 120 graden
            servo.servo_move_step(SERVO_PIN, 120, 0, 0.01, 1, 0.01)
        else:
            # stop de servo
            servo.servo_stop()
finally:
    # geef de pinnen weer vrij
    GPIO.cleanup()
