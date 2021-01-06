#!/bin/bash
#This is the main pipeline that starts all the scripts and programs for this project

#Change list for k in k-mers
numbN="1 2 3 4"

for each in $(ls origin/*.fa |sed -e 's/\// /g' | awk '{print $2}')
do
	break
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
	mkdir ${dir}/kmer/
	mkdir ${dir}/plot/
	for N in ${numbN}
	do
		echo "${N}"
		python kMers.py ${dir} ${N}
		R/Kmers.R ${dir}/kmer/${dir}.k${N}All ${dir}/plot/${dir}.k${N}.png "${dir} K${N}"
	done

	#Run NX for each study
	touch ${dir}/${dir}.Nx
	for N in 10 25 33 50 66 75 90
	do
		python3 NX.py ${dir} ${N} >> ${dir}/${dir}.Nx
	done

done


#Spearman correlation on all
echo "Study1_Study2	correlation	p-value" > pearsonCorr.tsv
for each in $(ls origin/*.fa |sed -e 's/\// /g'|awk '{print $2}'|sed -e 's/.fa//g')
do
	echo "${each}"
	for beach in $(ls origin/*.fa |sed -e 's/\// /g'|awk '{print $2}'|sed -e 's/.fa/ /g')
	do
		if [ "$each" = "$beach" ]
		then
			continue
		fi
		for N in ${numbN}
		do
			echo "${N}"
			#TODO could be optimized by running a loop insitde the python program
			python pearsonCorr.py ${each}/kmer/${each}.k${N}All ${beach}/kmer/${beach}.k${N}All pearsonCorr.tsv
		done
	done
done
sort -gk2r pearsonCorr.tsv > pearsonCorr2.tsv
mv pearsonCorr2.tsv pearsonCorr.tsv

