#! /usr/bin/env python

import os
import shutil
  
def read_logfile():
    """ read the existing latest build number from the log file """
    
    file_read = open('build_num.txt', 'r')

    build_num = file_read.read();

    file_read.close()
    return build_num

def write_logfile(build_num):
    file_write = open('build_num.txt', 'w')
    file_write.write(build_num)
    file_write.close()
    
def copy_file():
 
    rootPath = '//panda.autodesk.com/BRE_MASTERS_UNL/AutoCAD/Longbow/px86/'
    subdir = '.acad.unl.px86'
    LongbowBuildChar = 'J'
    buildnum = read_logfile();

    directory = rootPath + LongbowBuildChar + buildnum + subdir
    filename = directory + '/' + 'J039.acad.unl.px86.md5'
    dir_target = '//shacnd10877j3/Shared'
    
    if os.path.exists(directory):
        print (directory)
        shutil.copy(filename, dir_target)
        write_logfile(buildnum + '1')
    else:
        print ("No such directory")

# Run the main function
copy_file()
