# ----------------------------------------------------------------------------
# Calculate wind chill from Temperature and u and v Wind (or wind speed).
#
# ----------------------------------------------------------------------------

#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Optimized
#

from numpy import where, less_equal

def execute(T, wSp):
   "This tool derives the Wind Chill index from Temperature and Wind Speed"
   mag = wSp * 1.15
   WndChl = where(less_equal(mag, 3), T, 35.74 + (0.6215 * T) -
               (35.75 * (mag ** 0.16)) + (0.4275 * T * (mag ** 0.16)))
   # clip values where WindChill > T
   mask = (WndChl > T)
   WndChl[mask] = T[mask]
   # substitute the temperature if WindChill >= 51 degrees
   mask = (T >= 51)
   WndChl[mask] = T[mask]
   return WndChl
