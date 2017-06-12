from numpy import power
    

# Calculate theta from temperature and pressure.
# This function accepts numpy arrays
#
# @param P: Pressure in millibars
# @param T: Temperature in degrees Kelvin
# @return: Potential temperature in degrees Kelvin
# 
def execute(P, T):
    "Calculate theta (PoT) from temperature and pressure."

    pComponent = 1000.0/P
    pComponent = power(pComponent, 0.286)
    theta = T * pComponent
    # convert theta to an unmasked array with 1e37 for invalid values
    return theta
