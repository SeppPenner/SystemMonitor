USE SystemMonitor;

#Begin master data
DELIMITER //
CREATE PROCEDURE systemMonitorInsertMasterData(IN serial VARCHAR(255), IN cpuCountLogical DECIMAL(30, 2) UNSIGNED, IN cpuCount DECIMAL(30, 2) UNSIGNED)
 BEGIN
	INSERT INTO SystemMonitor.MasterData(`serial`, `cpuCountLogical`, `cpuCount`) VALUES (serial, cpuCountLogical, cpuCount);
 END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE systemMonitorGetMasterData(IN serial VARCHAR(255))
 BEGIN
 SELECT `id`, `serial` FROM SystemMonitor.MasterData
 WHERE `serial` = serial;
 END //
DELIMITER ;
#End master data

#Begin periodic data
DELIMITER //
CREATE PROCEDURE systemMonitorLoadPeriodicData(IN serialId BIGINT, IN cpuDataUser DECIMAL(30, 2) UNSIGNED, IN cpuDataNice DECIMAL(30, 2) UNSIGNED,
											   IN cpuDataSystem DECIMAL(30, 2) UNSIGNED, IN cpuDataIdle DECIMAL(30, 2) UNSIGNED,
											   IN cpuDataIoWait DECIMAL(30, 2) UNSIGNED, IN cpuDataIrq DECIMAL(30, 2) UNSIGNED,
											   IN cpuDataSoftIrq DECIMAL(30, 2) UNSIGNED, IN cpuDataSteal DECIMAL(30, 2) UNSIGNED,
											   IN cpuDataGuest DECIMAL(30, 2) UNSIGNED, IN cpuDataGuestNice DECIMAL(30, 2) UNSIGNED,
											   IN cpuPercentageTotal DECIMAL(30, 2) UNSIGNED, IN cpuPercentageCore1 DECIMAL(30, 2) UNSIGNED,
											   IN cpuPercentageCore2 DECIMAL(30, 2) UNSIGNED, IN cpuPercentageCore3 DECIMAL(30, 2) UNSIGNED,
											   IN cpuPercentageCore4 DECIMAL(30, 2) UNSIGNED, IN cpuPercentageCore5 DECIMAL(30, 2) UNSIGNED,
											   IN cpuPercentageCore6 DECIMAL(30, 2) UNSIGNED, IN cpuPercentageCore7 DECIMAL(30, 2) UNSIGNED,
											   IN cpuPercentageCore8 DECIMAL(30, 2) UNSIGNED, IN cpuStatsSwitches BIGINT UNSIGNED,
											   IN cpuStatsInterrupts BIGINT UNSIGNED, IN cpuStatsSoftInterrupts BIGINT UNSIGNED,
											   IN cpuStatsSysCalls BIGINT UNSIGNED, IN cpuFreqTotalCurrent DECIMAL(30, 2) UNSIGNED,
											   IN cpuFreqTotalMin DECIMAL(30, 2) UNSIGNED, IN cpuFreqTotalMax DECIMAL(30, 2) UNSIGNED,
											   IN virtualMemoryDataTotal BIGINT UNSIGNED, IN virtualMemoryDataAvailable BIGINT UNSIGNED,
											   IN virtualMemoryDataPercent DECIMAL(30, 2) UNSIGNED, IN virtualMemoryDataUsed BIGINT UNSIGNED,
											   IN virtualMemoryDataFree BIGINT UNSIGNED, IN virtualMemoryDataActive BIGINT UNSIGNED,
											   IN virtualMemoryDataInactive BIGINT UNSIGNED, IN virtualMemoryDataBuffers BIGINT UNSIGNED,
											   IN virtualMemoryDataCached BIGINT UNSIGNED, IN virtualMemoryDataShared BIGINT UNSIGNED,
											   IN virtualMemoryDataSlab BIGINT UNSIGNED, IN swapMemoryDataTotal BIGINT UNSIGNED,
											   IN swapMemoryDataUsed BIGINT UNSIGNED, IN swapMemoryDataFree BIGINT UNSIGNED,
											   IN swapMemoryDataPercent DECIMAL(30, 2) UNSIGNED, IN swapMemoryDataSin BIGINT UNSIGNED,
											   IN swapMemoryDataSout BIGINT UNSIGNED, IN diskUsageTotal BIGINT UNSIGNED,
											   IN diskUsageUsed BIGINT UNSIGNED, IN diskUsageFree BIGINT UNSIGNED,
											   IN diskUsagePercent DECIMAL(30, 2) UNSIGNED, IN diskIoCountersTotalReadCount BIGINT UNSIGNED,
											   IN diskIoCountersTotalWriteCount BIGINT UNSIGNED, IN diskIoCountersTotalReadBytes BIGINT UNSIGNED,
											   IN diskIoCountersTotalWriteBytes BIGINT UNSIGNED, IN diskIoCountersTotalReadTime BIGINT UNSIGNED,
											   IN diskIoCountersTotalWriteTime BIGINT UNSIGNED, IN netIoCountersTotalBytesSent BIGINT UNSIGNED,
											   IN netIoCountersTotalBytesReceived BIGINT UNSIGNED, IN netIoCountersTotalPaketsSent BIGINT UNSIGNED,
											   IN netIoCountersTotalPaketsReceived BIGINT UNSIGNED, IN netIoCountersTotalErrIn BIGINT UNSIGNED,
											   IN netIoCountersTotalErrOut BIGINT UNSIGNED, IN netIoCountersTotalDropIn BIGINT UNSIGNED,
											   IN netIoCountersTotalDropOut BIGINT UNSIGNED, IN  sensorTemperaturesLabel VARCHAR(255),
											   IN sensorTemperaturesCurrent DECIMAL(30, 2) UNSIGNED, IN sensorTemperaturesHigh DECIMAL(30, 2) UNSIGNED,
											   IN sensorTemperaturesCritical DECIMAL(30, 2) UNSIGNED, IN bootTime DECIMAL(30, 2) UNSIGNED)
 BEGIN
	INSERT INTO Monitoring (`serialId`, `createdAt`, `cpuDataUser`, `cpuDataNice`, `cpuDataSystem`, `cpuDataIdle`, `cpuDataIoWait`, `cpuDataIrq`,
							`cpuDataSoftIrq`, `cpuDataSteal`, `cpuDataGuest`, `cpuDataGuestNice`, `cpuPercentageTotal`, `cpuPercentageCore1`,
							`cpuPercentageCore2`, `cpuPercentageCore3`, `cpuPercentageCore4`, `cpuPercentageCore5`, `cpuPercentageCore6`,
							`cpuPercentageCore7`, `cpuPercentageCore8`, `cpuStatsSwitches`, `cpuStatsInterrupts`, `cpuStatsSoftInterrupts`,
							`cpuStatsSysCalls`, `cpuFreqTotalCurrent`, `cpuFreqTotalMin`, `cpuFreqTotalMax`, `virtualMemoryDataTotal`,
							`virtualMemoryDataAvailable`, `virtualMemoryDataPercent`, `virtualMemoryDataUsed`,`virtualMemoryDataFree`,
							`virtualMemoryDataActive`, `virtualMemoryDataInactive`, `virtualMemoryDataBuffers`, `virtualMemoryDataCached`,
							`virtualMemoryDataShared`, `virtualMemoryDataSlab`, `swapMemoryDataTotal`, `swapMemoryDataUsed`, `swapMemoryDataFree`,
							`swapMemoryDataPercent`, `swapMemoryDataSin`, `swapMemoryDataSout`, `diskUsageTotal`, `diskUsageUsed`, `diskUsageFree`,
							`diskUsagePercent`, `diskIoCountersTotalReadCount`, `diskIoCountersTotalWriteCount`, `diskIoCountersTotalReadBytes`,
							`diskIoCountersTotalWriteBytes`, `diskIoCountersTotalReadTime`, `diskIoCountersTotalWriteTime`,
							`netIoCountersTotalBytesSent`, `netIoCountersTotalBytesReceived`, `netIoCountersTotalPaketsSent`,
							`netIoCountersTotalPaketsReceived`, `netIoCountersTotalErrIn`, `netIoCountersTotalErrOut`, `netIoCountersTotalDropIn`,
							`netIoCountersTotalDropOut`, `sensorTemperaturesLabel`, `sensorTemperaturesCurrent`, `sensorTemperaturesHigh`,
							`sensorTemperaturesCritical`, `bootTime`)
	VALUES (serialId, CURRENT_TIMESTAMP, cpuDataUser, cpuDataNice, cpuDataSystem, cpuDataIdle, cpuDataIoWait, cpuDataIrq, cpuDataSoftIrq,
			cpuDataSteal, cpuDataGuest, cpuDataGuestNice, cpuPercentageTotal, cpuPercentageCore1, cpuPercentageCore2, cpuPercentageCore3,
			cpuPercentageCore4, cpuPercentageCore5, cpuPercentageCore6, cpuPercentageCore7, cpuPercentageCore8, cpuStatsSwitches,
			cpuStatsInterrupts, cpuStatsSoftInterrupts, cpuStatsSysCalls, cpuFreqTotalCurrent, cpuFreqTotalMin, cpuFreqTotalMax,
			virtualMemoryDataTotal, virtualMemoryDataAvailable, virtualMemoryDataPercent, virtualMemoryDataUsed, virtualMemoryDataFree,
			virtualMemoryDataActive, virtualMemoryDataInactive, virtualMemoryDataBuffers, virtualMemoryDataCached, virtualMemoryDataShared,
			virtualMemoryDataSlab, swapMemoryDataTotal, swapMemoryDataUsed, swapMemoryDataFree, swapMemoryDataPercent, swapMemoryDataSin,
			swapMemoryDataSout, diskUsageTotal, diskUsageUsed, diskUsageFree, diskUsagePercent, diskIoCountersTotalReadCount,
			diskIoCountersTotalWriteCount, diskIoCountersTotalReadBytes, diskIoCountersTotalWriteBytes, diskIoCountersTotalReadTime,
			diskIoCountersTotalWriteTime, netIoCountersTotalBytesSent, netIoCountersTotalBytesReceived, netIoCountersTotalPaketsSent,
			netIoCountersTotalPaketsReceived, netIoCountersTotalErrIn, netIoCountersTotalErrOut, netIoCountersTotalDropIn,
			netIoCountersTotalDropOut, sensorTemperaturesLabel, sensorTemperaturesCurrent, sensorTemperaturesHigh, sensorTemperaturesCritical,
			bootTime);
 END //
DELIMITER ;
#End periodic data

#Begin index
CREATE INDEX systemMonitorMonitoringCreatedAtIndex ON SystemMonitor.Monitoring(createdAt);
#End index