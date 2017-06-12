from numpy import where, isnan

def execute(precip, accumNow, accumBefore):
    if(len(precip.shape) == 2):
        precip = precip.sum(1)
    return where(isnan(precip), accumNow-accumBefore, precip)