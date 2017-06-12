#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       cast NaN to float32
#

from numpy import NaN, float32

# For modelsounding cloud layers, return prCloud when it is > bottom and < top
def execute(prCloudHgt, bottom, top):
    prCloudHgt[prCloudHeight <= bottom] = float32(NaN)
    prCloudHgt[prCloudHeight >= top] = float32(NaN)
    return prCloudHgt