#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        end = "\n"
    else:
        end = ", "
    print("{:02n}".format(i), end=end)
