#def convert(s):
#    '''Convert to an integer.'''
#    try:
#       return int(s)
#       #print('Conversion succeeded! x =', x)
#    except (ValueError, TypeError):
#       #print('Conversion failed!')
#       #x = -1    
#        pass
#    return -1

import sys
def convert(s):
    '''Convert to an integer.'''
    try:
       return int(s)
       #print('Conversion succeeded! x =', x)
    except (ValueError, TypeError) as e:
       print('Co ty robisz! Conversion error: {}'\
              .format(str(e)), file=sys.stderr)
       #x = -1 
       raise
      

from math import log

def string_log(s):
    v = convert(s)
    return log(v)
