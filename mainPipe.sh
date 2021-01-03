#!/bin/bash
#This is the main pipeline that starts all the scripts and programs for this project

for each in $(ls origin/*.fa |sed -e 's/\// /g' | awk '{print $2}')
do
	#Make file locations
	dir=$(echo "${each}" | sed -e 's/\./ /g' | awk '{print $1}' )
	echo "${dir}"
	rm $dir -rf
	mkdir $dir

	#Preprosess the format to make sure each string is on one line
	python rmNewLine.py origin/${each} ${dir}/${each} 

	#Makes a stat *.stat file with stats of the individual strand
	python stats.py ${dir}/${each} ${dir}/${dir}.stat

	#Sum up the whole study/file
	python3 filesum.py ${dir}


	#Run K-mers with 1 to 4
	python kMers.py ${dir} 1
	python kMers.py ${dir} 2
	python kMers.py ${dir} 3
	python kMers.py ${dir} 4

	#Run NX for each study
	touch ${dir}/${dir}.Nx
	for N in 10 20 30 40 50 60 70 80 90
	do
		python3 NX.py ${dir} ${N} >> ${dir}/${dir}.Nx
	done

done

