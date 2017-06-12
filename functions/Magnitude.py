# ----------------------------------------------------------------
# Calculate magnitude
# ----------------------------------------------------------------
from numpy import hypot

def execute(*args):
    """ Return the magnitude of a given vector or vector components
    
    """
    
    if type(args[0]) == tuple:
        return hypot(args[0][0], args[0][1])
    else:
        return hypot(args[0], args[1])