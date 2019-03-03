import psutil

class MemoryPsutilMapper:
	def __init__(self):
		pass

	def readVirtualMemoryData(self):
		"Reads all the virtual memory data from psutil"
		return psutil.virtual_memory()

	def readSwapMemoryData(self):
		"Reads the swap memory data from psutil"
		return psutil.swap_memory()