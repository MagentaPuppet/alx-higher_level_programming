#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = []
    for i in my_list:
        tmp.append(i)
        if idx < len(tmp) and idx >= 0:
            tmp[idx] = element
    return tmp
