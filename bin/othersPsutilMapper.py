import psutil

class OthersPsutilMapper:
	def __init__(self):
		pass

	def readBootTime(self):
		"Reads the system boot time from psutil"
		return psutil.boot_time()