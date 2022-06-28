#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ""
    for i in my_string:
        if i not in ['c', 'C']:
            my_new_string += i
    return my_new_string
