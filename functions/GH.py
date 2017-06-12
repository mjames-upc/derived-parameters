#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Removed unused imports
#

import meteolib
from numpy import concatenate

import P

def execute1(levels, staElev):
    staElev = staElev.reshape(-1, 1);
    hft2m = 30.48
    return concatenate((staElev, levels * hft2m), 1)

def execute2(pres):
    return meteolib.ptozsa(pres)*4

def execute3(prCloudStation,lowCldStation,midCldStation,hiCldStation):
    prCloudClg = P.execute6(prCloudStation,lowCldStation,midCldStation,hiCldStation)
    return meteolib.ptozsa(prCloudClg)

