# 
#argv[1] study name
#argv[2] Number of K-mers
import sys

#Function to create K-mers list
def getKList(k,word):
    alp = 'A T G C' 
    if(k <= 0):
        return word

    lis = ''
    for each in alp.split(' '):
        lis = lis + getKList(k-1, word+each ) + ' '

    return lis[:-1]


k=int(sys.argv[2])
kList= getKList(k, '').split(' ')

study = sys.argv[1]


out = open(study + '/'+study+'.k'+str(k) , 'w')
outNorm = open(study + '/'+study+'.k'+str(k)+'N' , 'w')


for each in open(study+'/'+study+'.fa'):
    if (each[0] == '>'):
        out.write(each)
        outNorm.write(each)
        continue
    lis = ''
    lisN = ''
    length = len(each)
    for kk in kList:
        lis = lis  + str(each.count(kk)) +'\t'
        lisN = lisN  + format(each.count(kk)/float(length),'.2f') +'\t'

    out.write('\t'.join(kList)+'\n')
    out.write(lis+'\n')

    outNorm.write('\t'.join(kList)+'\tLength\n')
    outNorm.write(lis+' '+str(length)+'\n')
