import pymysql.cursors
import traceback
from bin import lang, cpuPsutilMapper, memoryPsutilMapper, disksPsutilMapper, networkPsutilMapper, sensorsPsutilMapper, othersPsutilMapper, serial

# Database settings
databaseUser = 'default'
databasePassword = 'asdf'
databaseName = 'SystemMonitor'
hostAddress = '192.168.2.2'
databasePort = 3307

language = lang.Lang('german') # Valid ones are currently 'german' and 'english'
cpuPsutilHelper = cpuPsutilMapper.CpuPsutilMapper()
memoryPsutilHelper = memoryPsutilMapper.MemoryPsutilMapper()
disksPsutilHelper = disksPsutilMapper.DisksPsutilMapper()
networkPsutilHelper = networkPsutilMapper.NetworkPsutilMapper()
sensorsPsutilHelper = sensorsPsutilMapper.SensorsPsutilMapper()
othersPsutilHelper = othersPsutilMapper.OthersPsutilMapper()
serial = serial.Serial()

def writeMasterDataToDatabase(serial: str, cpuCountLogical: float, cpuCount: float):
	"Writes the serial number from the CPU to the database if it does not exist already"
	try:
		if serial == "ERROR000000000":
			return -1
		print(language.getString('DatabaseConnecting'))
		connection = pymysql.connect(host = hostAddress, user = databaseUser, password = databasePassword, database = databaseName, port = databasePort)
		print(language.getString('GettingCursor'))
		with connection.cursor() as cursor:
			print(language.getString('ExecutingQuery'))
			cursor.callproc('systemMonitorGetMasterData', [serial])
			print(language.getString('GettingResults'))
			readSerial = cursor.fetchone()
			if not readSerial:
				print(language.getString('ExecutingQuery'))
				cursor.callproc('systemMonitorInsertMasterData', [serial, cpuCountLogical, cpuCount])
				lastRowId = cursor.lastrowid
				connection.commit()
				return lastRowId + 1
			else:
				return readSerial[0]
		connection.close()
	except Exception as e:
		traceback.print_exc()

def writeDataToDatabase(serialId: int, cpuData, cpuPercentageTotal, cpuPercentagePerProcessor, cpuStats, cpuFreqTotal, virtualMemoryData, swapMemoryData,
						diskUsage, diskIoCountersTotal, netIoCountersTotal, sensorTemperatures, bootTime):
	"Writes the data read before to the database"
	try:
		cpuPercentage = []
		if (len(cpuPercentagePerProcessor) > 8):
			raise Exception(language.getString('NumberOfCPUCoresIsBiggerThan8'))
		else:
			for c in cpuPercentagePerProcessor:
				cpuPercentage.append(c)
			while len(cpuPercentage) < 8:
				cpuPercentage.append(None)
		print(language.getString('DatabaseConnecting'))
		connection = pymysql.connect(host = hostAddress, user = databaseUser, password = databasePassword, database = databaseName, port = databasePort)
		print(language.getString('GettingCursor'))
		with connection.cursor() as cursor:
			print(language.getString('ExecutingQuery'))
			cursor.callproc('systemMonitorLoadPeriodicData',
					[serialId, cpuData.user, cpuData.nice, cpuData.system, cpuData.idle, cpuData.iowait, cpuData.irq, cpuData.softirq, cpuData.steal,
					cpuData.guest, cpuData.guest_nice, cpuPercentageTotal, cpuPercentage[0], cpuPercentage[1], cpuPercentage[2], cpuPercentage[3],
					cpuPercentage[4], cpuPercentage[5], cpuPercentage[6], cpuPercentage[7], cpuStats.ctx_switches, cpuStats.interrupts,
					cpuStats.soft_interrupts, cpuStats.syscalls, cpuFreqTotal.current, cpuFreqTotal.min, cpuFreqTotal.max, virtualMemoryData.total,
					virtualMemoryData.available, virtualMemoryData.percent, virtualMemoryData.used, virtualMemoryData.free, virtualMemoryData.active,
					virtualMemoryData.inactive, virtualMemoryData.buffers, virtualMemoryData.cached, virtualMemoryData.shared, virtualMemoryData.slab,
					swapMemoryData.total, swapMemoryData.used, swapMemoryData.free, swapMemoryData.percent, swapMemoryData.sin, swapMemoryData.sout,
					diskUsage.total, diskUsage.used, diskUsage.free, diskUsage.percent, diskIoCountersTotal.read_count, diskIoCountersTotal.write_count,
					diskIoCountersTotal.read_bytes, diskIoCountersTotal.write_bytes, diskIoCountersTotal.read_time, diskIoCountersTotal.write_time,
					netIoCountersTotal.bytes_sent, netIoCountersTotal.bytes_recv, netIoCountersTotal.packets_sent, netIoCountersTotal.packets_recv,
					netIoCountersTotal.errin, netIoCountersTotal.errout, netIoCountersTotal.dropin, netIoCountersTotal.dropout, 'cpu-thermal',
					sensorTemperatures['cpu-thermal'][0].current, sensorTemperatures['cpu-thermal'][0].high, sensorTemperatures['cpu-thermal'][0].critical,
					bootTime])				
			connection.commit()
			print(language.getString('Done'))
		connection.close()
	except Exception as e:
		traceback.print_exc()

def readPeriodicData(serialId: int):
	"Read all the data to store it to the database"
	cpuData = cpuPsutilHelper.readCpuData()
	cpuPercentageTotal = cpuPsutilHelper.readCpuPercentageTotal()
	cpuPercentagePerProcessor = cpuPsutilHelper.readCpuPercentagePerProcessor()
	cpuStats = cpuPsutilHelper.readCpuStats()
	cpuFreqTotal = cpuPsutilHelper.readCpuFreqTotal()
	virtualMemoryData = memoryPsutilHelper.readVirtualMemoryData()
	swapMemoryData = memoryPsutilHelper.readSwapMemoryData()
	diskUsage = disksPsutilHelper.readDiskUsage()
	diskIoCountersTotal = disksPsutilHelper.readDiskIoCountersTotal()
	netIoCountersTotal = networkPsutilHelper.readNetIoCountersTotal()
	sensorTemperatures = sensorsPsutilHelper.readSensorTemperatures()
	bootTime = othersPsutilHelper.readBootTime()

	writeDataToDatabase(serialId, cpuData, cpuPercentageTotal, cpuPercentagePerProcessor, cpuStats, cpuFreqTotal,
						virtualMemoryData, swapMemoryData, diskUsage, diskIoCountersTotal,
					    netIoCountersTotal, sensorTemperatures, bootTime)

def run():
	"Starts the program"
	try:
		serialNumber = serial.getSerial()
		cpuCountLogical = cpuPsutilHelper.readCpuCountLogical()
		cpuCount = cpuPsutilHelper.readCpuCount()
		print(language.getString('SerialNumber', serialNumber))
		serialId = writeMasterDataToDatabase(serialNumber, cpuCountLogical, cpuCount)
		print(language.getString('SerialId', str(serialId)))
		if serialId == -1:
			return
		readPeriodicData(serialId)
	except Exception as e:
		traceback.print_exc()

run()