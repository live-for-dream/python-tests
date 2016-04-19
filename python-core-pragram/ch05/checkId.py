#!/usr/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits
            
alphas = string.letters + '_'
nums = string.digits
            
def check_id():
    print 'Welcome to the Identifier Checker v1.0'
    print 'Testees must be at least 2 chars long.'
    
    inp = raw_input('input Identifier to test? \n> ')
    
    if len(inp) > 1:
    
        if inp[:1] not in alphas:
            print '''invalid: first symbol must be
    	  alphabetic'''
        else:
            for otherChar in inp[1:]:
    
                if otherChar not in alphas + nums:
                    print '''invalid: remaining
    		  symbols must be alphanumeric'''
                    break
            else:
                print "okay as an identifier"
    
    return inp
#    return 'q'

def main():
    while True:
        input = check_id()
        if input[:1] == 'q':
            return 0

main()