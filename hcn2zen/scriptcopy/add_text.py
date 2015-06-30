import shutil
import os
import glob
all_files =  glob.glob("*.html")

new_text = """
<meta name="prodname" content="TeamForge"/>
<meta name="version" content="7.2"/>
<meta name="release" content=""/>
"""

for oldfile in all_files:
    print oldfile
    with open(oldfile) as f_old:
	with open('new' + oldfile, "w") as f_new:
	        for line in f_old:
	            f_new.write(line)
	            if 'content="en-us"/>' in line:
	                f_new.write(new_text)
    os.remove(oldfile)

all_files =  glob.glob("*html")


for oldfile in all_files:
    print oldfile
    with open(oldfile) as f_old:
        newname = oldfile.replace("new",'')
        with open(newname, "w") as f_new:
                for line in f_old:
                    f_new.write(line)
    os.remove(oldfile)

