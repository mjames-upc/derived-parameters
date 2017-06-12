#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       added casts to float32 and int32
#

from numpy import where, NaN, float32

def execute(arg1, arg2):
    if(arg2.dtype == float32):
        return where(arg1 >= 0, arg2, float32(NaN))
    else:
        return where(arg1 >= 0, arg2, int32(-9999))