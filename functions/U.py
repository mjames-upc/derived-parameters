#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Optimized
#

# ----------------------------------------------------------------
# Calculate U component from a vector or from a magnitude and direction
#
# ----------------------------------------------------------------

from numpy import float32, NaN, sin, radians

def execute(magOrVec, dir=None):
    if dir is None:
        return magOrVec[0]
    dir[dir < 0] = float32(NaN)
    dir[dir > 360] = float32(NaN)
    magOrVec[magOrVec < 0] = float32(NaN)
    magOrVec[magOrVec > 250] = float32(NaN)
    theta = radians(dir)
    U = (-1 * magOrVec) * sin(theta)
    return U