# ----------------------------------------------------------------
#
#
# ----------------------------------------------------------------
#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Optimized
# Oct 27, 2015   4703         bsteffen      correct use of U,V
#

import U
import V
from numpy import arctan2

def execute(windSpeed, windDir, accum_windSpeed24, accum_windDir24):
    U0 = U.execute(windSpeed, windDir)
    V0 = V.execute(windSpeed, windDir)

    U24 = U.execute(accum_windSpeed24, accum_windDir24)
    V24 = V.execute(accum_windSpeed24, accum_windDir24)

    DU = U0 - U24
    DV = V0 - V24

    WD = 57.2957 * arctan2(-DU,-DV)
    WD[WD < 0] += 360

    return WD