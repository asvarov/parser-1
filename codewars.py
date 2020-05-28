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


def spin_words(sentence):
    """
    Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
    letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
    Spaces will be included only when more than one word is present.
    Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns
    "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
    """
    s = sentence.split()
    l = len(s)
    if l == 1:
        print(s[0][::-1])
    else:
        for i in range(l):
            if len(s[i]) > 5:
                print(s[i][::-1], end=' ')
            else:
                print(s[i], end=' ')
    return None


spin_words("Hey fellow warriors")