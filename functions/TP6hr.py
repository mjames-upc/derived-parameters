#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Optimized
#


def execute(TP3hrtPlus0, TP3hrtMinus10800):
    TP3hrtPlus0[TP3hrtPlus0 > 4e13] = 0
    TP3hrtMinus10800[TP3hrtMinus10800 > 4e13] = 0;
    result = TP3hrtPlus0+TP3hrtMinus10800
    return result
