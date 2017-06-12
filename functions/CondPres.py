from numpy import zeros
from numpy import log
from numpy import sqrt

CONST_A = 0.0091379024
CONST_B = 6106.396
CONST_C = 223.1986
CONST_D = 0.0182758048
CONST_E = 0.37329638
CONST_F = 41.178204
CONST_G = 0.0015945203
CONST_H = 3.498257


# Calculate condensation pressure from pressure, temperature, and relative
# humidity
# @attention: Result may contain NaN
#
# @param p: Pressure in millibars
# @type p: scalar or numpy array
# @param t: Temperature in degrees Kelvin
# @type t: scalar or numpy array
# @param rh: Relative humidity from 0.0 to 100.0
# @type rh: scalar or numpy array
#
# @return: Condensation pressure in millibars 
# @rtype: numpy array of float
def execute(p, t, rh):
    rhqc = rh.clip(1.0,100.0)
    b = CONST_A * t + CONST_B / t - log(rhqc/100.0)
    tdp = (b - sqrt(b**2.0 - CONST_C)) / CONST_D
    tcp = tdp - (t-tdp) * (-CONST_E + CONST_F / t + CONST_G * tdp)
    q = p * (tcp/t) ** CONST_H
    return q
