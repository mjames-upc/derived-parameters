from numpy import zeros, float32, NaN, isnan


# Designed to replace interp_up and interp_down in design files for point data
#
def execute(paramArray, vertArray, numLevels, vertPoints, maxGap=None):
    #print "paramArray =", paramArray
    #print "vertArray =", vertArray
    #print "numLevels =", numLevels
    #print "vertPoints =", vertPoints
    #print "maxGap =", maxGap
    ret = zeros(numLevels.shape, 'float32')
    ret.fill(NaN)
    for i in range(len(vertArray)):
        count = numLevels[i]
        verts = vertArray[i][:count]
        params = paramArray[i][:count]
        if isinstance(vertPoints, float):
            vertPoint = vertPoints
        elif isinstance(vertPoints, float32):
            vertPoint = vertPoints
        else:
            vertPoint = vertPoints[i]
        below = None
        above = None
        for j in range(len(verts)):
            if isnan(verts[j]) or isnan(params[j]):
                continue
            if (verts[j] > vertPoint and (above == None or verts[above] > verts[j])):
                above = j
            if (verts[j] < vertPoint and (below == None or verts[below] < verts[j])):
                below = j
        if(above == None and below == None):
            ret[i] = NaN
            continue
        if (maxGap != None):
            gap = None
            if(above == None):
                gap = (vertPoint - verts[below])*2
            elif(below == None):
                gap = (verts[above] - vertPoint)*2
            else:
                gap = verts[above] - verts[below]
            if(gap == None or gap > maxGap):
                ret[i] = NaN
                continue
        if(above == None):
            ret[i] = params[below]
        elif(below == None):
            ret[i] = params[above]
        else:
            wgt = (vertPoint-verts[below])/(verts[above] - verts[below])
            ret[i] = params[below] + wgt*(params[above] - params[below])
    #print "ret = ", ret
    #print "----------------------------"
    return ret
