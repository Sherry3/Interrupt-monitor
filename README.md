
exp1, exp2, exp3, exp6, exp7, exp8 completed
exp101, exp104, exp116, exp164, exp165 completed

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

6.2	- 
-------------------------------------------------------

exp1	- irqbalance off
	- big files
 
exp2	- irqbalance off
	- core 3 isolated
	- all interrupts to core 3 
	- big files

exp5	- irqbalance off
	- core 3 isolated
	- all interrupts to core 3 
	- big files
	- stress 8 cores for 500s

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

