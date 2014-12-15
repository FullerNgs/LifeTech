#!/usr/bin/python

'''
Created on Dec 10, 2014

@author: sombeet_sahu

Usage: folder_struct.py
e.g. folder_Struct.py /home/ionadmin/sombeet/files /home/ionadmin/sombeet/files2

Options:
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path     #CURRENTLY HARDCODED
    @param dir2: Second directory path

    Prints if the file tree is same and  there were no errors while accessing the directories or files

'''

import filecmp
import os.path

def compare_directory(dir1, dir2):

    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0 or len(dirs_cmp.right_only)>0 or \
        len(dirs_cmp.funny_files)>0:
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(
        dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not compare_directory(new_dir1, new_dir2):
            return False
    return True





def main():
    # DIR = os.path.dirname(os.path.realpath(__file__))
    DIR = "C:\Users\sahus3\Desktop\dat1"
    DIR2 = "C:\Users\sahus3\Desktop\dat2"
    dr = compare_directory(DIR, DIR2)
    #print dr

    if dr is True:
        print "The files are same in both directories"
    else:
        print "The file tree do not match in the directories"


if __name__ == '__main__':
    main()

