import matplotlib.pyplot as plt
import sys

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
				self.pattern2 = ['', '', '--', '*', 's', '+']

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
				#print(self.data[j][i])
				for t in range(len(self.data[j][i])):
					if(t%max(num_plots) >= num_plots[k]):
						data[t%max(num_plots)].append(0)
					else:
						data[t%num_plots[k]].append(self.data[j][i][t])


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
					mx = max(mx, max(self.data[j][i]) - 170)
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
				for t in range(len(self.data[j][i])):
					if(t%min(num_plots) >= num_plots[k]):
						data[t%min(num_plots)].append(0)
					else:
						data[t%num_plots[k]].append(self.data[j][i][t])

				try:
					for f in range(len(data[0])):
						data_plot.append(0)
						for t in range(min(num_plots)):
							data_plot[f] = data_plot[f] + data[t][f]
				except:
					print("An error is occured")


				p = self.pattern1[k] + self.pattern2[0]
				plt.plot(range(len(data_plot) + 1)[1:], data_plot, p)

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
			plt.show()

		
a = Plot()

plots_dict = {1:1, 2:1, 3:1, 6:1, 7:1, 8:1, 11:2, 13:2, 21:2, 23:2, 101:1, 104:1, 116:1, 164:1, 165:1, 404:1, 416:1, 464:1, 465:1, 201:3, 202:4, 203:4, 204:3, 501:3, 502:4, 503:4, 601:3, 602:4, 603:4, 604:3, 801:5, 802:5, 1001:1, 1003:1}

if(len(sys.argv) != 1 and sys.argv[1] == "same"):
	a.plot_same(['Elapsed_Time'], plots_dict)
else:
	a.plot(['Elapsed_Time'], plots_dict)

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'Context_Switch_Forced', 'Context_Switch'])

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'CPU', 'Context_Switch_Forced', 'Context_Switch', 'Major_Page_Faults', 'Minor_Page_Faults', 'Swapped_Out_From_Main_Memory', 'Maximum_Resident_Set_Size'])



