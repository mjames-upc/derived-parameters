# ----------------------------------------------------------------
# Calculate Direction
# ----------------------------------------------------------------

from numpy import arctan2
from numpy import any


def execute(uW, vW, copy=False):
       # 180.0 / pi = 57.2957
       dir = 57.2957 * arctan2(-uW,-vW)
       dirN = dir < 0
       if any(dirN):
           dir[dirN] += 360.0
       return dir
