from numpy import array, NaN, float32

def execute(levelsList, index):
    maxLen = 0
    results = []
    for i in range(len(levelsList)):
        levels = levelsList[i]
        values = []
        for level in levels:
            values.append(level.getParam(index))
        if len(levels) > maxLen:
            maxLen = len(levels)
        results.append(values)
    for result in results:
        while len(result) < maxLen:
            result.append(NaN)
    return array(results, float32)