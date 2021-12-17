import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# definieer pinnen
gpioPins = [5,6,13,19]
KNOP_PIN1 = 10
KNOP_PIN2 = 9

GPIO.setmode(GPIO.BCM)
# zet pinnen als output
GPIO.setup(KNOP_PIN1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KNOP_PIN2, GPIO.IN, GPIO.PUD_DOWN)

motor = RpiMotorLib.BYJMotor("Vroooommm", "28BYJ")

try:
    while True:
        if GPIO.input(KNOP_PIN1) == GPIO.HIGH:
            # 5 sec linksom
            motor.motor_run(gpioPins, .0023, 512, True, False, "half", 0)
        elif GPIO.input(KNOP_PIN2) == GPIO.HIGH:
            # 12 sec rechtom
            motor.motor_run(gpioPins, .0055, 512, False, False, "half", 0)
        else:
            # stop de motor
            motor.motor_stop()
finally:
    # geef de pinnen weer vrij
    GPIO.cleanup()
