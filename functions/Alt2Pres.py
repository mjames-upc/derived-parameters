from numpy import power


# Routine to pressure from elevation and altimeter setting.
#
# @param alt: Altimeter setting (X)
# @param z: Elevation in meters.
# @return: Pressure (X)

def execute(alt, z):
    T0 = 288.0
    gamma = 0.0065
    g_Rgamma = 5.2532
    result = (T0-gamma*z)/T0
    result = power(result, g_Rgamma)
    result = alt*result
    return result
