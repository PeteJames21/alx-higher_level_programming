#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    args = [tuple_a, tuple_b]
    for i in range(2):
        if len(args[i]) == 0:
            args[i] = (0, 0)
        elif len(args[i]) == 1:
            tmp = args[i]
            args[i] = (tmp[0], 0)

    t1, t2 = args

    return (t1[0] + t2[0], t1[1] + t2[1])
