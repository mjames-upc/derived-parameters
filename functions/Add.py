from numpy import add,array,zeros_like

import Vector

def execute(*args):
    """ Perform scalar or vector addition
    
    """
    if len(args) == 1 and isinstance(args[0], list):
        return execute(*args[0])
    elif isinstance(args[0], tuple):
        return vectorAddition(args)
    else:
        return scalarAddition(args)
    
def scalarAddition(args):    
    return reduce(add, args)

def vectorAddition(args):
    uResult = zeros_like(args[0][0])
    vResult = zeros_like(args[0][0])
    
    for u, v in args:
        uResult += u
        vResult += v
    
    return Vector.componentsTo(uResult, vResult)
