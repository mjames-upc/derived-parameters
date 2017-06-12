## @file AdiabaticTemp.py
from numpy import exp

# Constants from the old C code.
const1 = 26.660820
const2 = 0.0091379024
const3 = 6106.396
const4 = 0.622
const5 = 2740.0


# The method that does the actual calculation.
# Adapted from the old adiabatic_te.c function.
# This method skips conversion of temp and pressure to NaN arrays
# and back again. It can be called directly if temp and pressure are
# guaranteed to be valid, or if they are already NaN arrays.
#
# @param temp: Temperature (K)
# @param pressure: Pressure (mb)
# @return: Adiabatic temperature (K)
# @rtype: numpy masked array
def calculate(temp, pressure):
    ee = exp(const1 - const2*temp - const3/temp)
    pme = pressure-ee
    ee *= const4
    ee = ee / pme
    
    result = temp * exp(const5*ee/temp)
    return result
    

# Calculate adaibatic temperature.
#
# @param temp: Temperature (K)
# @param pressure: Pressure (mb)
# @return: Adiabatic temperature    
def execute(temp, pressure):    
    result = calculate(temp, pressure)
    return result
