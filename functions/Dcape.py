#    SOFTWARE HISTORY
#    
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    Feb 17, 2010    4502          jelkins        Initial Creation.
#    Jun 05, 2013    2043          bsteffen       Ported from meteolib C
#    May 06, 2014    3101          njensen        Cast numpy shape values to int
#                                                  for cross platform compatibility
#    Mar 26, 2015    DR17264       M. Foster      Correct error due to T/Td level mismatch

from numpy import zeros
from com.raytheon.uf.common.derivparam.python.function import DCapeFuncPythonAdapter as DCapeFunc


def execute(threeDtemperature, threeDdewpoint, pressure, potentialTemperature, specificHumidity,maxEvaporation,maxRelativeHumidity,useVirtualTemp):
    """ Calculate Downdraft Convective Available Potential Energy
        
    @param threeDtemperature
                3D array of temperatures
    @param threeDdewpoint
                3D array of dewpoints
    @param pressure
    @param potentialTemperature
    @param specificHumidity
    @param maxEvaporation
                maximum amount of liquid water available to evaporate into the parcel
                as it descends, in g/g
    @param maxRelativeHumidity
                the desired maximum RH of the descending parcel as it reaches the surface
    @param useVirtualTemp
                use virtual (1) or plain (0) temperatures    
    @return
    
    """
    
    # Matt Foster:
    # Check the number of levels in the T and Td cubes.
    # If they are not equal, cut the difference off the top of the larger one.
    tempZlevs = threeDtemperature[0].shape[0]
    dewpZlevs = threeDdewpoint[0].shape[0]
    if tempZlevs != dewpZlevs:
        diff = abs(tempZlevs - dewpZlevs)
        if tempZlevs > dewpZlevs:
            threeDtemperature[0] = threeDtemperature[0][:-diff:]
        else:
            threeDdewpoint[0] = threeDdewpoint[0][:-diff:]
    threeDpressure = zeros(threeDtemperature[0].shape, threeDtemperature[0].dtype)
    
    # fill in the 3D pressure
    for pressureLevel in range(0, threeDpressure.shape[0]):
        pressureGrid = threeDpressure[pressureLevel]
        pressureGrid[:] = threeDtemperature[1][0][pressureLevel]
    
    # expand the single pressure value into a complete grid
    pressureValue = pressure
    pressure = zeros(potentialTemperature.shape, potentialTemperature.dtype)
    pressure[:] = pressureValue
    threeDshape = threeDpressure.shape
    return DCapeFunc.dcapeFunc(useVirtualTemp, threeDpressure, threeDtemperature[0], threeDdewpoint[0], pressure, potentialTemperature, specificHumidity, int(threeDshape[1]), int(threeDshape[2]), int(threeDshape[0]), maxEvaporation, maxRelativeHumidity)

