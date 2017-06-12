#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       cast ints in where() to float32
#

import numpy


def execute1(gammaE,MpV):
   "Calculate slantwise and vertical instability, assign as icons"
   MpV = MpV*1E5

   tmp = numpy.zeros(gammaE.shape,dtype=gammaE.dtype)

   mask1 = numpy.less(gammaE, 0.0)
   tmp = numpy.where(mask1, numpy.float32(192), tmp)

   mask2 = numpy.greater_equal(gammaE, 0.0)
   mask3 = numpy.less(MpV, 0.20)
   #0.25
   tmp = numpy.where(numpy.ma.logical_and(mask2, mask3), numpy.float32(30), tmp)

   return tmp
