import matplotlib.pyplot as plt
import sys

class Plot():
	def __init__(self):
		self.path = []
		self.data = {}
		self.pattern = []

		if(len(sys.argv) != 1):
			self.pattern1 = ['g', 'r', 'y', 'b', 'c', 'k']
			self.pattern2 = ['o', '', '--', '*', '+', 's']

			self.pattern = []
			for i in self.pattern2:
				for j in self.pattern1:
					self.pattern.append(i + j)

			for a in sys.argv[1:]:
				self.path.append("/home/sourabh/Desktop/Sherry/exp" + a + "/time.txt")
		else:		
			exp = input("Experiments : ").split()
			self.pattern = input("Grapg symbols : ").split()

			if(len(exp) != len(self.pattern)):
				print("Experiment and graph symbols must have same number of values")
				exit()
	
			for i in exp:
				self.path.append("/home/sourabh/Desktop/Sherry/exp" + i + "/time.txt")
			
		f = open(self.path[0], 'r')
		lines = f.readlines()

		for path in self.path:			
			f = open(path, 'r')
			lines = f.readlines()
			
			self.data[path] = {}			

			#Extract all attributes from file
			for i in lines:
				if(len(i.split()) < 2):
					break

				j = i.split('\n')[0].split()
				self.data[path][j[0]] = []

			for i in lines:
				j = i.split('\n')[0].split('%')[0].split()
				if(len(j) == 2):
					self.data[path][j[0]].append(float(j[1]))	

	def plot(self, attr):
		num_plots = [1, 1, 1, 2, 2, 2]
		for i in attr:
			plt.title(i)
			mi = min(self.data[self.path[0]][i])
			mx = min(self.data[self.path[0]][i])
			
			k = 0
			data = []

			for j in self.path:
				data.clear()
				for t in range(max(num_plots)):
					data.append([])
				#print(self.data[j][i])
				for t in range(len(self.data[j][i])):
					if(t%max(num_plots) >= num_plots[k]):
						data[t%max(num_plots)].append(0)
					else:
						data[t%num_plots[k]].append(self.data[j][i][t])

				for t in range(min(num_plots)):
					#print(data[t])
					p = self.pattern1[k] + self.pattern2[t]
					#print(p)
					plt.plot(range(len(data[t]) + 1)[1:], data[t], p)

				#plt.plot(range(len(self.data[j][i]) + 1)[1:], self.data[j][i], self.pattern[k])		
				mi = min(mi, min(self.data[j][i]))
				mx = max(mx, max(self.data[j][i]))
				k = k + 1
		
			#plt.axis([0, len(self.data[self.path[0]][i]), mi, mx])
			plt.axis([0, len(data[0]), mi, mx])
			plt.show()

		
a = Plot()
a.plot(['Elapsed_Time'])

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'Context_Switch_Forced', 'Context_Switch'])

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'CPU', 'Context_Switch_Forced', 'Context_Switch', 'Major_Page_Faults', 'Minor_Page_Faults', 'Swapped_Out_From_Main_Memory', 'Maximum_Resident_Set_Size'])



