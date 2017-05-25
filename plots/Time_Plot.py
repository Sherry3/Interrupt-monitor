import matplotlib.pyplot as plt
import sys

class Plot():
	def __init__(self):
		self.path = []
		self.data = {}
		self.pattern = []

		if(len(sys.argv) != 1):
			self.pattern1 = ['g', 'r', 'y', 'b', 'c', 'k']
			self.pattern2 = ['o', '', '--', '*', 's', '+']

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
	
		plots_dict = {1:1, 2:1, 3:1, 6:1, 7:1, 8:1, 101:1, 104:1, 116:1, 164:1, 165:1, 404:1, 416:1, 464:1, 465:1, 201:3, 202:4, 203:4, 501:3, 502:4, 503:4, 601:3, 602:4, 603:4, 801:5, 802:5}
		num_plots = []

		row = 1
		col = 2

		for i in sys.argv[1:]:
			num_plots.append(plots_dict[int(i)])

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


				plt.subplot(row, col, k + 1)
				plt.title('EXP :: ' + sys.argv[1 + k])

				for t in range(max(num_plots)):
					#print(data[t])
					p = self.pattern1[k] + self.pattern2[t]
					#print(p)
					plt.plot(range(len(data[t]) + 1)[1:], data[t], p)

				mi = min(mi, min(self.data[j][i]))
				mx = max(mx, max(self.data[j][i]))
				k = k + 1
		
			k = 0
			for j in self.path:
				plt.subplot(row, col, k + 1)
				plt.axis([0, len(data[0]), mi, mx])
				k = k + 1

			plt.show()

		
a = Plot()
a.plot(['Elapsed_Time'])

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'Context_Switch_Forced', 'Context_Switch'])

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'CPU', 'Context_Switch_Forced', 'Context_Switch', 'Major_Page_Faults', 'Minor_Page_Faults', 'Swapped_Out_From_Main_Memory', 'Maximum_Resident_Set_Size'])



