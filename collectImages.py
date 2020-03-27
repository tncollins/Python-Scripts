import os, shutil

#Root directory of .nii.gz images
searchDir = "/home/tncolli3/OASIS3/Images/NIIfiles/"

#Output director for .nii images
outputDir = "/home/tncolli3/OASIS3/Images/input/"

for root, dirs, files in os.walk(searchDir):
    for file in files:
        if file.endswith(".nii") or file.endswith(".gz"):
            shutil.move(os.path.join(root, file), outputDir)

os.system("gunzip " + outputDir + "*.nii.gz")
