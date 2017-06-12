# ----------------------------------------------------------------
# Returns wave type information
# 
# ----------------------------------------------------------------
import numpy
from numpy import concatenate
from numpy import isnan
from numpy import zeros

# Returns
#   0 if no wave infomation is present
#   1 if waveHeight information is present
#   2 if waveHeight is not present and windWaveHeight data is present.
def determineType(waveHeight, windWaveHeight):
    nn = len(waveHeight)
    type = numpy.zeros(nn)
    for n in range(nn):
        if isnan(waveHeight[n]):
            if not isnan(windWaveHeight[n]):
                type[n] = 2
        else:
            type[n] = 1
    
    return type
    

# Returns wave type information
#
# @param waveHeight : waveHeight
# @param windWaveHeight : windWaveHeight
# @return:
# @rtype:
# 
def execute1(waveHeight,windWaveHeight):
    return determineType(waveHeight,windWaveHeight)
