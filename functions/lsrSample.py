from datetime import datetime

def execute(timeObs, injuries, fatalities, remarks):
    "Calculate Sampling String."
    sampleStrings = list()
    for num in range(len(injuries)):
        timeVal = datetime.utcfromtimestamp(timeObs[num]/1000).strftime("%H%MZ");
        injuriesVal = injuries[num]
        fatalitiesVal = fatalities[num]
        remarksVal = remarks[num]
        if (injuriesVal > 0 or fatalitiesVal > 0):
            if (injuriesVal <= 0):
                casualtiesStr = ' *** ' + str(fatalitiesVal) + ' FATAL *** '
            elif (fatalitiesVal <= 0):
                casualtiesStr = ' *** ' + str(injuriesVal) + ' INJ *** '
            else:
               casualtiesStr = ' *** ' + str(fatalitiesVal) + ' FATAL, ' + str(injuriesVal) + ' INJ *** '
        else:
            casualtiesStr = ' '
        sampleStrings.append(timeVal + casualtiesStr + remarksVal)
    return sampleStrings

    