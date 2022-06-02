#!/usr/bin/python3
def remove_char_at(str, n):
    str_new = ""
    i = 0
    for c in str:
        if i != n:
            str_new += c
        i += 1
    return str_new
