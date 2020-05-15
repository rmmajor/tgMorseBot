from pyes import consts


def is_coded(c):
    if c in consts.morze:
        return True
    else:
        return False


def trans(text):
    res = ''
    for c in text:
        if c == ' ':
            res += '    '
        if is_coded(c):
            res += consts.morze[c] + '   '
        else:
            res += c
    return res
