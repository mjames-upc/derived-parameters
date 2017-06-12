# ----------------------------------------------------------------
# 
# 
# ----------------------------------------------------------------
import numpy
from numpy import isnan

def execute(temperature, tempFromTenths, accum_temperature24, accum_tempFromTenths24):
    T0 = numpy.where(isnan(tempFromTenths), temperature, tempFromTenths)
    T0 = (T0 * 1.8) + 32
    T24 = numpy.where(isnan(accum_tempFromTenths24), accum_temperature24, accum_tempFromTenths24)
    T24 =(T24 * 1.8) + 32
    return T0 - T24