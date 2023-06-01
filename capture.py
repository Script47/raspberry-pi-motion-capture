from picamera2 import Picamera2
from datetime import datetime
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PIR_PIN = 17

GPIO.setup(PIR_PIN, GPIO.IN)

camera = Picamera2()
camera.start()

print("Loading...")

while True:
	if GPIO.input(PIR_PIN):
		print("Motion Detected")
		timestamp = time.strftime("%Y-%m-%d-%H:%M:%S")
		imageName = timestamp + "-motion-detection.jpg"
		
		time.sleep(2)
		camera.capture_file("captures/" + imageName)
	else:
		print("No motion detected")
	
	time.sleep(1)
