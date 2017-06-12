from numpy import power
from numpy import multiply

def execute(*args):
    """Combine the arguments into a polynomial result
    
    @return result of arg1*arg2^arg3 + arg4*arg5^arg6 + arg7*arg8 
    
    """

    result = 0
    
    terms = len(args) / 3
    if len(args) % 3 != 0:
        terms = terms + 1
    
    for i in range(terms):
                
        coefficient = args[i * 3]    
        variable = 1 if i * 3 + 1 >= len(args) else args[i * 3 + 1]
        exponent = 1 if i * 3 + 2 >= len(args) else args[i * 3 + 2]
        
        result += multiply(coefficient, power(variable, exponent))
        
    return result 

def test():
    
    from numpy import array
    
    if not(all(execute(array([1., 2.])) == array([1., 2.]))):
        raise Exception
        
    if not(all(execute(array([1., 2.]), array([3., 4.])) == array([3., 8.]))):
        raise Exception
        
    if not(all(execute(array([1., 2.]), array([3., 4.]), array([5., 6.])) == array([243., 8192.]))):
        raise Exception

    print "Poly Test Complete"