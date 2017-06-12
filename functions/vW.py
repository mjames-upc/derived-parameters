from numpy import concatenate
from numpy import zeros

def execute1(vComp, v10):
    v10 = v10.reshape(-1, 1);
    return concatenate((v10, vComp), 1)

def execute3(vwpV):
    return concatenate((zeros([vwpV.shape[0],1], 'float32'), vwpV), 1)
