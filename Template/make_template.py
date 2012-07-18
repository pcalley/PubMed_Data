import json
import re

filename = './TXT/MASCP.PpdbReader-11-10-04.txt'

fo = open(filename, 'rU')
wo = open('./TXT/Template.txt', 'w')


for line in fo:
    line = line.strip('\n')
    line = re.sub(',', ' ', line)
    linelist = line.split(' ')
    wo.write(linelist[0] + '\n')

fo.close()
wo.close()
