import os
import time

# import RPi.GPIO as GPIO
# from picamera2 import Picamera2

import helpers
import env

env.load_dotenv()

print(os.getenv("CAPTURE_TYPE"))

CWD = os.path.dirname(os.path.abspath(__file__))
CAPTURES_DIRECTORY = CWD + "/captures"
PIR_PIN = 17

helpers.create_captures_dir(CAPTURES_DIRECTORY)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(PIR_PIN, GPIO.IN)
# camera = Picamera2()
# camera.start()

try:
    while True:
        # if GPIO.input(PIR_PIN):
        #     helpers.print_with_date("Motion detected...")
        #     time.sleep(2)
        #     camera.capture_file("captures/" + helpers.build_capture_output_name())

        time.sleep(1)
except KeyboardInterrupt:
    helpers.print_with_date("exiting...")
    # GPIO.cleanup()
