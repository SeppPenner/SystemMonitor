# Data formats from [psutil](https://psutil.readthedocs.io/en/latest/)

## Master data
```python
# cpuCountLogical: 4
# cpuCount: 2
```

## Periodic data
```python
# cpuData: scputimes(user=17411.7, nice=77.99, system=3797.02, idle=51266.57, iowait=732.58, irq=0.01, softirq=142.43, steal=0.0, guest=0.0, guest_nice=0.0)
# cpuPercentageTotal: 2.9
# cpuPercentagePerProcessor: [2.0, 1.0]
# cpuTimesPercentageTotal: 2.9
# cpuStats: scpustats(ctx_switches=20455687, interrupts=6598984, soft_interrupts=2134212, syscalls=0)
# cpuFreqTotal: scpufreq(current=931.42925, min=800.0, max=3500.0)
# virtualMemoryData: svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712, active=4748992512,
# 					  inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304, slab=199348224)
# swapMemoryData: sswap(total=2097147904L, used=886620160L, free=1210527744L, percent=42.3, sin=1050411008, sout=1906720768)
# diskUsage: sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
# diskIoCountersTotal: sdiskio(read_count=8141, write_count=2431, read_bytes=290203, write_bytes=537676, read_time=5868, write_time=94922)
# netIoCountersTotal: snetio(bytes_sent=14508483, bytes_recv=62749361, packets_sent=84311, packets_recv=94888, errin=0, errout=0, dropin=0, dropout=0)
# sensorTemperatures: {'acpitz': [shwtemp(label='', current=47.0, high=103.0, critical=103.0)],
# 						'asus': [shwtemp(label='', current=47.0, high=None, critical=None)],
# 						'coretemp': [shwtemp(label='Physical id 0', current=52.0, high=100.0, critical=100.0),
#      							 shwtemp(label='Core 0', current=45.0, high=100.0, critical=100.0),
#      							 shwtemp(label='Core 1', current=52.0, high=100.0, critical=100.0),
#      							 shwtemp(label='Core 2', current=45.0, high=100.0, critical=100.0),
#     								 shwtemp(label='Core 3', current=47.0, high=100.0, critical=100.0)]}
# bootTime: 1389563460.0
```