## @file gamma.py

from numpy.ma.core import masked_values
from numpy.ma.core import log

## 
# Calculate lapse rate from temperature and pressure pairs.
# This method is derived from the lapserate.f function, which 
# used an extra integer parameter to determine which of 5 functions
# were to be used. However, only the "4" (pressure) function was
# being used.
#
# @param Tlo: Temperature at lower level (K) 
# @param Plo: Pressure at lower level (mb)
# @param Thi: Temperature at upper level (K)
# @param Phi: Pressure at upper level (mb)
# @return: Lapse rate (C/km)  
def execute(Tlo, Plo, Thi, Phi):
    C = 0.034167
    
    Tratio = Thi/Tlo
    Pratio = Phi/Plo
    
    logTratio = log(Tratio)
    logPratio = log(Pratio)
    
    # Guard against divide-by-zero errors, again
    logPratio = masked_values(logPratio, 0, copy=False)
    
    result = C * logTratio / logPratio
    
    return result