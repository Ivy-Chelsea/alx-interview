#!/usr/bin/python3
"""

"""

def canUnlockAll(boxes):
    """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations. One to traverse the list
    and the other to compare if key is idx or not in order to open
    """
    if type(boxes) is not list:
        return False
    else (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] nd k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
