from Add import execute as Add
from numpy import multiply, copy

def execute(*args):
    """ Perform scalar or vector subtraction.
    
    """
    diffArgs = list(args)

    if type(diffArgs[0]) == tuple:
        for i in range(1, len(diffArgs)):
            diffArgs[i] = (-diffArgs[i][0], -diffArgs[i][1])
        return apply(Add, diffArgs)
    else:
        result = 0
        result += diffArgs[0]
        for i in range(1, len(diffArgs)):
            result -= diffArgs[i]
        return result