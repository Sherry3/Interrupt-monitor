import os
import time

f = '/home/sourabh/Desktop/Sherry/log_cpu_freq.txt'
time.sleep(120)

os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq >> ' + f)
os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq >> ' + f)

os.system('python3 /home/sourabh/Desktop/Sherry/Monitor.py')

os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq >> ' + f)
os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq >> ' + f)
os.system('sudo echo -------------------------------------------' + f)

os.system('sudo reboot')
