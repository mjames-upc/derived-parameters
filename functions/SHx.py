# ----------------------------------------------------------------
# Calculate Specific Humidity (g/Kg) from Pressure, Temperature and
# Relative Humidity.
# ----------------------------------------------------------------

#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Optimized
#

from numpy import concatenate


def execute(specHum, q2):
    q2 = q2.reshape(-1, 1);
    result = concatenate((q2, specHum), 1)
    result[result != -9999] *= 1000
    return result
