#!/usr/bin/python

'''
Created on Dec 10, 2014

@author: sombeet_sahu
Version 1.0

Usage: folder_struct.py [options] folderpath

Options:
--version             show program's version number and exit
  -h, --help            show this help message and exit
  -count folderpath

    
e.g. folder_Struct.py -count /home/ionadmin/sombeet/files

'''

import filecmp
import os.path

def are_dir_trees_equal(dir1, dir2):
    """
    author:sahus3
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: True if the directory trees are the same and
        there were no errors while accessing the directories or files,
        False otherwise
   """


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
        if not are_dir_trees_equal(new_dir1, new_dir2):
            return False
    return True





def main():
    # DIR = os.path.dirname(os.path.realpath(__file__))
    DIR = "C:\Program Files\DellTPad\Data\Cur"
    DIR2 = "C:\Program Files\DellTPad\Data\Cur"
    dr = are_dir_trees_equal(DIR, DIR2)
    print dr


if __name__ == '__main__':
    main()

