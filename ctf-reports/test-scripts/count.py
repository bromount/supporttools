## {{{ http://code.activestate.com/recipes/578197/ (r1)
import os, sys

def main():
    if len(sys.argv) - 1:
        engine(' '.join(sys.argv[1:]))
    else:
        print os.path.basename(sys.argv[0]), '<directory>'

def engine(path):
    directories = files = 0
    for information in os.walk(path):
        directories += len(information[1])
        files += len(information[2])
    print 'Directories =', directories
#    print 'Files =', files


engine('.')

