#
#argv[1]
#argv[2]
import sys

def ACGT2num(ACGT):
    if(ACGT == 'A'):
        return 0
    elif(ACGT == 'C'):
        return 1
    elif(ACGT == 'G'):
        return 2
    else: #In case it is a U and not a T, Trust the file do not have any other anomolies
        return 3

inn = sys.argv[1]
out = sys.argv[2]
outfile = open(out, 'w')

for each in open(inn, 'r'):
    if(each[0] == '>'):
        outfile.write(each)
    else:
        tot = 0 
        ACGT = [0,0,0,0] #Array to store the amount of each SNP in the forloop 
        for SNP in each: 
            x = ACGT2num(SNP)
            tot = tot + 1
            ACGT[x] = ACGT[x] + 1 
        outfile.write("\tLength: " + str(tot) + "\n"
                + "\tA: " + str(ACGT[0]) + ',' + format(ACGT[0]/float(tot)*100,'.2f')+'%\n'
                + "\tC: " + str(ACGT[1]) + ',' + format(ACGT[1]/float(tot)*100,'.2f')+'%\n'
                + "\tG: " + str(ACGT[2]) + ',' + format(ACGT[2]/float(tot)*100,'.2f')+'%\n'
                + "\tT: " + str(ACGT[3]) + ',' + format(ACGT[3]/float(tot)*100,'.2f')+'%\n'
                + "\tGC-Content: " + format(((ACGT[1]+ACGT[2])/float(tot))*100,'.2f')+'%\n'
                )
        
        
