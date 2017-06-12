from numpy import arctan2
from numpy import hypot
from numpy import cos
from numpy import sin
from numpy import degrees
from numpy import radians
from numpy import abs
from numpy import isscalar, empty, float32
from numpy import NaN

def execute(u, v, magDir=None):
    """ Make a vector from u,v or mag, dir.
      
      @param magDir
                 controls how the function operates on the given u and v values.
                 When the magDir is specified and is a constant scalar value
                 the u and v input values are assumed to be speed and direction.

                 positive :: assume meteorological direction(direction from)
                 negative :: assume mathematical direction(direction to)
      
                 abs(legacyOption) == 1 :: assume direction in degrees
                 abs(legacyOption) != 1 :: assume direction in radians

      @return: tuple of (u,v)
    
    """
    # If either u or v is a single number, expand it to match an entire Grid
    if isscalar(u) and not(isscalar(v)):
        tmp = empty(v.shape, float32)
        tmp.fill(u)
        u = tmp
        
    if isscalar(v) and not(isscalar(u)):
        tmp = empty(u.shape, float32)
        tmp.fill(v)
        v = tmp
    
    if magDir == None:
        return componentsTo(u, v)
    elif magDir == 1:
        return magDirDegreesFrom(u, v);
    elif magDir == -1:
        return magDirDegreesTo(u, v);
    elif magDir >= 0:
        return magDirRadiansFrom(u, v);
    else:
        return magDirRadiansTo(u, v);

def componentsTo(u,v):
    return (u, v)

def magDirRadiansTo(mag, dir):
    u = sin(dir) * mag
    v = cos(dir) * mag
    return componentsTo(u,v)

def magDirDegreesTo(mag, dir):
    # in nwps1 model, it uses -999 to denote no value in the direction grid
    # so we assume anything less than -360 is invalid
    dir[dir<-360] = NaN
    return magDirRadiansTo(mag, radians(dir))

def componentsFrom(u,v):
    return componentsTo(-u,-v)

def magDirRadiansFrom(mag, dir):
    u = sin(dir) * mag
    v = cos(dir) * mag
    return componentsFrom(u,v)

def magDirDegreesFrom(mag, dir):
    # in nwps1 model, it uses -999 to denote no value in the direction grid
    # so we assume anything less than -360 is invalid
    dir[dir<-360] = NaN
    return magDirRadiansFrom(mag, radians(dir))