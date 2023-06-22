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
    valid = helper_validate_utf8(data, True)
    return valid


def helper_validate_utf8(data, valid):
    """
    Recursive helper function to help validate utf8
    """
    i = 0
    # base cases
    if len(data) == 0:
        return valid
    if valid is False:
        return valid
    first_byte = "{0:b}".format(data[0],fill=0)
    try:
        first_byte = first_byte[-8:]
    except Exception as e:
        first_byte = first_byte
    # ascii values less than 128 and part of 1-byte case
    if len(first_byte) <= 7:
        valid = True
        i = i + 1
        data = data[i:]
        valid = helper_validate_utf8(data, valid)
    elif first_byte[0:3] == "110":  # two-byte case
        try:
            second_byte = "{0:b}".format(data[1])
            second_byte = second_byte[-8:]
        except Exception as e:
            valid = False
            return valid
        if second_byte[0:2] == "10":
            valid = True
            i = i + 2
            data = data[i:]
            valid = helper_validate_utf8(data, valid)
        else:
            valid = False
            return valid
    elif first_byte[0:4] == "1110":  # 3-byte case
        try:
            second_byte = "{0:b}".format(data[1])
            third_byte = "{0:b}".format(data[2])
            second_byte = second_byte[-8:]
            third_byte = third_byte[-8:]
        except Exception as e:
            valid = False
            return valid
        if second_byte[0:2] == "10" and third_byte[0:2] == "10":
            valid = True
            i = i + 3
            data = data[i:]
            valid = helper_validate_utf8(data, valid)
        else:
            valid = False
            return valid
    elif first_byte[0:5] == "11110":  # 4-byte case
        try:
            second_byte = "{0:b}".format(data[1])
            third_byte = "{0:b}".format(data[2])
            fourth_byte = "{0:b}".format(data[3])
            second_byte = second_byte[-8:]
            third_byte = third_byte[-8:]
            fourth_byte = fourth_byte[-8:]
        except Exception as e:
            valid = False
            return valid
        if second_byte[0:2] == "10" and third_byte[0:2] == "10"\
                and fourth_byte[0:2] == "10":
            valid = True
            i = i + 4
            data = data[i:]
            valid = helper_validate_utf8(data, valid)
        else:
            valid = False
            return valid
    else:  # All other one byte case
        if len(first_byte) == 8 and first_byte[0] == "0":
            i = i + 1
            data = data[1:]
            valid = helper_validate_utf8(data, valid)
        else:
            valid = False
            return valid
    return valid
