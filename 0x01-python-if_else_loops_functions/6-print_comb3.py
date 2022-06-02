#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i >= 8 and j >= 9:
            end = "\n"
        else:
            end = ", "
        if i < j:
            print("{}{}".format(i, j), end=end)
