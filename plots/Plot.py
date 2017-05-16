import matplotlib.pyplot as plt
import sys

class Plot():
	def __init__(self):
		if(len(sys.argv) > 1):
			self.path = "exp" + sys.argv[1] + "/plot" + sys.argv[2]
			self.exp = sys.argv[1] + "_" + sys.argv[2]
		else:
			self.path = input("Enter input directory : ")
			self.exp = self.path.split("/")[0][3] + "_" + self.path.split("/")[1][4]			

		self.path = "/home/sourabh/Desktop/Sherry/" + self.path

		if(self.path[-1] != '/'):
			self.path = self.path + '/'

		if(len(sys.argv) > 1 and sys.argv[3] == 'global'):
			f = open(self.path + "../../readme_plot.txt", "r")
		else:
			f = open(self.path + "../readme_plot.txt", "r")

		lines = f.readlines()

		self.d ={}
		for i in lines:
			j = i.split('\n')[0].split()
			self.d[j[0]] = j[1]	
	
	def plot_int(self):
		f = open(self.path + "hdd_int.txt", "r")
		lines = f.readlines()

		intr = []

		for i in lines:
			if(i != "\n"):
				intr.append(int(i.split()[int(self.d['int_core']) + 1]))

		plt.title('HDD interrupts ' + self.exp)
		plt.plot(range(len(intr)), intr, 'k')
		plt.axis([0, len(intr), min(intr), max(intr)])
		plt.show()


	def plot_memory(self):
		f = open(self.path + "memory.txt", "r")
		lines = f.readlines()

		free = []
		active = []
		used = []
		shared = []
		buff = []
		cache = []

		j = 0
		for i in lines:
			if(j % 5 == 1):
				k = i.split()
				free.append(int(k[1]))
	
			if(j % 5 == 2):
				k = i.split()
				active.append(int(k[1]))

			if(j % 5 == 3):
				k = i.split()
				#print(k[2][:-1])
				used.append(float(k[2][:-1]))
				shared.append(float(k[4][:-1]))
				buff.append(float(k[5][:-1]))
				cache.append(float(k[6][:-1]))
			j += 1
	

		plt.title('free and active ' + self.exp)
		plt.plot(range(len(free)), free, 'ro')
		plt.plot(range(len(active)), active, 'go')
		plt.axis([0, len(free), min([min(free), min(active)]), max(max(free), max(active))])
		plt.show()

		plt.title('used ' + self.exp)
		plt.plot(range(len(used)), used, 'ro')
		plt.axis([0, len(used), min(used), max(used)])
		plt.show()

		plt.title('shared ' + self.exp)
		plt.plot(range(len(shared)), shared, 'ro')
		plt.axis([0, len(shared), min(shared), max(shared)])
		plt.show()

		plt.title('buffer ' + self.exp)
		plt.plot(range(len(buff)), buff, 'ro')
		plt.axis([0, len(buff), min(buff), max(buff)])
		plt.show()

		plt.title('cached ' + self.exp)
		plt.plot(range(len(cache)), cache, 'ro')
		plt.axis([0, len(cache), min(cache), max(cache)])
		plt.show()

	def plot_core(self):
		f = open(self.path + "cores.txt", "r")
		lines = f.readlines()

		usr = []
		sys = []
		iowait = []
		idle = []

		for i in range(5):
			usr.append([])
			sys.append([])
			iowait.append([])
			idle.append([])

		for i in lines:
			k = i.split()	
			if(len(k) > 1 and k[2] != 'CPU'):
				if(k[2] == 'all'):
					usr[4].append(float(k[3]))
					sys[4].append(float(k[5]))
					iowait[4].append(float(k[6]))
					idle[4].append(float(k[12]))
				else:
					usr[int(k[2])].append(float(k[3]))
					sys[int(k[2])].append(float(k[5]))
					iowait[int(k[2])].append(float(k[6]))
					idle[int(k[2])].append(float(k[12]))


		if(self.d['core_choice'] == 'cpu'):
			for i in range(5):
				plt.title('CPU ' + str(i) + ' ' + self.exp)
				plt.plot(range(len(usr[i])), usr[i], 'ro')
				plt.plot(range(len(sys[i])), sys[i], 'bo')
				plt.plot(range(len(iowait[i])), iowait[i], 'g+')
				plt.plot(range(len(idle[i])), idle[i], 'gs')

				plt.axis([0, len(usr[i]), 0, 100])
				plt.show()

		else:
			plt.title('usr ' + self.exp)
			plt.plot(range(len(usr[0])), usr[0], 'r+')
			plt.plot(range(len(usr[1])), usr[1], 'g+')
			plt.plot(range(len(usr[2])), usr[2], 'b+')
			plt.plot(range(len(usr[3])), usr[3], 'y+')
			plt.plot(range(len(usr[4])), usr[4], 'c+')
			plt.axis([0, len(usr[0]), 0, 100])
			plt.show()

			plt.title('sys ' + self.exp)
			plt.plot(range(len(sys[0])), sys[0], 'r+')
			plt.plot(range(len(sys[1])), sys[1], 'g+')
			plt.plot(range(len(sys[2])), sys[2], 'b+')
			plt.plot(range(len(sys[3])), sys[3], 'y+')
			plt.plot(range(len(sys[4])), sys[4], 'c+')
			plt.axis([0, len(usr[0]), 0, 100])
			plt.show()

			plt.title('iowait ' + self.exp)
			plt.plot(range(len(iowait[0])), iowait[0], 'r+')
			plt.plot(range(len(iowait[1])), iowait[1], 'g+')
			plt.plot(range(len(iowait[2])), iowait[2], 'b+')
			plt.plot(range(len(iowait[3])), iowait[3], 'y+')
			plt.plot(range(len(iowait[4])), iowait[4], 'c+')
			plt.axis([0, len(usr[0]), 0, 100])
			plt.show()

			plt.title('idle ' + self.exp)
			plt.plot(range(len(idle[0])), idle[0], 'r+')
			plt.plot(range(len(idle[1])), idle[1], 'g+')
			plt.plot(range(len(idle[2])), idle[2], 'b+')
			plt.plot(range(len(idle[3])), idle[3], 'y+')
			plt.plot(range(len(idle[4])), idle[4], 'c+')
			plt.axis([0, len(usr[0]), 0, 100])
			plt.show()

	def plot_disk(self):	
		f = open(self.path + "disk.txt", "r")
		lines = f.readlines()

		tps = []
		r_s = []
		w_s = []
		r = []
		w = []

		for i in lines:
			j = i.split()
			if(len(j) > 0 and j[0] == "sda"):
				tps.append(float(j[1]))
				r_s.append(float(j[2]))
				w_s.append(float(j[3]))
				r.append(int(j[4]))
				w.append(int(j[5]))

		plt.title('tps ' + self.exp)
		plt.plot(range(len(tps)), tps, 'ro')
		plt.axis([0, len(tps), min(tps), max(tps)])
		plt.show()

		plt.title('read/s (KB) ' + self.exp)
		plt.plot(range(len(r_s)), r_s, 'ro')
		plt.axis([0, len(r_s), min(r_s), max(r_s)])
		plt.show()

		plt.title('write/s (KB) ' + self.exp)
		plt.plot(range(len(w_s)), w_s, 'ro')
		plt.axis([0, len(w_s), min(w_s), max(w_s)])
		plt.show()

		plt.title('read (KB) ' + self.exp)
		plt.plot(range(len(r)), r, 'ro')
		plt.axis([0, len(r), min(r), max(r)])
		plt.show()

		plt.title('write (KB) ' + self.exp)
		plt.plot(range(len(w)), w, 'ro')
		plt.axis([0, len(w), min(w), max(w)])
		plt.show()	

#	def plot_disk_rw(self):
		
a = Plot()
if(a.d['plot_int'] == 'true'):
	a.plot_int()
if(a.d['plot_core'] == 'true'):
	a.plot_core()
if(a.d['plot_disk'] == 'true'):
	a.plot_disk()
if(a.d['plot_disk_rw'] == 'true'):
	a.plot_disk_rw()
if(a.d['plot_memory'] == 'true'):
	a.plot_memory()
