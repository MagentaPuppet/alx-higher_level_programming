#!/usr/bin/python3
def roman_to_int(roman_string):
    dec_places = {1: ["M", "C", "X", "I"],
                  2: ["MM", "CC", "XX", "II"],
                  3: ["MMM", "CCC", "XXX", "III"],
                  4: [None, "CD", "XL", "IV"],
                  5: [None, "D", "L", "V"],
                  6: [None, "DC", "LX", "VI"],
                  7: [None, "DCC", "LXX", "VII"],
                  8: [None, "DCCC", "LXXX", "VIII"],
                  9: [None, "CM", "XC", "IX"]}
    num = 0
    i = 0
    if type(roman_string) == str:
        length = len(roman_string)
        while i < length:
            for c in range(len(roman_string[::-1])):
                for key in dec_places:
                    for place in range(len(dec_places[key])):
                        if roman_string[::-1][(c):][::-1] \
                           == dec_places[key][place]:
                            tmp = ""
                            num += key * 10**(3-place)
                            tmp += roman_string[::-1][:(c)]
                            roman_string = tmp[::-1]
                            i += 1
                            if len(roman_string) == 0:
                                i = length
        return num
    else:
        return 0
