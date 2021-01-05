# 
#argv[1] study name
#argv[2] Number of K-mers
import sys
from operator import add

#Function to create K-mers list
def getKList(k,word):
    alp = 'A T G C' 
    if(k <= 0):
        return word

    lis = ''
    for each in alp.split(' '):
        lis = lis + getKList(k-1, word+each ) + ' '

    return lis[:-1]


study = sys.argv[1]
k=int(sys.argv[2])
kList= getKList(k, '').split(' ')


out = open(study + '/kmer/'+study+'.k'+str(k) , 'w')
outNorm = open(study + '/kmer/'+study+'.k'+str(k)+'N' , 'w')
outFull = open(study + '/kmer/'+study+'.k'+str(k)+'All' , 'w')

scaffList = [0]*len(kList) #store all scaffolds at once
ksumsum = 0
for each in open(study+'/'+study+'.fa'):
    if (each[0] == '>'):
        out.write(each)
        outNorm.write(each)
        continue
    lis = ''
    lisN = ''
    kSum = 0 #The sum off all ks found
    
    for kk in kList:
        lis  = lis  + str(each.count(kk)) +'\t'
        kSum = kSum + each.count(kk)

    lisN = [str(int(x)/float(kSum)) for x in lis[:-1].split('\t')]

    out.write('\t'.join(kList)+'\n')
    out.write(lis+'\n')

    outNorm.write('\t'.join(kList)+'\tKmerCount\n')
    outNorm.write('\t'.join(lisN) +'\t' + str(kSum)+'\n')

    ksumsum = ksumsum + kSum
    scaffList = map(add, scaffList, list(map(int, lis.split('\t')[:-1])))

#Output the sum of all scaffolds
scaffList2 = [str(x/float(ksumsum)) for x in scaffList]
for x in range(len(scaffList2)):
    outFull.write(kList[x] + '\t' + scaffList2[x]+ '\n')

