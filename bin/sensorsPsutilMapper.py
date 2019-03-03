import psutil

class SensorsPsutilMapper:
	def __init__(self):
		pass

	def readSensorTemperatures(self):
		"Reads all sensor temperatures in degrees Celcius from psutil"
		return psutil.sensors_temperatures(fahrenheit = False)