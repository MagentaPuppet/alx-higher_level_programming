#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    joint = (list(set_1) + list(set_2))
    for i in range(len(joint)):
        if joint[i] not in (joint[(i + 1):] + joint[:i]):
            diff += [joint[i]]
    return set(diff)
