import os
from subprocess import call
import subprocess
import time

class Monitor:
	def __init__(self):

		self.interrupt_name = '0000:00:1f.2'						#HDD interrupt name
		
		self.next_exp = {}
		self.next_exp["501"] = "502"
		self.next_exp["502"] = "503"
		self.next_exp["503"] = "202"
		self.next_exp["202"] = "203"
		self.next_exp["203"] = "501"
	
		#Experiment number
		ff_input = "/home/sourabh/Desktop/Sherry/input" 				#Experiment number input file
		ffr = open(ff_input, "r")		
		
		ff_num = ffr.readlines()[0].split('\n')[0]

		self.path = "/home/sourabh/Desktop/Sherry/exp" + ff_num + "/"			#Experiment path
		self.log_file_path = ''

		try:
			self.log_file_path = "/home/sourabh/Desktop/Sherry/log" + ff_num + ".txt"
			self.log_file = open(self.log_file_path, 'a+')
		except:
			self.log_file_path = "/home/sourabh/Desktop/Sherry/log.txt"
			self.log_file = open(self.log_file_path, 'a')
		
		self.log_file.write("\nSession started\n")
		self.log_file.write("\nDirectory :: " + self.path + "\n")
		ffr.close()
		#Experiment number
		

		#if(self.path[-1] != '/'):
		#	self.path = self.path + '/'

		f = open(self.path + "readme.txt", "r")
		lines = f.readlines()

		self.d ={}
		for i in lines:
			j = i.split('\n')[0].split()
			print(j)
			if(len(j) >= 2):
				self.d[j[0]] = j[1]	

		if(self.d['b_smp_affinity'] == 'true'):
			self.log_file.write("Core affinity started --- ")
			self.set_core_affinity()
			self.log_file.write("Core affinity closed\n")


		if('cpu_freq' in self.d and self.d['cpu_freq'] == 'true'):
			self.log_file.write("CPU frequency started\n")
			self.change_cpu_frequency()
			self.log_file.write("CPU frequency stopped\n")

		self.log_file.write("Monitoring started\n")
		self.start_monitor1()
		self.log_file.write("Monitoring stopped\n")

		self.log_file.write("txt copy started --- ")
		limit_reached = self.copy()
		self.log_file.write("txt copy stopped\n")

		#print("rm " + self.path + "txt/*")
		#print("rm /home/sourabh/Desktop/" + self.d['stress2'] + '/*')

		self.log_file.write("Removing txt started --- ")
		os.system("rm " + self.path + "txt/*")
		self.log_file.write("Removing txt stopped\n")

		if(self.d['stress2'] != "false"):
			self.log_file.write("Removing " + self.d['stress2'] + " started --- ")
			#os.system("ls /home/sourabh/Desktop/" + self.d['stress2'] + " >> /home/sourabh/Desktop/Sherry/log.txt")
			os.system("rm /home/sourabh/Desktop/" + self.d['stress2'] + '/*')
			self.log_file.write("Removing " + self.d['stress2'] + " stopped\n")
	
		#if(limit_reached == 30):
		#self.log_file.write("Limit reached\n")
		ffw = open(ff_input, 'w')
		ffw.write(self.next_exp[ff_num])
		self.log_file.write("Changed to " + self.next_exp[ff_num] + "\n")
		ffw.close()
			
		self.log_file.close()
		os.system('cat /proc/cmdline >> ' + self.log_file_path)
		

	def set_core_affinity(self):
		irqs = os.listdir("/proc/irq")
		#print(irqs)

		for irq_num in irqs[1 : len(irqs) - 1]:
			name = "/proc/irq/" + irq_num + "/smp_affinity"
			#print(name)
			os.system('sudo echo ' + self.d['other_irqs'] + ' > ' + name)		#Other smp affinity

		f_int = open("/proc/interrupts", "r")
		j = '0'

		lines = f_int.readlines()
		for i in lines:
			if(len(i.split()) == 8 and (i.split())[7] == self.interrupt_name):
				j = (i.split())[0].split(':')[0]

		if(j == '0'):
			print(self.interrupt_name + " interrupt not found")
		else:
			#HDD smp affinity
			os.system('sudo echo ' + self.d['hdd_irqs'] + ' > ' + "/proc/irq/" + str(j) + "/smp_affinity")
			#print("Affinity updated to 08 of " + "/proc/irq/" + str(j) + "/smp_affinity")

	def start_monitor1(self):
		f_m = open(self.path + "txt/memory.txt", "w+")
		f_c = open(self.path + "txt/cores.txt", "w+")
		f_d = open(self.path + "txt/disk.txt", "w+")
		f_h = open(self.path + "txt/hdd_int.txt", "w+")


		#Disk read/write
		#if(self.d['b_disk_rw'] == 'true')
		#	system.os("dstat -d >" +  self.path + "txt/disk_rw.txt&")


		for k in range(int(self.d['work_delay']) + int(self.d['copy_time']) + int(self.d['after_copy_time'])):

			if(k % 100 == 1):
				print(k)


			if(k == int(self.d['work_delay'])):
				cmd1 = ''

				if(self.d['b_time'] == 'true'):
					fmat = '"Elapsed_Time %e\n'
					fmat = fmat + 'Kernel_Time %S\n'
					fmat = fmat + 'User_Time %U\n'
					fmat = fmat + 'Major_Page_Faults %F\n'
					fmat = fmat + 'Minor_Page_Faults %R\n'
					fmat = fmat + 'Maximum_Resident_Set_Size %M\n'
					fmat = fmat + 'CPU %P\n'
					fmat = fmat + 'Swapped_Out_From_Main_Memory %W\n'
					fmat = fmat + 'Context_Switch_Forced %c\n'
					fmat = fmat + 'Context_Switch %w\n\n"'

					cmd1 = cmd1 + '/usr/bin/time -a -f ' + fmat + ' -o ' + self.path + 'time.txt '

				if(self.d['taskset'] == 'true'):
					cmd1 = 'taskset ' + self.d['taskset_affinity']
			
				if(self.d['stress1'] == 'true'):
					cmd1 = cmd1 + ' stress'
					if(self.d['stress_disk'] == 'true'):
						cmd1 = cmd1 + " -d " + self.d['disk_workers'] + ' --hdd-bytes ' + self.d['disk_size']
					if(self.d['stress_cores'] == 'true'):
						cmd1 = cmd1 + " -c " + self.d['core_workers']
					if(self.d['stress_memory'] == 'true'):
						cmd1 = cmd1 + " -m " + self.d['memory_workers'] + ' --vm-bytes ' + self.d['memory_size']

					cmd1 = cmd1 + ' -t ' + self.d['stress_period']

					os.system(cmd1 + "&")
					self.log_file.write("Reached stress1 " + self.d['stress1'] + "\n")
					self.log_file.write("Executing "+ cmd1 + "&\n")

				#New command
				cmd2 = ''

				if(self.d['b_time'] == 'true'):
					fmat = '"Elapsed_Time %e\n'
					fmat = fmat + 'Kernel_Time %S\n'
					fmat = fmat + 'User_Time %U\n'
					fmat = fmat + 'Major_Page_Faults %F\n'
					fmat = fmat + 'Minor_Page_Faults %R\n'
					fmat = fmat + 'Maximum_Resident_Set_Size %M\n'
					fmat = fmat + 'CPU %P\n'
					fmat = fmat + 'Swapped_Out_From_Main_Memory %W\n'
					fmat = fmat + 'Context_Switch_Forced %c\n'
					fmat = fmat + 'Context_Switch %w\n\n"'

					cmd2 = cmd2 + '/usr/bin/time -a -f ' + fmat + ' -o ' + self.path + 'time.txt '

				if(self.d['taskset'] == 'true'):
					cmd2 = cmd2 + ' taskset ' + self.d['taskset_affinity']

				if(self.d['stress2'] == 'small_files'):
					cmd2 = cmd2 + ' cp /media/sourabh/SHERRY/Small/* /home/sourabh/Desktop/' + self.d['stress2']
					os.system(cmd2 + "&")
					self.log_file.write("Reached stress2 " + self.d['stress2'])
					self.log_file.write("Executing "+ cmd2 + "&\n")

				if(self.d['stress2'] == 'big_files'):
					cmd2 = cmd2 + ' cp /media/sourabh/SHERRY/Big/* /home/sourabh/Desktop/' + self.d['stress2']
					os.system(cmd2 + "&")
					self.log_file.write("Reached stress2" + self.d['stress2'] + "\n")
					self.log_file.write("Executing "+ cmd2 + "&\n")

				if(self.d['stress2'] == 'multiple_big_files'):
					for i in range(3):
						cmd_temp = cmd2 + ' cp /media/sourabh/SHERRY/Big/' + str(i + 1) + '.mkv /home/sourabh/Desktop/' + self.d['stress2']
						os.system(cmd_temp + "&")
						self.log_file.write("Reached stress2" + self.d['stress2'] + "\n")
						self.log_file.write("Executing "+ cmd_temp + "&\n")


			#Memory info
			if(self.d['b_memory'] == 'true'):
				mem = open("/proc/meminfo", "r")
				lines = mem.readlines()

				for i in [0, 1, 6]:
					f_m.write(lines[i])

				cmd = ['free', '-h',]
				lines = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

				f_m.write(lines[1] + "\n")
				f_m.write("\n")
	
			#Cores info
			if(self.d['b_core'] == 'true'):
				cmd = ['mpstat', '-P', 'ALL']
				lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

				for i in lines[2:-1]:
					f_c.write(i + "\n")
			
				f_c.write("\n")


			#Disk info
			if(self.d['b_disk'] == 'true'):	
				cmd = ['iostat']
				lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

				for i in range(5, 7):
					f_d.write(lines[i] + '\n')
			
				f_d.write("\n")

			#HDD Interrupts
			if(self.d['b_int'] == 'true'):
				f_int = open("/proc/interrupts", "r")
				j = '0'

				lines = f_int.readlines()
				for i in lines:
					if(len(i.split()) == 8 and (i.split())[7] == self.interrupt_name):
						f_h.write(i + "\n")
						j = (i.split())[0].split(':')[0]
			
				f_h.write("\n")
			
			time.sleep(1)


	def start_monitor2(self):
		f_m = open(self.path + "txt/memory.txt", "w+")
		f_c = open(self.path + "txt/cores.txt", "w+")
		f_d = open(self.path + "txt/disk.txt", "w+")
		f_h = open(self.path + "txt/hdd_int.txt", "w+")

		#Disk read/write
		#if(self.d['b_disk_rw'] == 'true')
		#	system.os("dstat -d >" +  self.path + "txt/disk_rw.txt&")


		for k in range(int(self.d['work_delay']) + int(self.d['copy_time']) + int(self.d['after_copy_time'])):

			if(k % 100 == 1):
				print(k)

			if(k == int(self.d['work_delay'])):
				cmd1 = ''
				if(self.d['taskset'] == 'true'):
					cmd1 = 'taskset ' + self.d['taskset_affinity']
			
				if(self.d['stress1'] == 'true'):
					cmd1 = cmd1 + ' stress'
					if(self.d['stress_disk'] == 'true'):
						cmd1 = cmd1 + " -d " + self.d['disk_workers'] + ' --hdd-bytes ' + self.d['disk_size']
					if(self.d['stress_cores'] == 'true'):
						cmd1 = cmd1 + " -c " + self.d['core_workers']
					if(self.d['stress_memory'] == 'true'):
						cmd1 = cmd1 + " -m " + self.d['memory_workers'] + ' --vm-bytes ' + self.d['memory_size']

					cmd1 = cmd1 + ' -t ' + self.d['stress_period']

					os.system(cmd1 + "&")
					self.log_file.write("Reached stress1 " + self.d['stress1'] + "\n")
					self.log_file.write("Executing "+ cmd1 + "&\n")

				#New command
				cmd2 = ''

				if(self.d['b_time'] == 'true'):
					fmat = '"Elapsed_Time %e\n'
					fmat = fmat + 'Kernel_Time %S\n'
					fmat = fmat + 'User_Time %U\n'
					fmat = fmat + 'Major_Page_Faults %F\n'
					fmat = fmat + 'Minor_Page_Faults %R\n'
					fmat = fmat + 'Maximum_Resident_Set_Size %M\n'
					fmat = fmat + 'CPU %P\n'
					fmat = fmat + 'Swapped_Out_From_Main_Memory %W\n'
					fmat = fmat + 'Context_Switch_Forced %c\n'
					fmat = fmat + 'Context_Switch %w\n\n"'

					cmd2 = cmd2 + '/usr/bin/time -a -f ' + fmat + ' -o ' + self.path + 'time.txt '

				if(self.d['taskset'] == 'true'):
					cmd2 = cmd2 + ' taskset ' + self.d['taskset_affinity']

				if(self.d['stress2'] == 'small_files'):
					cmd2 = cmd2 + ' cp /media/sourabh/SHERRY/Small/* /home/sourabh/Desktop/' + self.d['stress2']
					os.system(cmd2 + "&")
					self.log_file.write("Reached stress2 " + self.d['stress2'])
					self.log_file.write("Executing "+ cmd2 + "&\n")

				if(self.d['stress2'] == 'big_files'):
					cmd2 = cmd2 + ' cp /media/sourabh/SHERRY/Big/* /home/sourabh/Desktop/' + self.d['stress2']
					os.system(cmd2 + "&")
					self.log_file.write("Reached stress2" + self.d['stress2'] + "\n")
					self.log_file.write("Executing "+ cmd2 + "&\n")

			#Memory info
			if(self.d['b_memory'] == 'true'):
				mem = open("/proc/meminfo", "r")
				lines = mem.readlines()

				for i in [0, 1, 6]:
					f_m.write(lines[i])

				cmd = ['free', '-h',]
				lines = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

				f_m.write(lines[1] + "\n")
				f_m.write("\n")
	
			#Cores info
			if(self.d['b_core'] == 'true'):
				cmd = ['mpstat', '-P', 'ALL']
				lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

				for i in lines[2:-1]:
					f_c.write(i + "\n")
			
				f_c.write("\n")


			#Disk info
			if(self.d['b_disk'] == 'true'):	
				cmd = ['iostat']
				lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

				for i in range(5, 7):
					f_d.write(lines[i] + '\n')
			
				f_d.write("\n")

			#HDD Interrupts
			if(self.d['b_int'] == 'true'):
				f_int = open("/proc/interrupts", "r")
				j = '0'

				lines = f_int.readlines()
				for i in lines:
					if(len(i.split()) == 8 and (i.split())[7] == self.interrupt_name):
						f_h.write(i + "\n")
						j = (i.split())[0].split(':')[0]
			
				f_h.write("\n")
			
			time.sleep(1)


	def copy(self):	
		fr = open(self.path + 'plot_num.txt', 'r')
		num = fr.readlines()[0].split('\n')[0]
		fr.close()
		print(num)

		fw = open(self.path + 'plot_num.txt', 'w')
		fw.write(str(int(num) + 1))
		fw.close()

		to = self.path + "plot" + num
		os.system('mkdir ' + to)
		os.system('cp ' + self.path + 'txt/* ' + to)		

		return int(num)

	def change_cpu_frequency(self):
		os.system("sudo ./changeFreq.sh")
	


A = Monitor()
