#
#    
#     SOFTWARE HISTORY
#    
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    01/19/12        DR14296        M. Huang      Flipped result by applying -1
# 
#

from numpy import power
from LvlQvec import calculate as lvlQvec

def execute(GHxSM, TxSM, P, dx, dy, coriolis):
    slqx, slqy, dtdx, dtdy  = lvlQvec(GHxSM, TxSM, P, dx, dy, coriolis)
    
    # Compute the temperature to potential temperature ratio for this level.
    t2th = power(1000/P, 0.286)
    t2th *= 2
    
    # Now calculate the QG frontogensis function for this level.
    # Fgen = 2(Qx * d(theta)/dx + Qy * d(theta)/dy)
    result = slqx * dtdx
    result -= slqy * dtdy
    result *= t2th
    
    return result  
