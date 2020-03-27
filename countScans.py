import csv,os, re,sys
from shutil import copy2
rows = []
with open('221IDs.csv',newline='') as inputfile:
    for row in csv.reader(inputfile):
        item = (row[0][0:8],row[0][12:17],0)
        rows.append(item)


print(rows)
allImages = "/home/tncolli3/OASIS3/Images/input/"
output = "/home/tncolli3/OASIS3/Images/221Input/"
dirs = os.listdir(allImages)
filename = []
i = 0
for file in dirs:
    if re.search('.nii',file):
        filename += [file]

for root,d,f in os.walk(allImages):
    for scan in rows:
        x = scan[2]
        for file in filename:
            if scan[0] == file[4:12]:
                if scan[1] == file[17:22]:
                    copy2(os.path.join(root,file),output)
        rows[i] = (scan[0],scan[1],x)
        i += 1

for item in rows:
    if item[2] == 0:
        print(item)
