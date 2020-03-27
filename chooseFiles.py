import csv,os, re,sys
from shutil import copy2
rows = []
with open('470ID.csv',newline='') as inputfile:
    for row in csv.reader(inputfile):
        rows.append(row[0])

#print(rows)
allImages = "/mnt/c/Users/karat/Documents/Capstone/Images/"
output = "/mnt/c/Users/karat/Documents/Capstone/CompleteSet/"
dirs = os.listdir(allImages)
filename = []
for file in dirs:
    if re.search('.nii',file):
        filename += [file]

for root,d,f in os.walk(allImages):
    for file in filename:
        if rows.count(file[4:12]) == 1:
            copy2(os.path.join(root,file),output)
        
