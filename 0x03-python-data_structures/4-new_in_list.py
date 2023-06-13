#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if (len(my_list) - 1) < idx < 0:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
