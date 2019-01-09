#!/bin/bash

mkdir dirA dirB
touch -d '01/01/2015' file1
cd dirA
	touch -d '01/01/2015' file2 file3
	mkdir dirC dirE
	cd dirC
		touch -d '01/01/2015' file4 file5
		mkdir dirD
		cd dirD
			touch -d '01/01/2015' file7 file8
			touch file6 file 77
			cd ..
		cd ..
	cd dirE
		touch -d '01/01/2015' file9
		cd ..
	cd ..
cd dirB
	touch file10
	mkdir dirF
	cd dirF
		touch -d '01/01/2015' file11 file12
		mkdir dirG
		cd dirG
			touch -d '01/01/2015' file13
			cd ..
		cd ..
	cd ..

