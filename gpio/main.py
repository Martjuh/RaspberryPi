try:
    import RPi.GPIO as GPIO
    test_environment = False
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
except ImportError:
    print("RPi.GPIO not found, import simulator")
    from RPiSim import GPIO
    test_environment = True

import time

GPIO.cleanup()
print("Starting blinker!")
print(f"Mode: {GPIO.getmode()}")

ouput_pin = 11

try:
    GPIO.setmode(GPIO.BCM)
    print(f"Mode: {GPIO.getmode()}")
    GPIO.setup(ouput_pin, GPIO.OUT, initial=GPIO.LOW)
    # loop through 50 times, on/off for 1 second
    for i in range(50):
        GPIO.output(ouput_pin, True)
        time.sleep(1)
        GPIO.output(ouput_pin, False)
        time.sleep(1)
    GPIO.cleanup()
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Keyboard interrupt")

except:
   print("some error")
finally:
   print("clean up")
   GPIO.cleanup()
