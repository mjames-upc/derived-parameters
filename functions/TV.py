# ----------------------------------------------------------------
# calculate virtual temperature from the pressure, 
#    temperature, and relative humidity.
# ----------------------------------------------------------------

from numpy import clip
from numpy import exp

def execute(P,T,RH):
    "Calculate virtual temperature from temperature(K), relative \
    humidity(0 to 100) and Pressure."

    rhqc=clip(RH,1.0,100.0)
    k = T
    eee = exp(21.0827887-0.0091379024*k-6106.396/k)
    tv = T * P / (P - RH * eee)
    return tv
