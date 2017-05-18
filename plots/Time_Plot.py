import matplotlib.pyplot as plt
import sys

class Plot():
	def __init__(self):
		self.path = []
		self.data = {}

		for a in sys.argv[1:]:
			self.path.append("/home/sourabh/Desktop/Sherry/exp" + a + "/time.txt")
			
		f = open(self.path[0], 'r')
		lines = f.readlines()

		for path in self.path:			
			f = open(path, 'r')
			lines = f.readlines()
			
			self.data[path] = {}			

			for i in lines:
				if(len(i.split()) < 2):
					break

				j = i.split('\n')[0].split()
				self.data[path][j[0]] = []

			for i in lines:
				j = i.split('\n')[0].split('%')[0].split()
				if(len(j) >= 2):
					self.data[path][j[0]].append(float(j[1]))	

	def plot(self, attr):
		for i in attr:
			plt.title(i)
			pattern = ['go', 'ro', 'yo', 'bo']
			mi = min(self.data[self.path[0]][i])
			mx = min(self.data[self.path[0]][i])
			
			k = 0
			for j in self.path:
				#print(self.data[j][i])
				plt.plot(range(len(self.data[j][i]) + 1)[1:], self.data[j][i], pattern[k])
				mi = min(mi, min(self.data[j][i]))
				mx = max(mx, max(self.data[j][i]))
				k = k + 1
		
			plt.axis([0, len(self.data[self.path[0]][i]), mi, mx])
			plt.show()

		
a = Plot()
a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'Context_Switch_Forced', 'Context_Switch'])

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'CPU', 'Context_Switch_Forced', 'Context_Switch', 'Major_Page_Faults', 'Minor_Page_Faults', 'Swapped_Out_From_Main_Memory', 'Maximum_Resident_Set_Size'])



