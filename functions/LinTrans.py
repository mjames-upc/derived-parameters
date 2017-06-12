from Add import execute as Add
from Multiply import execute as Multiply
from numpy import zeros_like, ndarray
 
def execute(*args):
    """Perform a linear transform
    
    @return: result = arg1*arg2 + arg3*arg4 + arg5... 
             vecresult = vec1*sca1 + vec2*sca2 + vec3...
             
    """

    result = None



    if type(args[0]) == tuple:
        zeroArray = zeros_like(args[0][0]) 
        result = (zeroArray, zeroArray.copy())
    else:
        for arg in args:
            if (type(arg) == ndarray):
                result = zeros_like(arg)
                break

    termLength = 2
    
    terms = len(args) / termLength
    if len(args) % termLength != 0:
        terms = terms + 1
    
    for i in range(terms):
        coefficient = args[i * termLength]    
        variable = 1 if i * termLength + 1 >= len(args) else args[i * termLength + 1]
        result = Add(result, Multiply(coefficient, variable))
    
    return result
