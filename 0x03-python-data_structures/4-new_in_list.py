#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    file = my_list.copy()
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list) - 1:
        return my_list
    else:
        file[idx] = element
        return file
