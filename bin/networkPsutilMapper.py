import psutil

class NetworkPsutilMapper:
	def __init__(self):
		pass

	def readNetIoCountersTotal(self):
		"Reads all the network IO counters from psutil"
		return psutil.net_io_counters(pernic=False, nowrap=True)