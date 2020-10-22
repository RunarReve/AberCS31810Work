#!/bin/bash
#Script that sums up all the content of given set studies
#Argv[1] study name
#Argv[2] output 

study="${1}"
out="${2}"
rm ${out}
touch ${out}

echo "${study}"

#Number of objects
numObj=$(grep '>' ${study}/${study}.fa -c)
echo "Number of Objects: ${numObj}"

#Total Lenght
len='0'
for each in $(grep "Length:" ${study}/${study}.fa.stat | awk '{print $2}')
do
	len=$(expr ${len} + ${each})
done 
echo "Total lenght: ${len}"
