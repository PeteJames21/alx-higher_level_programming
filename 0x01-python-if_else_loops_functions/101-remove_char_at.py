#!/usr/bin/python3

def remove_char_at(s, n):
    """Return the string `s` with the character at index `n` removed."""
    if n < 0 or n > len(s) - 1:
        return s

    s2 = ""
    i = 0
    for char in s:
        if i == n:
            pass
        else:
            s2 += char
        i += 1

    return s2
