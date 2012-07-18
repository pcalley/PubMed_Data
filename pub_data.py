############################################################
#Convert the Pubmed data into json format to be read by the 
#gator.
#Paul Calley
#JBEI
############################################################

import json
import re

###Variable Declaration###################################

#Open the template file as well as the data sets 
#labeled infile##.
infile01 = './TXT/Golgi_curated.txt'
f01 = open(infile01, 'rU')

infile02 = './TXT/Cytosol.txt'
f02 = open(infile02, 'rU')

temp00 = './Template/Template.txt'
t00 = open(temp00, 'rU')

#Specify the output file MASCP.PubmedReader.txt
wo = open('./JSON/MASCP.PubmedReader.txt', 'w')

#Iterator declarations
protein_list=[]
f01_list = []
f02_list = []

###Main Loop Body#########################################

#Set up the iterator lists for t00 and f**
for line in t00:
    line = line.strip('\n')
    protein_list.append(line)

for line in f01:
    line = line.strip('\n')
    line = re.sub(r'\s+',' ', line)
    linelist = line.split(' ')
    f01_list.append(linelist[0].lower())
    f01_list.append(linelist[1].lower())
    f01_list.append(linelist[2].lower())
    f01_list.append(linelist[3].lower())
    f01_list.append(linelist[4].lower())
    f01_list.append(linelist[5].lower())

for line in f02:
    line = line.strip('\n')
    line = re.sub(r'\s+',' ', line)
    linelist = line.split(' ')
    f02_list.append(linelist[0].lower())
    f02_list.append(linelist[1].lower())
    f02_list.append(linelist[2].lower())
    f02_list.append(linelist[3].lower())
    f02_list.append(linelist[4].lower())
    f02_list.append(linelist[5].lower())
    f02_list.append(linelist[6].lower())

#for each agi in t00 if that agi appears in an infile** then 
#add the pubmed code for the publication that has it to the 
#pub_list and add a json entry for the peptide to pep_list.
#then write out the pub_list and pep_list to wo.
for agi in protein_list:
    #Attributes for each protein
    pub_list = []
    pep_list = []

    #Add the contents of f01 to the output file
    if agi in f01_list:
	first_index = f01_list.index(agi)
	for i in range(f01_list.count(agi)):
	    if f01_list[first_index] != agi: print('this is an error')
	    pub_list.append(22430844)     
	    pep_list.append({"publications": "22430844","sequence": f01_list[first_index + 5].upper(), "pep_exp_mz": f01_list[first_index + 1],"pep_exp_mr": f01_list[first_index + 2], "pep_exp_z": f01_list[first_index + 3], "pep_score": f01_list[first_index + 4]})
	    first_index = first_index + 6 
    
    #Add the contents of f02 to the output file
    if agi in f02_list:
	first_index = f02_list.index(agi)
	for j in range(f02_list.count(agi)):
	    if f02_list[first_index] != agi: print('this is an error')
	    pub_list.append(21166475)     
	    pep_list.append({"publications": "21166475","sequence": f02_list[first_index + 5].upper(), "pep_exp_mz": f02_list[first_index + 1],"pep_exp_mr": f02_list[first_index + 2], "pep_exp_z": f02_list[first_index + 3], "pep_score": f02_list[first_index + 4], "model": f02_list[first_index + 6]})
	    first_index = first_index + 7
    
    #write to the output file.
    wo.write(agi.upper() + ',{"publications":'+ str(pub_list) + ',"peptides":' + json.dumps(pep_list) + ',"retrieved":"2012-07-04T00:00:00.000Z"}' + '\n')
    

###Subroutines################################################


t00.close()
f01.close()
f02.close()
wo.close()
