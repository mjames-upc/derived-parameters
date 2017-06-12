#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       cast NaN to float32
#

from numpy import where, isnan, NaN, float32

def execute(precip, accum_precip):
    sum = accum_precip.sum(axis=1)
    sum[sum < -0.005] = float32(NaN)
    return where(isnan(precip), sum, precip)