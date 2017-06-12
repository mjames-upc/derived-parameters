import gridslice
from numpy import ndarray, NaN

gridslice_maskval = 1e37

def execute(*args):
    #defineNumpySlice(vc, param, targetLevel, sense)
    # vc - cube/list for output parameter
    # param - cube of data that is the same as targetLevel
    # targetLevel - constant value level
    # sense - corresponds to vc for vertical coordinate and whether to search for highest/lowest occurence
    #
    #createNumpySlice(vc, s3d, targetLevel, sense, hyb-optional)
    # vc - cube/list of data that is the same as targetLevel
    # s3d - cube for output parameter
    # targetLevel - 2d grid of data values to find in vc to interpolate s3d
    # sense - corresponds to vc for vertical coordinate and whether to search for highest/lowest occurence
    if len(args) == 3:

        # cube, target level, sense
        if type(args[1]) == ndarray:
            # target level is 2d grid
            rval = gridslice.createNumpySlice(args[0][1], args[0][0], args[1], int(args[2]))
            rval[rval == gridslice_maskval] = NaN
            return rval
        else:
            # target level is single value
            rval = gridslice.defineNumpySlice(args[0][1], args[0][0], args[1], int(args[2]))
            rval[rval == gridslice_maskval] = NaN
            return rval
    else:
        if type(args[2]) == ndarray:
            # cube, cube, grid, sense
            rval = gridslice.createNumpySlice(args[0][0], args[1][0], args[2], int(args[3]))
            rval[rval == gridslice_maskval] = NaN
            return rval
        else:
            # cube, cube, level, sense
            # need to make 2 slice calls, one to create the common level slice
            # and a second to make the output slice
            levelSense = -1
            if abs(int(args[3])) > 1:
                levelSense = -2

            # create slice at common cube level
            rval = gridslice.defineNumpySlice(args[0][1], args[0][0], args[2], levelSense)

            rval = gridslice.createNumpySlice(args[1][1], args[1][0], rval, int(args[3]))
            rval[rval == gridslice_maskval] = NaN
            return rval
        