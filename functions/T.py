# ----------------------------------------------------------------
# Returns tempFromTenths if present, otherwise returns temperature
# 
# ----------------------------------------------------------------
import numpy
from numpy import concatenate
from numpy import isnan
from unit import celciusToKelvin 

# build an array that contains the higher resolution tempFromTenths where possible, otherwise use the lower resolution temperature
def combineTemps(temperature,tempFromTenths):
    return numpy.where(isnan(tempFromTenths), temperature, tempFromTenths)
    

# Returns tempFromTenths if present, otherwise returns temperature
#
# @param temperature : temperature
# @param tempFromTenths : tempFromTenths
# @return:
# @rtype:
# 
def execute1(temperature,tempFromTenths):
    return celciusToKelvin(combineTemps(temperature,tempFromTenths))

def execute2(temperature, temp2):
    temp2 = temp2.reshape(-1, 1);
    result = concatenate((temp2, temperature), 1)
    return result

def execute3(temperatureStation,tempFromTenthsStation):
    return celciusToKelvin(combineTemps(temperatureStation, tempFromTenthsStation))