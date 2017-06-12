from numpy import multiply
import Vector

def execute(*args):
    """ Perform multiplication of any number of scalars or of a vector and a scalar.
    
    """
    
    if type(args[0]) == tuple:
        return vectorMultiply(args)
    else:
        return scalarMultiply(args)
    
def scalarMultiply(args):
    return reduce(multiply, args)

def vectorMultiply(args):
    return Vector.componentsTo(scalarMultiply((args[0][0],  args[1])), scalarMultiply((args[0][1],  args[1])))
    