import os
import time

time.sleep(120)
os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq >> log_cpu_freq.txt')
os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq >> log_cpu_freq.txt')
os.system('python3 /home/sourabh/Desktop/Sherry/Monitor.py')
os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq >> log_cpu_freq.txt')
os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq >> log_cpu_freq.txt')
os.system('sudo reboot')
