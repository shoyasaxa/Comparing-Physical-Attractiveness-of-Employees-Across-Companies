import shutil
import os 

root = 'C:/Users/Shoya/Aphrodite/CFD Images/'

for subdir, dirs, files in os.walk(root):
    for directory in dirs:
    	for file in os.listdir(root+directory):
    		if (file != ".DS_Store"):
    			shutil.move(root+directory+"/"+file, root+"All Images/"+file)
    		else:
				print("ignore")
    break
