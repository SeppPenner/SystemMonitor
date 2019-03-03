import psutil

class CpuPsutilMapper:
	def __init__(self):
		pass

	def readCpuData(self):
		"Reads all the CPU times data from psutil"
		return psutil.cpu_times()

	def readCpuPercentageTotal(self):
		"Reads all the CPU percentage in total from psutil"
		return psutil.cpu_percent(interval=1, percpu=False)

	def readCpuPercentagePerProcessor(self):
		"Reads all the CPU percentage per processor from psutil"
		return psutil.cpu_percent(interval=1, percpu=True)

	def readCpuCountLogical(self):
		"Reads the logical CPU count from psutil"
		return psutil.cpu_count(logical=True)

	def readCpuCount(self):
		"Reads the real CPU count from psutil"
		return psutil.cpu_count(logical=False)

	def readCpuStats(self):
		"Reads the CPU statistics from psutil"
		return psutil.cpu_stats()

	def readCpuFreqTotal(self):
		"Reads the total CPU frequency from psutil"
		return psutil.cpu_freq(percpu=False)