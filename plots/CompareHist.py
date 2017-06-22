import os
import sys

for i in sys.argv[1:]:
	os.system('python3 Histogram.py all ' + i + " test1&")
	os.system('python3 Histogram.py all ' + i + " test2&")


