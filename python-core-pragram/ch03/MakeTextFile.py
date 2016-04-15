#!/usr/bin/env python

'create a text file and input some data'

import pdb
import os

#pdb.set_trace() 
def input_filename():
    'Let user input a filename which not exsists'
    while True:
        name = raw_input('file-name:\n>')
        if os.path.exists(name):
            print "*** ERROR: '%s' already exists" % name
        else:
            return name

def input_data():
    'get user input util . charactor'
    all = []
    print 'input file data:'
    while True:
        entry = raw_input('> ')
        if entry == '.':
            return all
        else:
            all.append(entry)
           
def main():
    'main function'

#    pdb.set_trace()    
    print('START:')
    fname = input_filename()
    fdata = input_data()
    
    fobj = open(fname, 'w')
    fobj.write('\n'.join(fdata))
    fobj.close()
    print('DONE')
if __name__ == '__main__':    
#    pdb.set_trace()  
    main()  
