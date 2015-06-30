import re
import os
import glob
#f=open('results.txt')
#lines=f.readlines();

#for line in lines:
 #   line=line[3:]


infile = open('./results.txt')
outfile = open('result_new.txt', "w" )
for line in infile:
    outfile.write( line[3:] )
infile.close()
outfile.close()
