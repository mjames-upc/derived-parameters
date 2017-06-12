import numpy

def execute(MIXLY):
    #conversions used in awips1
    
    #first transform data to pixel values in the colormap
    
    #data 0-13 gets modified by y=112x/13 + 16
    #the result is position in the colormap
    #mask values above 13
    result = numpy.ma.masked_greater(MIXLY, 13)
    #transform unmasked values
    result *= (112.0/13.0)
    result += 16
    #now convert into actual data values
    #modified by y=0.0914286x - 1.46286
    #result is the data value as calculated in awips1
    result *= 0.0914286
    result += -1.46286
    #remove mask
    result.mask = numpy.ma.nomask
    
    #data 13-127 mapped to colormap position by y=56x/57+6568/57
    #result is in range 128->240
    result = numpy.ma.masked_less(result, 13)
    result = numpy.ma.masked_greater(result, 127)
    result *= (56.0/57.0)
    result += (6568.0/57.0)
    #map into values by y=0.801429x - 92.3429
    result *= 0.801429
    result += -92.3429
    #remove mask
    result.mask = numpy.ma.nomask
    
    #data 128->255 mapped to colormap position by y=12x/127 + 29071/127
    #result is in range 241->253
    result = numpy.ma.masked_less(result, 128)
    result = numpy.ma.masked_greater(result, 255)
    result *= (12.0/127.0)
    result += (29071.0/127.0)
    #map into data range by y=0.801429x - 92.3429
    result *= 0.801429
    result += -92.3429
    result.mask = numpy.ma.nomask
    
    #fix any values that are very close to zero but negative
    result = numpy.ma.masked_greater(result, 0)
    result *= 0.0
    result.mask = numpy.ma.nomask
    
    return result


def main():
    testin = numpy.array([[12.0,36,253,64,53,24,33],[253,254,112,29,42,1,55],[12,123,253,18,254,22,212]])
    testout = execute(testin)
    print(testout)
    
if __name__ == "__main__":
    main()
