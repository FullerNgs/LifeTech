#!/usr/bin/python

'''
Created on Dec 10, 2014

@author: sombeet_sahu
Version1.0

Usage: folder_struct.py [options] folderpath

Options:
--version             show program's version number and exit
  -h, --help            show this help message and exit
  -count folderpath

    
e.g. folder_Struct.py -a /home/ionadmin/sombeet/files

'''
from optparse import OptionParser
import re
import json
import os
import os.path


def readTxt( txtFile ):
    try:
        jsn = dict()
        with open(txtFile, 'r') as f:
            content = f.readlines()
            f.close()
        for line in content:
            if " = " in line:
                key, value = line.rstrip().split(' = ')
                jsn[key] = value
        return jsn
    except:
        print "Error: can\'t find file or read data"
        return None

def parsePath( txtFile ):
    try:
        jsn = dict()
        with open(txtFile, 'r') as f:
            content = f.readlines()
            f.close()
        for line in content:
            if " = " in line:
                key, value = line.rstrip().split(' = ')
                jsn[key] = value
        return jsn
    except:
        print "Error: can\'t find file or read data"
        return None


def main():
    parser = OptionParser(usage="usage: %prog [options] filename", version="%prog 1.0")
    parser.add_option("-c", action="store", dest="readFolderCount", help="Required for testing folder structure.")

    
    options, args = parser.parse_args()
    option_dict = vars(options)
    val = [ v for v in option_dict.values() if v is not None]

    if len(val) < 1:
        parser.error("wrong number of arguments. Please use -h option")


    
    #############################################################
    # Folder Structure Comparison from BaseLine Analysis: Count #
    #############################################################

    if options.readFolderCount:
        beadSummary = readTxt(options.readFolderCount)
        if beadSummary and not len(beadSummary) == 0:
          #  print len([name for name in os.listdir('.') if os.path.isfile(name)])
          DIR = os.path.dirname(os.path.realpath(__file__))
            #DIR = 'C:/Users/sahus3/Desktop/BaseLine_Comparision_Script/'
    print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    
if __name__ == '__main__':
    main()
