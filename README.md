exp3 running for time

exp1, exp3, exp4, exp5 completed(time is not used)

exp6, exp7, exp2 completed

-------------------------------------------------------
Versions:-

4.2	- stable

5.0	- time included

5.2	- exp6, ex7, exp2 completed with time

5.3	- exp3 completed

6.0	- experiments are running with time(1, 8, 51, 53, 56, 58)
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

exp5[x]	- Similar to exp[x] with small_files
