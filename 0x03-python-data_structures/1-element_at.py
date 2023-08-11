#!/usr/bin/python3

def element_at(my_list, idx):
    len_ = len(my_list)
    if idx < 0 or idx >= len_ or len_ == 0:
        return None

    return my_list[idx]
