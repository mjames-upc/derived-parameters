## @file IsenStability.py
from numpy import NaN
from numpy import isnan
from numpy import maximum
from numpy import shape


# Calculate the isentropic stability through a layer.
#
# @param p_up: Pressure on upper isentrope (mb)
# @param p_lo: Pressure on lower isentrope (mb)
# @param o_up: Upper isentrope (K)
# @param o_lo: This (lower) isentrope (K)
# @return: Isentropic stability array through layer
# @rtype: numpy array
def execute(p_up, p_lo, o_up, o_lo):
    "Calculate the isentropic stability through a layer."
    
    # protect against divide-by-zero errors
    o_diff = o_up - o_lo
    
    dth = 1.0 / o_diff
    
    # calculate stability [maximum() is elementwise]
    p_diff = p_lo-p_up
    stab = maximum(p_diff, 10.0) * dth
    # maximum(NaN,X) is X. Restore the NaNs.
    if shape(p_diff) == ():
        if isnan(p_diff):
            stab = NaN
    else:
        stab[isnan(p_diff)] = NaN
    return stab
        
