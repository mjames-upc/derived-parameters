#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Removed unused imports
#

from numpy import concatenate, zeros

def execute1(uComp, u10):
    u10 = u10.reshape(-1, 1);
    return concatenate((u10, uComp), 1)

def execute3(vwpU):
    return concatenate((zeros([vwpU.shape[0],1], 'float32'), vwpU), 1)

