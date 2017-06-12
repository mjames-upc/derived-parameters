#    SOFTWARE HISTORY
#    
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    18 Feb 2010     #4502         jelkins        Initial Creation.

from numpy import array, nanmax

def execute(*args):
    """ Return the max value at each grid point
    
    @param args
                a list of grids or a single 3D grid. If a single 3D variable is passed in, 
                will compute without considering the vertical coordinate information. 
    """
    if len(args) == 1 and isinstance(args[0], list):
        if len(args[0]) == 2 and len(args[0][0].shape) == 3:
            # we have been passed 3D data
            return nanmax(args[0][0], 0)
        else:
            return execute(*args[0])
    else:
        return nanmax(array(list(args)), 0)
    
def test():
    """ Unit test
    """
    
    from numpy import all
    
    threeDarray = array([[[1.,2.],[20.,3.]],[[3.,40.],[4.,5.]],[[5.,6.],[6.,7.]]])
    grid1 = threeDarray[0]
    grid2 = threeDarray[1]
    grid3 = threeDarray[2]
    correctResult = array([[ 5, 40],[20,  7]])

    result = execute([threeDarray,0])
    
    if not(all(result == correctResult)):
        raise Exception
    
    result = execute(grid1,grid2,grid3)
    
    if not(all(result == correctResult)):
        raise Exception
    
    print "Max Test Complete"