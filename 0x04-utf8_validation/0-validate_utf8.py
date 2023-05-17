#!/usr/bin/python3
"""
Contains a function that validates input for
utf-8 encoding
"""


def validUTF8(data):
    """
    Determines if data is valid utf-8
    encoding
    returns True if valid or False
    if not valid
    """
    for number in data:
        number_bin = "{0:b}".format(number)
        no_of_digits = len(number_bin)
        if 1 < no_of_digits <= 7 or\
                (no_of_digits != 8 and no_of_digits % 8 == 0):
            continue
        else:
            return False
    return True
