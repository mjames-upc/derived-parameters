import numpy
from numpy import zeros

def execute(values, *mappings):
    tmp = zeros(values.shape, 'float32')
    
    size = len(mappings)
    i = 0
    while i < size:
        checkFor = mappings[i]
        i += 1
        setTo = mappings[i]
        i += 1
        tmp[values == checkFor] = setTo
    return tmp



       
