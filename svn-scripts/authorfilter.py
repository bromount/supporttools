#!/usr/bin/env python
# Use at own risk script. No guarantee of same results
# This is to be run inside a repo that was checked out, not on the main server
# We are not responsible for any mistakes or issues caused
#
# 
# Usage put it in the repo (or your path) and run:
# svn log --quiet | ./authorfilter.py
#
# Remember to run chmod +x on the file before you use it.
#


import sys
authors = {}
for line in sys.stdin:
    if line[0] != 'r':
        continue
    author = line.split()[2]
    if author not in authors:
        authors[author] = 0
    authors[author] += 1
for author in sorted(authors):
    print author, authors[author]
