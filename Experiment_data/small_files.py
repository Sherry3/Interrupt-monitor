import os

for i in range(10000):
	if(i % 1000 == 1):
		print(i)
	os.system("cat demo.txt > /media/sourabh/SHERRY/Small/file" + str(i) + ".txt")
