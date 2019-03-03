import psutil

class DisksPsutilMapper:
	def __init__(self):
		pass

	def readDiskUsage(self):
		"Reads the disk usage from psutil"
		return psutil.disk_usage('/')

	def readDiskIoCountersTotal(self):
		"Reads the disk IO counters in total from psutil"
		return psutil.disk_io_counters(perdisk=False, nowrap=True)