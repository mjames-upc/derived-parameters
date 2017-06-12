from numpy import where, NaN, float32

#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       cast NaN to float32
#


# Designed to replace sample_up and sample_down in design files for point data
#
def execute(data, qc):
    return where(qc == 0, data, float32(NaN))
