# Provide access to the meteolib functions through the java library


#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    Aug 13, 2013    2262          dgilling       Use new wxmath routine ports.
########################################################################


from com.raytheon.uf.common.wxmath import PToZsa
from com.raytheon.uf.common.wxmath import ZToPsa
import numpy

#allows calling ztopsa with either a float, numpy.float32, or ndarray
def ztopsa(Z):
    if isinstance(Z, float) or isinstance(Z, numpy.float32):
        if (Z > -9998): 
            return ZToPsa.ztopsa(float(Z))
    elif isinstance(Z, numpy.ndarray):
        result = numpy.ndarray(Z.shape, numpy.float32)
        for i in range(len(Z)):
            result[i] = ztopsa(Z[i]);
        return result
    return Z

#allows calling ptozsa with either a float, numpy.float32, or ndarray
def ptozsa(P):
    if isinstance(P, float) or isinstance(P, numpy.float32):
        if (P > -9998):
            return PToZsa.ptozsa(float(P))
    elif isinstance(P, numpy.ndarray):
        result = numpy.ndarray(P.shape, numpy.float32)
        for i in range(len(P)):
            result[i] = ptozsa(P[i]);
        return result
    return P