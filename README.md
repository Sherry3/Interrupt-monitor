
exp1, exp2, exp3, exp6, exp7, exp8 completed

exp101, exp104, exp116, exp164, exp165 completed

exp201, exp404, exp416, exp464, exp465 completed

exp202, exp203, exp501, exp502, exp503 completed

exp601, exp602, exp603 completed

exp801, exp802 completed

exp1001, exp1003 completed

exp204, exp604, exp11, exp13, exp21, exp23 completed

exp12, exp22, exp205, exp605 completed

exp2001, exp2003, exp2006, exp2008, exp2011, exp2013, exp2021, exp2023 completed

exp3001, exp3003, exp3006, exp3008, exp3011, exp3013, exp3021, exp3023 completed

exp3002, exp3007 exp3012, exp3022, exp2002, exp2007 exp2012, exp2022 completed

exp2302, exp2307, exp2312, exp2322 completed

exp2301, exp2303, exp2306, exp2308, exp2311, exp2313, exp2321, exp2323 completed

200 and 600 series without isolation completed

200 and 600 series with isolation completed

Project closed
-------------------------------------------------------
Versions:-

4.2	- stable

5.0	- time included

5.2	- exp6, ex7, exp2 completed with time

5.3	- exp3 completed

6.0	- experiments completed with time(1, 8)
	- Introduced (51, 52, 53, 56, 57, 58)
	- Started (101, 104, 116, 164)

6.1	- 101, 104, 116, 164, 165 completed
	- 201, 404, 416, 464, 465 running

6.2	- 201, 404, 416, 464, 465 completed

6.3	- running 202, 203, 501, 502, 503	
	- Underclocked CPU

7.0	- partial results of 202, 203, 501, 502, 503
	- Underclocked cpu not working

7.1	- Seaperate folder for logs removed
	- monitor2() removed
	- Underclocked cpu not working
	- 202, 203, 501, 502, 503 completed
	- running 601, 602, 603

7.2	- Underclocked cpu worked
	- 601, 602, 603 completed

7.3	- 801, 802 completed

8.0	- 1001, 1003 completed
	- 204, 604, 11, 13, 21, 23 completed
	- 12, 22 running

8.1	- 12, 22, 205, 605 completed

9.0	- 2001, 2003, 2006, 2008, 2011, 2013, 2021, 2023 completed
	- 3001, 3003, 3006, 3008, 3011, 3013, 3021, 3023 running

9.1 	- 3001, 3003, 3006, 3008, 3011, 3013, 3021, 3023 completed
	- 3002, 3007, 3012, 3022, 2002, 2007, 2012, 2022 completed
	- Time_Plot.py merged with Histogram.py

10.0	- 2302, 2307, 2312, 2322 completed
	- 2301, 2303, 2306, 2308, 2311, 2313, 2321, 2323 completed

10.1	- Gone through each readme file to find errors
	- 3008, 8 was wrong, deleted
	- 3008, 8 completed
	- 2002, 2302 was wrong, deleted
	- 2002, 2302 completd
	- 200 and 600 series running without isolation

11.0	- 200 and 600 series without isolation completed
	- 200 and 600 series with isolation completed
-------------------------------------------------------

exp1	- irqbalance off
	- big files
 
exp2	- irqbalance off
	- core 3 isolated
	- all interrupts to core 3 
	- big files

exp3	- irqbalance off
	- all interrupts to core 3 
	- big files

exp11	- irqbalance off
	- big files
	- stress 1 cores for 500s

exp12	- irqbalance off
	- big files
	- core 3 isolated
	- all interrupts to core 3
	- stress 1 cores for 500s

exp13	- irqbalance off
	- all interrupts to core 3 
	- big files
	- stress 1 cores for 500s

exp21	- irqbalance off
	- big files
	- stress 2 cores for 500s

exp22	- irqbalance off
	- big files
	- core 3 isolated
	- all interrupts to core 3
	- stress 2 cores for 500s

exp23	- irqbalance off
	- all interrupts to core 3 
	- big files
	- stress 2 cores for 500s

exp6	- equivalent to exp4 with time
	- irqbalance off
	- all interrupts to core 3 
	- big files
	- stress 8 cores for 500s

exp7	- equivalent to exp5 with time
	- irqbalance off
	- core 3 isolated
	- all interrupts to core 3 
	- big files
	- stress 8 cores for 500s

exp8	- irqbalance off
	- stress 8 cores for 500s
	- big files
 
exp5[x]	- Similar to exp[x] with small_files

exp[2000]	- Similar to exp[x] with hdd_to_hdd

exp[2300]	- Similar to exp[x] with underclock and hdd_to_hdd

exp[3000]	- Similar to exp[x] with underclock

exp101	- 1G of stress on harddisk

exp104	- 4G of stress on harddisk

exp116	- 16G of stress on harddisk

exp164	- 64G of stress on harddisk

exp165	- 128G of stress on harddisk

exp404	- 4G of stress on harddisk with 8 threads

exp416	- 16G of stress on harddisk with 8 threads

exp464	- 64G of stress on harddisk with 8 threads

exp465	- 128G of stress on harddisk with 8 threads

exp201	- irqbalance off
	- multiple big files

exp202	- irqbalance off
	- multiple big files
	- stress 10 cores

exp203	- irqbalance off
	- multiple big files
	- stress 50 cores

exp204	- irqbalance off
	- multiple big files
	- all interrupts to core 3 

exp205	- irqbalance off
	- multiple big files
	- all interrupts to core 3 
	- isolated core 3

exp503	- irqbalance off
	- multiple big files
	- stress 50 cores
	- cpu_frequency(didn't worked)

exp601	- irqbalance off
	- multiple big files
	- cpu_frequency(worked)

exp602	- irqbalance off
	- multiple big files
	- stress 10 cores
	- cpu_frequency(worked)

exp603	- irqbalance off
	- multiple big files
	- stress 50 cores
	- cpu_frequency(worked)

exp604	- irqbalance off
	- multiple big files
	- cpu_frequency(worked)
	- all interrupts to core 3 

exp605	- irqbalance off
	- multiple big files
	- cpu_frequency(worked)
	- all interrupts to core 3 
	- isolated core 3

exp801	- irqbalance off
	- multiple big files(4)
	- stress 10 cores

exp802	- irqbalance off
	- multiple big files(4)
	- stress 10 cores
	- cpu_frequency(worked)

