from numpy import isnan

def execute(wSp, WD, wW, rms):
    "Calculate Sampling String."
    sampleStrings = list()
    for i in range(len(wSp)):
        if (isnan(WD[i]) or WD[i] <= -8888):
            windDirStr = '***'
        else:
            windDirStr = "%3.3ddeg " % WD[i]
        if (isnan(wSp[i]) or wSp[i] <= -8888):
            windSpdStr = '***'
        else:
            windSpdStr = "%dkts " % (wSp[i] * 1.944)
        if (isnan(rms[i]) or rms[i] <= -8888):
            rmsStr = '***'
        else:
            rmsStr = "rms:%.0fkts " % rms[i]
        if (isnan(wW[i]) or wW[i] <= -8888):
            wCompStr = '***'
        else:
            wCompStr = "w:%.0fcm/s " % wW[i]
        sampleStrings.append(windDirStr + windSpdStr + rmsStr + wCompStr)
    return sampleStrings

        
    