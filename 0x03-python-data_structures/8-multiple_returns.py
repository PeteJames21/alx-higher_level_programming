#!/usr/bin/python3

def multiple_returns(sentence):
    len_s = len(sentence)
    first_char = None
    if len_s > 0:
        first_char = sentence[0]

    return (len_s, first_char)
