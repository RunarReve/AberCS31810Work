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
	python stats.py ${dir}/${each} ${dir}/${each}.stat

	#Sum up the whole study/file
	./filesum.sh ${dir} ${dir}/${dir}.sum 
done

