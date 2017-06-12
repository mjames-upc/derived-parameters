from numpy import power


# This routine estimates 1000 to 500 mb thickness from 500 height
#  and mean sea level pressure.

def execute(mslp, GH):
        "Calculate thickness from mean sea level pressure and height."
        # Constants from Fortran code.
        # Wish these had more descriptive names; don't know what they are.
        a = 0.4599042
        b = 3.262312
        c = 0.1902672
        # calculate thickness
        dZ = GH * a
        denom = power(mslp, c)
        denom -= b
        dZ /= denom
        return dZ
