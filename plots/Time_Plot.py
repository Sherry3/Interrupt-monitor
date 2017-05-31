import matplotlib.pyplot as plt
import sys
import os

class Plot():
	def __init__(self):
		self.path = []
		self.data = {}

		if(len(sys.argv) != 1):
			if(sys.argv[1] == "same"):
				self.pattern1 = ['g', 'r', 'y', 'b', 'c', 'k']
				self.pattern2 = ['', '--']

				for a in sys.argv[2:]:
					self.path.append("/home/sourabh/Desktop/Sherry/exp" + a + "/time.txt")

			else:
				self.pattern1 = ['g', 'r', 'y', 'b', 'c', 'k']
				self.pattern2 = ['', '--', '*', 's', '+']

				for a in sys.argv[1:]:
					self.path.append("/home/sourabh/Desktop/Sherry/exp" + a + "/time.txt")
		else:		
			self.exp = input("Experiments : ").split()
			self.pattern = input("Grapg symbols : ").split()

			if(len(self.exp) != len(self.pattern)):
				print("Experiment and graph symbols must have same number of values")
				exit()
	
			for i in self.exp:
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

	def plot(self, attr, plots_dict):
	
		num_plots = []

		row = int(input("rows : "))
		col = int(input("cols : "))

		if(len(sys.argv) != 1):
			for i in sys.argv[1:]:
				num_plots.append(plots_dict[int(i)])
		else:
			for i in self.exp:
				num_plots.append(plots_dict[int(i)])

		for i in attr:
			plt.title(i)
			
			k = 0
			data = []

			for j in self.path:
				data.clear()
				for t in range(max(num_plots)):
					data.append([])

				'''
				print('-------------------------------------')
				print(len(self.data[j][i]) / num_plots[k])
				print(self.data[j][i])
				print('-------------------------------------')
				'''
			
				for t in range(len(self.data[j][i])):
					data[t%num_plots[k]].append(self.data[j][i][t])

				for z in range(num_plots[k], max(num_plots)):
					for t in range(int(len(self.data[j][i]) / num_plots[k])):
						data[z].append(0)

				'''
				for t in range(max(num_plots)):
					print(len(data[t]))
					print(data[t])
					print()
				'''

				plt.subplot(row, col, k + 1)

				if(len(sys.argv) != 1):
					plt.title(i + ' ' + sys.argv[1 + k])
				else:
					plt.title(i + ' ' + self.exp[k])

				for t in range(max(num_plots)):
					#print(data[t])
					p = self.pattern1[k] + self.pattern2[t]
					plt.plot(range(len(data[t]) + 1)[1:], data[t], p)

				if('mi' in locals()):
					mi = min(mi, min(self.data[j][i]))
				else:
					mi = min(self.data[j][i])
			
				if('mx' in locals()):
					mx = max(mx, max(self.data[j][i]))
				else:
					mx = max(self.data[j][i])

				k = k + 1
		
			k = 0
			for j in self.path:
				plt.subplot(row, col, k + 1)
				plt.axis([0, len(data[0]), mi, mx])
				k = k + 1

			plt.show()

	def plot_same(self, attr, plots_dict):
		num_plots = []

		if(len(sys.argv) != 2):
			for i in sys.argv[2:]:
				num_plots.append(plots_dict[int(i)])
		else:
			for i in self.exp:
				num_plots.append(plots_dict[int(i)])


		for i in attr:
			plt.title(i)
			
			k = 0
			data = []
			data_plot = []

			for j in self.path:
				data.clear()
				data_plot.clear()
				for t in range(max(num_plots)):
					data.append([])
				#print(self.data[j][i])
				for z in range(max(num_plots)):
					if(z >= num_plots[k]):
						for t in range(int(len(self.data[j][i]) / num_plots[k])):
							data[z].append(0)
					else:
						for t in range(len(self.data[j][i])):
							data[t%num_plots[k]].append(self.data[j][i][t])

				try:
					for f in range(len(data[0])):
						data_plot.append(0)
						for t in range(min(num_plots)):
							data_plot[f] = data_plot[f] + data[t][f]
				except:
					print("An error is occured")


				p = self.pattern1[k%6] + self.pattern2[int(k/6)]
				plt.plot(range(len(data_plot) + 1)[1:], data_plot, p, label = sys.argv[2 + k])

				if('mi' in locals()):
					mi = min(mi, min(data_plot))
				else:
					mi = min(data_plot)
			
				if('mx' in locals()):
					mx = max(mx, max(data_plot))
				else:
					mx = max(data_plot)

				k = k + 1
		

			plt.axis([0, len(data_plot), mi, mx])
			plt.legend()
			plt.show()


	def plot_int2(self):
		
		result = {}

		for k in self.path:
			k = k[:-8]
			result[k] = 0

			exps = os.listdir(k)
			for i in exps:
				try:					
					f = open(k + i + "/hdd_int.txt", "r")
					lines = f.readlines()

					intr1 = [int(lines[0].split()[int(0) + 1])]
					intr2 = []

					for i in lines:
						if(i != "\n"):
							intr1.append(int(i.split()[int(self.d['int_core']) + 1]))

					for i in range(len(intr1)):
						result[k] = result[k] + (intr1[i] - intr1[i-1])
					
				except:
					print(k + i + "/hdd_int.txt" + " is not what you want")

		print(result)
		return result

		
a = Plot()

plots_dict = {1:1, 2:1, 3:1, 6:1, 7:1, 8:1, 11:2, 12:2, 13:2, 21:2, 22:2, 23:2, 101:1, 104:1, 116:1, 164:1, 165:1, 404:1, 416:1, 464:1, 465:1, 201:3, 202:4, 203:4, 204:3, 205:3, 501:3, 502:4, 503:4, 601:3, 602:4, 603:4, 604:3, 605:3, 801:5, 802:5, 1001:1, 1003:1}

if(len(sys.argv) != 1 and sys.argv[1] == "same"):
	a.plot_same(['Elapsed_Time'], plots_dict)
else:
	a.plot(['Elapsed_Time'], plots_dict)

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'Context_Switch_Forced', 'Context_Switch'])

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'CPU', 'Context_Switch_Forced', 'Context_Switch', 'Major_Page_Faults', 'Minor_Page_Faults', 'Swapped_Out_From_Main_Memory', 'Maximum_Resident_Set_Size'])



