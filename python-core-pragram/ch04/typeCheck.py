#!/usr/bin/env python
'check number types and display'

def deisplayType(num):
    print num, 'is'
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type ', type(num).__name__
    else:
        print 'Not a number at all'

deisplayType(-5.2+1.9j)
deisplayType(9999999999999999999999L)
deisplayType(1)
deisplayType(1.1)