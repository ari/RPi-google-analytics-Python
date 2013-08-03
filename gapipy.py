#!/usr/bin/env python2.7
# Based on Alex Eames' python scripts for gertboard, see http://RasPi.TV

import RPi.GPIO as GPIO
from pyus import AppTracker
GPIO.setmode(GPIO.BCM)  # Run in BCM mode

# Now set up the detection for the buttons
for i in range(23, 26):
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # sets up for switches to1 be detected on gertboard
    GPIO.add_event_detect(i, GPIO.RISING, bouncetime=200)  # Defines an event

# Print Instructions to user
print("ready for input")

# This setting isn't used
app_name = "coffeemachine"

# Insert your Tracking ID below, something like UA-XXXXXXX-Y
tracking_id = "UA-41589819-1"

tracker = AppTracker(app_name, tracking_id)

#What event are we tracking?
event_category = "coffee"

while True:
    if GPIO.event_detected(23):  # calls based on add_event_detect -- you could run a callback in add_event_detect to do more
        tracker.track_event(event_category, "make with 23", label="machine", value=5)  # category, action, label, value
    print("sent 23")
    if GPIO.event_detected(24):
        tracker.track_event(event_category, "make with 24", label="machine", value=5)  # category, action, label, value
    print("sent 24")
    if GPIO.event_detected(25):
        tracker.track_event(event_category, "make with 25", label="machine", value=5)  # category, action, label, value
    print("sent 25")
