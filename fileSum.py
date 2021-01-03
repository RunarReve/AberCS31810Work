#
#argv[1] study name 
#TODO add longes contig
#TODO add shortest contig 
#TODO add standard deviation og GC-content 
#TODO add Mean codon length 
import sys
import statistics

study = sys.argv[1]
out = study + '/' + study + '.sum' 

totObj = 0
totLen = 0
totA   = 0
totC   = 0
totG   = 0
totT   = 0
codonList = []

stat = study + '/' + study + '.stat'
for each in open(stat, 'r'):
    if(each[0] == '>'):
        totObj = totObj + 1
        continue
    numb = each.split(': ')[-1].split(',')[0]
    if("Length:" in each):
        codonList.append(int(numb))
        totLen = totLen + int(numb)
    elif("A:" in each):
        totA = totA + int(numb)  
    elif("C:" in each):
        totC = totC + int(numb)
    elif("G:" in each):
        totG = totG + int(numb)
    elif("T:" in each):
        totT = totT + int(numb)

#GC-content 
GC = format((totG + totC)/float(totLen)*100 ,'.2f')

if(len(codonList) == 1): #Simple fix if only one scaffold for calculations
    codonList.append(codonList[0])

#Print all 
outfile = open(out, 'w')
outfile.write(
    study + '\n'+
    "Numb scaffolds:\t" + str(totObj) +
    "\nTotal Lenght:\t" + str(totLen) +
    "\nLongest:\t" + str(max(codonList)) +
    "\nShortest:\t" + str(min(codonList)) +
    "\nAvrg length:\t" +  format(statistics.mean(codonList) , '.0f') +
    "\nStd.Dev:\t" +         format(statistics.stdev(codonList), '.0f') +
    "\nTotal A:\t" + str(totA) + 
    "\nTotal C:\t" + str(totC) + 
    "\nTotal G:\t" + str(totG) + 
    "\nTotal T:\t" + str(totT) + 
    "\nGC-Content:\t" +str(GC) + '%\n'
    )
