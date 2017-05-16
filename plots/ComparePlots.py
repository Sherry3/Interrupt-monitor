import os

exp = input("Enter input experiments : ").split()
plot = input("Enter plots : ").split()
scope = input("Enter readme_plot scope(local/global) : ")

for i in exp:
	for j in plot:
		os.system('python3 Plot.py ' + i + " " + j + " " + scope + " &")


