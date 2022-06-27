#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < len(my_list) and idx > 0:
        for i in my_list:
            if i == idx:
                my_list[idx] = element
    return my_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
