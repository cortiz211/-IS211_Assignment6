
def convert(fromUnit, toUnit, value):
    """
    Convert
    """
    if fromUnit == "C" and toUnit == "K":
        C = 300
        K = C + 273.15
        return K
    elif fromUnit == "C" and toUnit == "F":
        C = 300
        F = C * 1.8 + 32
        return F
    elif fromUnit == "m" and toUnit == "yr":
        m = 100
        yr = m * 1.0936
        return yr
    elif fromUnit == "m" and toUnit == "mi":
        m = 100
        mi = m * 0.00062137
        return mi
    elif fromUnit == "yr" and toUnit == "m":
        yr = 100
        m = yr / 1.0936
        return m
    elif fromUnit == "yr" and toUnit == "mi":
        yr = 100
        mi = yr * 0.00056818
        return mi
    elif fromUnit == "mi" and toUnit == "yr":
        mi = 100
        yr = mi * 1760
        return yr
    elif fromUnit == "mi" and toUnit == "m":
        mi = 100
        m = mi / 0.00062137
        return m
    elif fromUnit == "K" and toUnit =="C":
        K = 300
        C = K - 273.15
        return C
    elif fromUnit == "K" and toUnit == "F":
        K = 300
        F = K * 1.8 - 459.67
        return F
    elif fromUnit == "F" and toUnit == "C":
        F = 300
        C = (F - 32) * 5 / 9
        return C
    elif fromUnit == "F" and toUnit == "K":
        F = 300
        K = (F + 459.67) * 5 / 9
        return K
