# ----------------------------------------------------------------
# Returns wavePeriod if it exists, otherwise return windWavePeriod
# 
# ----------------------------------------------------------------
import numpy
from numpy import concatenate
from numpy import isnan

# select wavePeriod if it exists, otherwise return windWavePeriod
def combineHeights(wavePeriod, windWavePeriod):
    return numpy.where(isnan(wavePeriod), windWavePeriod, wavePeriod)
    

# Returns wavePeriod if it exists, otherwise return windWavePeriod
#
# @param wavePeriod : waveHeight
# @param windWavePeriod : windWaveHeight
# @return:
# @rtype:
# 
def execute1(wavePeriod,windWavePeriod):
    return combineHeights(wavePeriod,windWavePeriod)
