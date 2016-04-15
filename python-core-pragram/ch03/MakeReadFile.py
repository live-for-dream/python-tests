#!/usr/bin/env python

'Read a text file and output those data'

import os
#import MakeTextFile

def myRead(filename):
    'read from File and output to stdout'
    try:
        fobj = open(filename, 'r')
    except IOError, e:
        print"*** file open error:", e
    else:
        for eachLine in fobj:
            print eachLine,
        fobj.close()

def main():
    filename = raw_input('input filename: ')
    myRead(filename)

main()