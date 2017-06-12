#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       cast NaN to float32
#

from Multiply import execute as Multiply
from numpy import NaN, where, float32


def execute(*args):
    """ Divide a scalar by a scalar or a vector by a scalar.

    """

    divArgs = list(args)

    for i in range(1,len(divArgs)):
        divArgs[i] = where(divArgs[i] == 0, float32(NaN), 1/divArgs[i] )

    return apply(Multiply,divArgs)

def test():
    from numpy import array

    if not( all(execute(array([2.,4.]),array([2.,2.])) == array([1.,2.]))):
        raise Exception

    from Vector import execute as Vector

    vector = Vector(array([2.,4.]),array([0.,270.]),True)
    (mag, dir, u, v) = execute(vector,2.)
    if not( all(mag == array([1.,2.])) and all(dir == array([0.,270.]))):
        raise Exception

    if not( all(execute(array([2.,4.]),array([2.,0.])) == array([1.,NaN]))):
        raise Exception

    print "Divide Test Complete"