#!/usr/bin/python3
"""
A module that defines a function that determines
if all boxes can be opened or not
"""


def canUnlockAll(boxes):
    """
    function that determines if all boxes passed as
    an argument can be opened or not.A box is a lists
    of lists and each box contains key numbered as boxes are
    Boxes are numbered from 0 to n - 1.
    Return a boolean value
    """

    for i in range(0, len(boxes)):
        if i == 0:
            current_keys = {key for key in boxes[i]}
            continue
        elif i in current_keys:
            current_keys = current_keys.union(boxes[i])
            continue
        elif i < len(boxes) - 1 and i not in current_keys:
            # iterate throught the whole set to check if i is in a corresponding box-key
            unlockable = False
            for key in current_keys:
                if i in boxes[key]:
                    current_keys = current_keys.union(boxes[i])
                    unlockable = True
                    break
            if unlockable:
                continue
            else:
                return False
        else:
            return False
    return True
