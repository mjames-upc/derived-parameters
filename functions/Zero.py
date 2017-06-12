#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       cast 0 to float32
#

from numpy import where, float32
from unit import inchToMillimeter

# zero out all negative precip values
def execute(values, min):
    return where((values < min), float32(0), values);
