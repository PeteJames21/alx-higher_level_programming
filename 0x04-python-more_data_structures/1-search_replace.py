#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurences of an element with a specified value.

    :param my_list: list containing the data
    :param search: element to be replaced
    :param replace: element to use as replacement
    """
    return [i if i != search else replace for i in my_list]
