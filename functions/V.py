# ----------------------------------------------------------------
# Calculate V component from a vector or from a magnitude and direction
#
# ----------------------------------------------------------------

#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Optimized
#

from numpy import NaN, float32, cos, radians

def execute(magOrVec, dir=None):
    if dir is None:
        return magOrVec[0]

    dir[dir < 0] = float32(NaN)
    dir[dir > 360] = float32(NaN)
    magOrVec[magOrVec < 0] = float32(NaN)
    magOrVec[magOrVec > 250] = float32(NaN)
    theta = radians(dir)
    V = (-1 * magOrVec) * cos(theta)
    return V