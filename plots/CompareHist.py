import os

exp = input("Enter experiment code : ").split()

for i in exp:
	os.system('python3 Histogram.py bigbang ' + i + " max&")


