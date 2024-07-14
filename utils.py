def isValidNumber(number: str):
    valid = False
    try:
        float(number)
        valid = True
        return valid

    except ValueError:
        return valid


def isnNumOrDotOrComma(input : str):
    valid = True
    if input not in "1234567890,.":
        valid = False
    return valid


def isEmpty(string: str):
    return len(string) == 0