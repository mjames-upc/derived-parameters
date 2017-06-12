from numpy import add
from numpy import array
from numpy import zeros
from Magnitude import execute as Magnitude

def execute(uStk, vStk):
    res = zeros(uStk[0].shape, 'float32')
    for i in range(1, len(uStk)):
        u1 = uStk[i-1]
        v1 = vStk[i-1]
        u2 = uStk[i]
        v2 = vStk[i]
        res += Magnitude(u2-u1, v2-v1)
    return res
