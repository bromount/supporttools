import os
import glob
os.chdir(".")

titles = open("titles.txt","a")

import os
cfiles = []
for root, dirs, files in os.walk('../newhtml'):
  for file in files:
    if file.endswith('.html'):
      cfiles.append(os.path.join(root, file))

print cfiles


for files in cfiles:
	title = open(files, 'r').read().split('<title>')[1].split('</title>')[0].strip()
#	print title

	title_string = files.split(os.sep)[-1] + " = " + title + "\n"

	print title_string

	titles.write(title_string)

titles.close()
