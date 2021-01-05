#
#Simple script to transform a tsv to latex tabularx format
import sys

out = open(sys.argv[1]+'.tabular', 'w')

for each in open(sys.argv[1], 'r'):
    #print(each.replace('\t', ' & ').replace('\n', ' \\\\ \n'))
    out.write(each.replace('\t', ' & ').replace('\n', ' \\\\ \n'))
    
