# ----------------------------------------------------------------
# Calculate mixing ratio from pressure, temperature and RH
# 
# ----------------------------------------------------------------
from numpy import exp
from numpy import zeros


# Calculate mixing ratio from pressure, temperature, and RH
#
# @param P: pressure in millibars
# @param T: temperature in degrees C or K
# @param RH: relative humidity from 0.0 to 100.0 percent
# @return mixing ratio 
# @rtype: numpy array or Python float
def execute(P,T,RH):
   "Calculate mixing ratio from pressure, temperature, and RH"
   
   eee = -0.0091379024 * T
   eee -= 6106.396 / T
   eee += 28.48859
   eee = exp(eee)
   eee = RH * eee
   denom = P - 0.001607717 * eee 
   mixRat = eee / denom
   return mixRat
