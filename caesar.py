

def encrypt(text, rot):
    """
    Ceaser encryption.
    """

    if type(text) != type(''):
        raise TypeError
    if type(rot) != type(1):
        raise TypeError

    retText = ''
    for char in text:
        retText += helpers.rotate_character(char, rot)
    return retText
