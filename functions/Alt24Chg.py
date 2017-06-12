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
# Aug 05, 2015   4703         njensen       cast NaN to float32
# Oct 27, 2015   4703         bsteffen      correct use of where
#
from numpy import where, float32, NaN

const1 = 33.86389
const2 = 100

def execute(altimeter, accum_altimeter24):
    ALT0 = where(altimeter > 0 , altimeter, float32(NaN))
    ALT24 = where(accum_altimeter24 > 0,
                        accum_altimeter24,
                        float32(NaN))
    return (ALT0 - ALT24) * const1 * const2