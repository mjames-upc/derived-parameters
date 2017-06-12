import IsenStability
import Vorticity


# Calculate the isentropic potential vorticity through a layer.
#
# @change: Adapted from calcpv.f 2008-18-06
#    User Notes:
#
#    1.  Stability is defined as -dP/d(theta).  We calculate this through
#        the layer from the isentropic surface 'n' to the surface above it,
#        'n+1'.
#
#    2.  Since we are dealing with a layer, we calculate a mean absolute
#        vorticity using the winds at the upper and lower layers.
#
#    3.  The PV is then [mean abs. vort.]/[stability]
#
# @param p_up: Pressure on upper isentrope (mb)
# @param p_lo: Pressure on lower isentrope (mb)
# @param o_up: Upper isentrope (K) (usually scalar)
# @param o_lo: This (lower) isentrope (K) (usually scalar)
# @param Wind_up: tuple(U,V) of winds on upper isentrope (m/s)
# @param Wind_lo: tuple(U,V) of winds on lower isentrope (m/s)
# @param dx: Spacing between data points in X direction (m)
# @param dy: Spacing between data points in Y direction (m)
# @param coriolis: Coriolis parameters (/s)
# @return: isentropic potential vorticity array
# 
def execute(p_up, p_lo, o_up, o_lo, vector_up, vector_lo, dx, dy, coriolis):
    "Calculate the isentropic potential vorticity through a layer."
    
    u_up, v_up = vector_up
    u_lo, v_lo = vector_lo
    
    
    # Calculate the absolute vorticity at each isentropic surface.
    avort1 = Vorticity.execute(u_up, v_up, coriolis, dx, dy)
    avort2 = Vorticity.execute(u_lo, v_lo, coriolis, dx, dy)

    # Calculate the isentropic stability through the layer.
    pvort = IsenStability.execute(p_up, p_lo, o_up, o_lo)
    
    # Calculate isentropic potential vorticity
    result = avort1 + avort2
    result *= 0.5
    result /= pvort
    
    return result