#
import sys
#argv[1] in file
#argv[2] out file

inn = sys.argv[1]
out = sys.argv[2]
outfile = open(out, 'w')
string = ''

for each in open(inn, 'r'):
    if(each[0] == '>'):
        if(string != ''):
            outfile.write(string + '\n')
        outfile.write(each)
        string = ''
    else:
        string = string + each.replace('\n', '')

