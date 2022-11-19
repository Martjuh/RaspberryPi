try:
    import RPi.GPIO as GPIO
    test_environment = False
except (ImportError, RuntimeError):
    from RPiSim import GPIO
    test_environment = True
import time


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
# loop through 50 times, on/off for 1 second
for i in range(50):
    GPIO.output(7,True)
    time.sleep(1)
    GPIO.output(7,False)
    time.sleep(1)
GPIO.cleanup()

print(test_environment)