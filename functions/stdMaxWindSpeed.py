## @file stdMaxWindSpeed.py

from numpy import isnan

# Do we plot any Dewpoints for this projection due to
# projection interval discrepancies between elements?

def execute(MaxWindSpeed):
    maxWindSpeedString = list()
    for num in range(len(MaxWindSpeed)):
        value = MaxWindSpeed[num];
        if (value <= 0.0 or isnan(value)):
            value = ''
        else:
            value = "G%d" % int(value)
        maxWindSpeedString.append(value)
    return maxWindSpeedString
