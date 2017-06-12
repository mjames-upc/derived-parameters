## @file Laplacian.py

from numpy import empty
from numpy import shape
from numpy import NaN


# Function to calculate the Laplacian of qan.
#
# @param qan: The quantity array. This must be at rank 2, with at least 3
#             cells in the first two dimensions.
# @param dx: The spacing between data points in the X direction.
# @param dy: The spacing between data points in the Y direction.
def execute(qan, dx, dy):

    result = empty(shape(qan), dtype=qan.dtype)
    
    # outer edges can't be calculated: fill with "invalid" value
    result[0,:] = NaN
    result[-1,:] = NaN
    result[1:-1,0] = NaN
    result[1:-1,-1] = NaN
    
    # If dx and dy are matrices, we never use the outer edge,
    # so strip it off so we don't have to use slice notation in the math.
    # If they're actually scalars or 1-element matrices, we can't
    # slice them so don't try. 
    shapedx = shape(dx)
    if len(shapedx) < sum(shapedx):
        dx = dx[1:-1,1:-1]
        
    shapedy = shape(dy)
    if len(shapedy) < sum(shapedy):
        dy = dy[1:-1, 1:-1]

    # Calculate the Q[i,j] + Q[i,j] array.
    twoq = qan[1:-1,1:-1] * 2
    
    # Calculate the X part of the answer
    ans = qan[1:-1,0:-2] + qan[1:-1,2:]
    ans -= twoq
    ans /= dx * dx
    
    # Calculate the Y part of the answer
    term = qan[0:-2,1:-1] + qan[2:,1:-1]
    term -= twoq
    term /= dy * dy
    
    # Combine pieces of the answer
    ans += term 
    
    # fill middle block of result with ans
    result[1:-1,1:-1] = ans
    return result
