def digital_root(n):
    """
    digital_root(942)
    => 9 + 4 + 2
    => 15 ...
    => 1 + 5
    => 6
    """
    s = str(n)
    summ = 0
    for i in range(len(s)):
        summ = summ + int(s[i])
    return int(summ)


def alphabet_position(text):
    """
    alphabet_position("The sunset sets! at twelve o' clock.")
    """
    punctulars = ",.?!@#$%^*( )\'"
    for i in punctulars:
        text = text.replace(i, '').lower()
    for i in text:
        alphabet = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13,
                    'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22,
                    'y': 25, 'x': 24, 'z': 26}
        print(alphabet['{}'.format(i)], end=' ')

alphabet_position("The sunset sets! at twelve o' clock.")