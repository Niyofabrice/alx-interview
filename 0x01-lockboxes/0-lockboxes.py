#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes passed to it can be opened.
    """
    unlocked = set()
    stack = [0]

    while stack:
        current_box = stack.pop()

        if current_box not in unlocked:
            unlocked.add(current_box)
            for key in boxes[current_box]:
                if key not in unlocked and key < len(boxes):
                    stack.append(key)
    return len(unlocked) == len(boxes)
