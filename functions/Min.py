#    SOFTWARE HISTORY
#    
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    18 Feb 2010     #4502         jelkins        Initial Creation.

from numpy import array, nanmin

def execute(*args):
    """ Return the min value at each grid point
    
    @param args
                a list of grids or a single 3D grid. If a single 3D variable is passed in, 
                will compute without considering the vertical coordinate information. 
    """
    
    if len(args) == 1 and isinstance(args[0], list):
        if len(args[0]) == 2 and len(args[0][0].shape) == 3:
            # we have been passed 3D data
            return nanmin(args[0][0], 0)
        else:
            return execute(*args[0])
    else:
        return nanmin(array(list(args)), 0)