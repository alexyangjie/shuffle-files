#!/usr/bin/python3
# Shuffle Files Utility
# v0.0.1
# Copyright Alex Yang

import sys, os
from os import path
from random import randint

def main():
    if len(sys.argv) == 1: 
        directory = '.'
    elif len(sys.argv) > 2: 
        print('Illegal arguments. You have {} arguments. Please only contains the file directory.'.format(len(sys.argv)))
        exit()
    else: 
        directory = sys.argv[1]
    shuffle_files(directory)

def shuffle_files(directory):
    directory = os.path.abspath(directory)
    print('Do you want to shuffle all files in {}? Yes/No'.format(directory))
    proceed = input('> ')
    if proceed == 'Yes':
        usedname = set()
        usedname_add = usedname.add
        for file in os.listdir(directory):
            if path.isfile(os.path.join(directory, file)):
                filename, extension = os.path.splitext(file)
                newname = ''
                success = False
                while not success:
                    tmpname = randint(1000000000, 9999999999)
                    if not (tmpname in usedname or usedname_add(tmpname)):
                        newname = str(tmpname)
                        success = True
                    else:
                        success = False
                print('Renaming {} to {}'.format(file, newname + extension))
                os.rename(os.path.join(directory, file), os.path.join(directory, newname + extension))
            else:
                print('{} is not a file.'.format(os.path.join(directory, file)))
    else:
        print('Operation aborted.')
        exit()

if __name__ == "__main__": main()