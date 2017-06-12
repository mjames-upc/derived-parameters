# ----------------------------------------------------------------
# Returns waveHeight if it exists, otherwise return windWaveHeight
# 
# ----------------------------------------------------------------
import numpy
from numpy import concatenate
from numpy import isnan

# select waveHeight if it exists, otherwise return windWaveHeight
def combineHeights(waveHeight, windWaveHeight):
    return numpy.where(isnan(waveHeight), windWaveHeight, waveHeight)
    

# Returns waveHeight if it exists, otherwise return windWaveHeight
#
# @param waveHeight : waveHeight
# @param windWaveHeight : windWaveHeight
# @return:
# @rtype:
# 
def execute1(waveHeight,windWaveHeight):
    return combineHeights(waveHeight,windWaveHeight)
