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
    print("data is {}".format(data))
    if data == []:
        return False
    valid = helper_validate_utf8(data, True)
    return valid


def helper_validate_utf8(data, valid):
    """
    Recursive helper function to help validate utf8
    """
    i = 0
    if len(data) == 0:
        return valid
    if valid is False:
        return valid
    first_byte = "{0:b}".format(data[0])
    try:
        first_byte = first_byte[-8:]
    except Exception as e:
        first_byte = first_byte
    if len(first_byte) <= 7:
        # print("first byte is less than 8 bits {}".format(first_byte))
        valid = True
        i = i + 1
        data = data[i:]
        valid = helper_validate_utf8(data, valid)
    elif first_byte[0:3] == "110":
        # print("first byte is of case 110 {}".format(first_byte))
        try:
            second_byte = "{0:b}".format(data[1])
            second_byte = second_byte[-8:]
        except Exception as e:
            valid = False
            return valid
        if second_byte[0:2] == "10":
            # print("second byte is of case 110 {}".format(second_byte))
            valid = True
            i = i + 2
            data = data[i:]
            valid = helper_validate_utf8(data, valid)
        else:
            # print("second byte is of case 110 {}".format(second_byte))
            valid = False
            return valid
    elif first_byte[0:4] == "1110":
        # print("first byte is of case 1110 {}".format(first_byte))
        try:
            second_byte = "{0:b}".format(data[1])
            third_byte = "{0:b}".format(data[2])
            second_byte = second_byte[-8:]
            third_byte = third_byte[-8:]
        except Exception as e:
            valid = False
            return valid
        if second_byte[0:2] == "10" and third_byte[0:2] == "10":
            # print("second byte is of case 110 {}".format(second_byte))
            # print("third byte is of case 110 {}".format(third_byte))
            valid = True
            i = i + 3
            data = data[i:]
            valid = helper_validate_utf8(data, valid)
        else:
            # print("second byte is of case 110 {}".format(second_byte))
            # print("third byte is of case 110 {}".format(third_byte))
            valid = False
            return valid
    elif first_byte[0:5] == "11110":
        # print("first byte is of case 11110 {}".format(first_byte))
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
            # print("second byte is of case 110 {}".format(second_byte))
            # print("third byte is of case 110 {}".format(third_byte))
            # print("fourth byte is of case 110 {}".format(fourth_byte))
            valid = True
            i = i + 4
            data = data[i:]
            valid = helper_validate_utf8(data, valid)
        else:
            # print("second byte is of case 110 {}".format(second_byte))
            # print("third byte is of case 110 {}".format(third_byte))
            # print("fourth byte is of case 110 {}".format(fourth_byte))
            valid = False
            return valid
    else:
        # print("first byte is {}".format(first_byte))
        if len(first_byte) == 8 and first_byte[0] == "0":
            i = i + 1
            data = data[1:]
            valid = helper_validate_utf8(data, valid)
        else:
            valid = False
            return valid
    return valid
