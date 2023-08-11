#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    len_ = len(my_list)
    if idx < 0 or idx >= len_ or len_ == 0:
        return my_list

    my_list[idx] = element
    return my_list
