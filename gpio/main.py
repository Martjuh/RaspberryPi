try:
    import RPi.GPIO as GPIO
    test_environment = False
except (ImportError, RuntimeError):
    from RPiSim import GPIO
    test_environment = True
import time


try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    # loop through 50 times, on/off for 1 second
    for i in range(50):
        GPIO.output(7,True)
        time.sleep(1)
        GPIO.output(7,False)
        time.sleep(1)
    GPIO.cleanup()
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("some error")
finally:
   print("clean up")
   GPIO.cleanup()
