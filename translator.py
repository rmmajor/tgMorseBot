from pyes import consts


def is_coded(c):
    if c in consts.symbs_to_morze:
        return True
    else:
        return False


def trans(text):
    res = ''
    for c in text:
        if c == ' ':
            res += '   '
        if is_coded(c):
            res += consts.symbs_to_morze[c] + '   '
        else:
            res += c
    return res


def format_morse_units(text):
    res = ''
    for c in text:
        if c in consts.format_morze:
            res += consts.format_morze[c]
        else:
            return 'ошибка'
    return res


def is_uncoded(c):
    if c in consts.morze_to_symbs:
        return True
    else:
        return False


def untrans(text):
    res = ''
    text = format_morse_units(text)
    words = text.split('       ')
    # print(words)
    for word in words:
        letters = word.split('   ')
        for letter in letters:
            if is_uncoded(letter):
                res += consts.morze_to_symbs[letter]
            else:
                res += '[ошибка декодировки]'
        res += ' '
        
    return res
