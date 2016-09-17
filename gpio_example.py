#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import pyowm

owm = pyowm.OWM(##_OMW_CODE_##)

# Localisation: Sadowa
LAT = 52.35 # lattitude
LON = 20.82 # londitude
NUMBER_OF_DAYS = 1


# Set raspberry pi GPIO mode: GPIO.BCM or GPIO.BOARD
GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT) # use only gpio input/output number 8

GPIO.output(8, False) # turn off i/o 8
time.sleep(60 * 60 * 2) # wait two hours

while True:
	# Get forecast for a given localisation
	forecast = owm.daily_forecast_at_coords(LAT, LON, NUMBER_OF_DAYS)
	f = forecast.get_forecast()
	for weather in f:
		rain_forecast = str(weather.get_status())

	if rain_forecast != "rain":
		print("rain is not forecast")
		GPIO.output(8, True) # turn on the pump
		time.sleep(60 * 2) # wait two minutes
		GPIO.output(8, False) # turn off the pump
		time.sleep(60 * 60 * 24 - 60 * 2) # wait one day
	else:
		print("rain is forecast")
		GPIO.output(8, False) # turn off the pump
		time.sleep(60 * 60 * 24) # wait one day





# Reset all gpio pin
GPIO.cleanup()
