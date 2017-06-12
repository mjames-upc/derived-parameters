# ----------------------------------------------------------------
#Returns the sum of elevation and the 1st skyLayerBase
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



# Returns the sum of elevation and the 1st skyLayerBase
#
# @param skyLayerBase, : skyLayerBase,
# @param elevation : elevation
# @return:
# @rtype:
#
def execute(skyLayerBase, elevation, index):
    #convert elevation (m) to elevation (ft)
    elevation_ft = (elevation * 3.2808399)
    return skyLayerBase[:,index] + elevation_ft
