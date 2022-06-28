#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    for i in my_list:
        if i % 2 == 0:
            x = True
        else:
            x = False
        list_result += [x]
    return list_result
