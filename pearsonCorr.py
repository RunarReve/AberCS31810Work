#
#Script for comparing two k-mers of same size with Pearson correlation
#argv[1] file 1
#argv[2] file 2
#argv[3] out append
import sys
from scipy import stats

k = sys.argv[1].split('/')[-1].replace('All','')[-1]
name1 = sys.argv[1].split('/')[-1].split('.')[0]
name2 = sys.argv[2].split('/')[-1].split('.')[0]
fullName = name1 + '_' + name2 + ';K' + k

list1 = []
list2 = []
for each in open(sys.argv[1], 'r'):
    list1.append(float(each.split()[1]))
for each in open(sys.argv[2], 'r'):
    list2.append(float(each.split()[1]))


pear = stats.pearsonr(list1, list2)

out = open(sys.argv[3], 'a')
out.write(fullName+ '\t'+ str(pear[0])+'\t'+str(pear[1])+ '\n')
