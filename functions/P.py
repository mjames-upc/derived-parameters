#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       cast scalars to float32
#

import meteolib
from numpy import equal, where, zeros, concatenate, greater, float32
from unit import pascalToMilliBar

def execute1(pressure, sfcPress):
    sfcPress = sfcPress.reshape(- 1, 1);
    result = concatenate((sfcPress, pressure), 1)
    return pascalToMilliBar(result)

def execute2(levels, staElev):
    staElev = staElev.reshape(- 1, 1);
    hft2m = 30.48
    levelsInMeters = where(equal(levels, - 9999), float32(-9999), levels * 30.48)
    GH = concatenate((staElev, levelsInMeters), 1)
    return meteolib.ztopsa(GH)

def execute3(numProfLvlsStation, MB):
    ret = zeros(numProfLvlsStation.shape, float32)
    ret.fill(MB)
    return ret

def execute4(prCloudStation,lowCldStation,midCldStation,hiCldStation):
    prCloudMB = prCloudStation/100
    CCPval = ccpExecute(lowCldStation,midCldStation,hiCldStation)
    isCeiling = where(greater(CCPval, 0.5), CCPval, float32(-9999))
    prCloudMB[isCeiling == -9999] = float32(-9999)
    prCloudMB[prCloudStation == -9999] = float32(-9999)
    return prCloudMB;

def execute5(height, elevation):
    # array height is in meters
    # scalar elevation is in meters
    pressure = where(equal(height, - 9999), float32(-9999), height + elevation)
    pressure = meteolib.ztopsa(pressure)
    return pressure

def execute6(numLevelsStation, MB):
    ret = zeros(numLevelsStation.shape, float32)
    ret.fill(MB)
    return ret

def ccpExecute(lowCldStation,midCldStation,hiCldStation):
    P = maximum(lowCldStation,midCldStation,hiCldStation)
    P[P != -9999] /= 100
    return P
