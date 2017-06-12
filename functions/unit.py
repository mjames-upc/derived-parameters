#
# SOFTWARE HISTORY
#
# Date           Ticket#      Engineer      Description
# ------------   ----------   -----------   -----------
#                             ????          Initial creation
# Aug 05, 2015   4703         njensen       Optimized
#

# Provide unit constants and conversions

def celciusToKelvin(celcius):
    return _add(celcius, 273.15)

def pascalToMilliBar(pascal):
    return _multiply(pascal, 0.01)

def knotToMetersPS(knot):
    return _multiply(knot, 0.514)

# water at 4 degrees celcius
def kgPerSquareMeterToInchOfWater(kgPm2):
    return _multiply(kgPm2, 0.03937117)

def mileToMeter(mile):
    return _multiply(mile, 1609.344)


def inchToMillimeter(inch):
    return _multiply(inch, 25.4)

def _multiply(array,scalar,dataMissing=-9999):
    array[array != dataMissing] *= scalar
    return array

def _add(array,offset,dataMissing=-9999):
    array[array != dataMissing] += offset
    return array
