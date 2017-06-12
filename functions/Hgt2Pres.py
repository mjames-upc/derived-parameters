from numpy import power, piecewise

T0 = 288.0
gamma = 0.0065
p0 = 1013.2
c1 = 5.256
c2 = 14600
z11 = 11000
p11 = 226.0971

# Routine to calculate pressure from height based on a standard
#  atmosphere
def execute(z):
    return piecewise(z, [z < z11, z >= z11], [lambda z: p0*power((T0-gamma*z)/T0,c1), lambda z: p11*power(10, (z11-z)/c2)])
