import matplotlib.pyplot as plt
import sys

class Plot():
	def __init__(self):
		self.path = []
		self.data = {}

		if(len(sys.argv) != 1):
			if(sys.argv[1] == "all"):

				#if(sys.argv[2] == '1'):
				#	self.plots_all = [201, 204, 205, 601, 604, 605, 1, 3, 2, 11, 13, 12, 21, 23, 22, 8, 6, 7]
				#	self.pattern1 = ['bs', 'gs', 'rs']
	
				if(sys.argv[2] == '1'):
					self.plots_all = [1, 3, 2, 11, 13, 12, 21, 23, 22, 8, 6, 7]
					self.pattern1 = ['bs', 'gs', 'rs']
				if(sys.argv[2] == '2000'):
					self.plots_all = [2001, 2003, 2002, 2011, 2013, 2012, 2021, 2023, 2022, 2008, 2006, 2007]
					self.pattern1 = ['bs', 'gs', 'rs']
				if(sys.argv[2] == '3000'):
					self.plots_all = [3001, 3003, 3002, 3011, 3013, 3012, 3021, 3023, 3022, 3008, 3006, 3007]
					self.pattern1 = ['bs', 'gs', 'rs']
				if(sys.argv[2] == '2300'):
					self.plots_all = [2301, 2303, 2302, 2311, 2313, 2312, 2321, 2323, 2322, 2308, 2306, 2307]
					self.pattern1 = ['bs', 'gs', 'rs']

				if(sys.argv[2] == 'mul200'):
					self.plots_all = [201, 204, 205, 211, 214, 215, 221, 224, 225, 281, 284, 285]
					self.pattern1 = ['bs', 'gs', 'rs']
				if(sys.argv[2] == 'mul600'):
					self.plots_all = [601, 604, 605, 611, 614, 615, 621, 624, 625, 681, 684, 685]
					self.pattern1 = ['bs', 'gs', 'rs']

				for a in self.plots_all:
					self.path.append("/home/sourabh/Desktop/Sherry/exp" + str(a) + "/time.txt")

			elif(sys.argv[1] == "same" or sys.argv[1] == "mul"):
				self.pattern1 = ['b', 'r', 'g', 'y', 'c', 'k']
				self.pattern2 = ['', '--']

				for a in sys.argv[2:]:
					self.path.append("/home/sourabh/Desktop/Sherry/exp" + a + "/time.txt")

			else:
				self.pattern1 = ['b', 'r', 'g', 'y', 'c', 'k']
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
				if(len(j) == 2 and float(j[1]) > 1):
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
			data_plot = []

			for j in self.path:
				data.clear()
				data_plot.clear()
				for t in range(max(num_plots)):
					data.append([])

				#print(self.data[j][i])

				for t in range(len(self.data[j][i])):
					data[t%num_plots[k]].append(self.data[j][i][t])

				for z in range(num_plots[k], max(num_plots)):
					for t in range(int(len(self.data[j][i]) / num_plots[k])):
						data[z].append(0)

				for t in range(max(num_plots)):					
					print(data[t])

				print("\n\n")

				try:
					for f in range(len(data[0])):
						data_plot.append(0)
						#print(str(num_plots[k]) + " -- " + j[-13:-9])
						if(num_plots[k] == 1):					
							data_plot[f] = data[0][f]
						elif(num_plots[k] == 3):
							data_plot[f] = data[2][f]
						else:
							try:
								data_plot[f] = data[num_plots[k] - 2][f]
							except:
								data_plot[f] = sum(data_plot[:-1]) / len(data_plot[:-1])
								print("An error is occured 2")	
				except:
					print("An error is occured 1")



				plt.subplot(row, col, k + 1)

				if(len(sys.argv) != 1):
					plt.title(i + ' ' + sys.argv[1 + k])
				else:
					plt.title(i + ' ' + self.exp[k])

				p = self.pattern1[k]
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
		
			k = 0
			for j in self.path:
				plt.subplot(row, col, k + 1)
				plt.axis([0, len(data[0]), mi, mx])
				k = k + 1

			plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
			plt.savefig('pictures/plot_elapsed_time' + str(sys.argv[1:]))
			plt.show()
			plt.close()		


	def plot_mul(self, attr, plots_dict):
	
		num_plots = []

		row = int(input("rows : "))
		col = int(input("cols : "))

		if(len(sys.argv) != 1):
			for i in sys.argv[2:]:
				num_plots.append(plots_dict[int(i)])
		else:
			for i in self.exp:
				num_plots.append(plots_dict[int(i)])

		for i in attr:
			plt.title(i)
			
			k = 0
			data = []

			for j in self.path:
				print(j)
				print(self.data[j][i], end = "\n\n")
						
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
					plt.title(i + ' ' + sys.argv[2 + k])
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

			plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
			plt.savefig('pictures/plot_elapsed_time' + str(sys.argv[1:]))
			plt.show()
			plt.close()		

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
					data[t%num_plots[k]].append(self.data[j][i][t])

				for z in range(num_plots[k], max(num_plots)):
					for t in range(int(len(self.data[j][i]) / num_plots[k])):
						data[z].append(0)

				for t in range(max(num_plots)):					
					print(data[t])

				print("\n\n")

				try:
					for f in range(len(data[0])):
						data_plot.append(0)
						#print(str(num_plots[k]) + " -- " + j[-13:-9])
						if(num_plots[k] == 1):					
							data_plot[f] = data[0][f]
						elif(num_plots[k] == 3):
							data_plot[f] = data[2][f]
						else:
							try:
								data_plot[f] = data[num_plots[k] - 2][f]
							except:
								data_plot[f] = sum(data_plot[:-1]) / len(data_plot[:-1])
								print("An error is occured 2")	
				except:
					print("An error is occured 1")

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
		

			plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
			plt.savefig('pictures/plot_elapsed_time' + str(sys.argv[1:]))
			plt.show()
			plt.close()		


	def plot_all(self, attr, plots_dict):
		num_plots = []

		for i in self.plots_all:
			num_plots.append(plots_dict[int(i)])

		for i in attr:	
			k = 0
			data = []
			data_plot = []
			points = []
			
			for l in range(3):
				points.append([])

			for j in self.path:
				data.clear()
				data_plot.clear()
				for t in range(max(num_plots)):
					data.append([])

				#print(self.data[j][i], end = "\n\n")

				#print('-------------------------------------')
				#print(len(self.data[j][i]) / num_plots[k])
				#print(self.data[j][i])
				#print('-------------------------------------')
			
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

				try:
					for f in range(len(data[0])):
						data_plot.append(0)
						if(num_plots[k] == 1):
							data_plot[f] = data_plot[f] + data[0][f]
						elif(num_plots[k] == 3):
							data_plot[f] = data_plot[f] + data[2][f]
						else:
							data_plot[f] = data_plot[f] + data[num_plots[k] - 2][f]
							
				except:
					print("An error is occured")

				points[k%3].append(sum(data_plot)/len(data_plot))

				if('mi' in locals()):
					mi = min(mi, sum(data_plot)/len(data_plot))
				else:
					mi = sum(data_plot)/len(data_plot)
			
				if('mx' in locals()):
					mx = max(mx, sum(data_plot)/len(data_plot))
				else:
					mx = sum(data_plot)/len(data_plot)

				k = k + 1

			lab = ['Normal', 'IRQ to core 3', 'Core 3 isolated']

			for l in range(3):
				points[l].append(mi - 1)
				points[l] = [mi - 1] + points[l]
				plt.plot(range(int(len(self.plots_all)/3) + 2), points[l], self.pattern1[l], label = lab[l])
				plt.plot(range(1, int(len(self.plots_all)/3) + 1), points[l][1:-1], self.pattern1[l][0])
 
			
			plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
			plt.savefig('pictures/plot_elapsed_time' + sys.argv[2])
			plt.show()
			plt.close()

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

plots_dict = {1:1, 2:1, 3:1, 6:1, 7:1, 8:2, 11:2, 12:2, 13:2, 21:2, 22:2, 23:2, 101:1, 104:1, 116:1, 164:1, 165:1, 404:1, 416:1, 464:1, 465:1, 201:3, 202:4, 203:4, 204:3, 205:3, 501:3, 502:4, 503:4, 601:3, 602:4, 603:4, 604:3, 605:3, 801:5, 802:5, 1001:1, 1003:1, 2001:1, 2002:1, 2003:1, 2006:2, 2007:2, 2008:2, 2011:2, 2012:2, 2013:2, 2021:2, 2022:2, 2023:2, 3001:1, 3002:1, 3003:1, 3006:2, 3007:2, 3008:2, 3011:2, 3012:2, 3013:2, 3021:2, 3022:2, 3023:2, 2301:1, 2302:1, 2303:1, 2306:2, 2307:2, 2308:2, 2311:2, 2312:2, 2313:2, 2321:2, 2322:2, 2323:2, 211:4, 214:4, 215:4, 221:4, 224:4, 225:4, 281:4, 284:4, 285:4, 611:4, 614:4, 615:4, 621:4, 624:4, 625:4, 681:4, 684:4, 685:4}

if(len(sys.argv) != 1 and sys.argv[1] == "same"):
	a.plot_same(['Elapsed_Time'], plots_dict)
elif(len(sys.argv) != 1 and sys.argv[1] == "mul"):
	a.plot_mul(['Elapsed_Time'], plots_dict)
elif(len(sys.argv) != 1 and sys.argv[1] == "all"):
	a.plot_all(['Elapsed_Time'], plots_dict)
elif(len(sys.argv) != 1 and sys.argv[1] == "hist"):
	a.plot_all(['Elapsed_Time'], "hist", plots_dict)
else:
	a.plot(['Elapsed_Time'], plots_dict)

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'Context_Switch_Forced', 'Context_Switch'])

#a.plot(['Kernel_Time', 'User_Time', 'Elapsed_Time', 'CPU', 'Context_Switch_Forced', 'Context_Switch', 'Major_Page_Faults', 'Minor_Page_Faults', 'Swapped_Out_From_Main_Memory', 'Maximum_Resident_Set_Size'])



