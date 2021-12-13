import math

def total(values):
    out = float(sum(values))
    return out

def average(values):
    if values == []:
        return math.nan
    else:
        out = float(sum(values)) / float(len(values))
        out = float("{:.5f}".format(out))
        return out

def median(values):
    if values != []:
        values = sorted(values)
        middle1 = (len(values) - 1) // 2
        middle2 = len(values) // 2
        return (values[middle1] + values[middle2]) / 2
    else:
        raise ValueError('ValueError empty variable')
