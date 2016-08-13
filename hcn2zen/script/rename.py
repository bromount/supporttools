import glob
import shutil
all_files =  glob.glob("*html")


for oldfile in all_files:
    print oldfile
    with open(oldfile) as f_old:
	newname = oldfile.replace("new",'')
	with open(newname, "w") as f_new:
	        for line in f_old:
	            f_new.write(line)
    shutil.move(oldfile,"old")		
