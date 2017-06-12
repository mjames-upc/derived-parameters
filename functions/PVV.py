#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Removed unused imports
#

from numpy import concatenate, zeros, shape, nan

def execute1(pvv):
    pv = zeros((shape(pvv)[0], 1))
    pv.fill(nan)
    result = concatenate((pv, pvv),1)
    return result

