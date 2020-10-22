#
#argv[1] study name 
import sys

study = sys.argv[1]
out = study + '/' + study + '.sum' 

totObj = 0
totLen = 0
totA   = 0
totC   = 0
totG   = 0
totT   = 0

stat = study + '/' + study + '.stat'
for each in open(stat, 'r'):
    if(each[0] == '>'):
        totObj = totObj + 1
        continue
    numb = each.split(': ')[-1].split(',')[0]
    if("Length:" in each):
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

#Print all 
outfile = open(out, 'w')
outfile.write(
    study + '\n'+
    "Number of objects: " + str(totObj) + '\n'+
    "Total Lenght: " + str(totLen) + '\n'+
    "Total A: " + str(totA) + '\n'+
    "Total C: " + str(totC) + '\n'+
    "Total G: " + str(totG) + '\n'+
    "Total T: " + str(totT) + '\n'+
    "GC-Content: " + str(GC) + '%\n'
    )
