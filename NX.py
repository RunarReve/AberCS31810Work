#
#Program to get various Ns as in N50
#argv[1] Study name
#argv[2] x in Nx, default set to 50
import sys

N=50
if(len(sys.argv) > 2 and sys.argv[2].isnumeric()):
        N=int(sys.argv[2])
else:
    print("Wrong input or no input given, set to N50")

inn = sys.argv[1] + '/' + sys.argv[1] + '.fa'

contigs = []
#Count all contigs into a list
for each in open(inn, 'r'):
    if (each[0] == '>'):
        continue
    contigs.append(len(each))


#Sort list contigs
contigs.sort(reverse=True)
#print(contigs)

sumLength = sum(contigs)

x = (sumLength /100) *N

index = 0
while x > 0:
    x= x - contigs[index]
    index=index+1

print("N"+str(N) +"\t"+ str(contigs[index-1]))
