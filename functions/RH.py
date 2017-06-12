from numpy import exp

def execute1(T, DpT):
    "Calculate Relative Humidity from Temperature and Dewpoint Temp."
    RH = T-DpT
    RH *= 0.0091379024
    RH += 6106.396/T
    RH -= 6106.396/DpT
    RH = exp(RH)
    RH *= 100
    return RH

def execute2(P, T, SHx):
    "Calculate Relative Humidity from Pressure, Temp, and Spec Humidity."
    # Constants from the Fortran code.
    a = 22.05565
    b = 0.0091379024
    c = 6106.396
    epsilonx1k = 622.0
    
    shxDenom = SHx * 0.378
    shxDenom += epsilonx1k
    
    tDenom = -b*T
    tDenom += a
    tDenom -= c/T
    
    RH = P * SHx
    RH /= shxDenom
    RH /= exp(tDenom)

    return RH

