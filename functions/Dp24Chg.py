# ----------------------------------------------------------------
# 
# 
# ----------------------------------------------------------------
import numpy

def execute(dewpoint, dpFromTenths, accum_dewpoint24, accum_dpFromTenths24):
    Td24 = numpy.where(numpy.isnan(dpFromTenths), dewpoint, dpFromTenths)
    Td0 = (dewpoint * 1.8) + 32
    Td24 = numpy.where(numpy.isnan(accum_dpFromTenths24), accum_dewpoint24, accum_dpFromTenths24)
    Td24 = (accum_dpFromTenths24 * 1.8) + 32
    return Td0 - Td24