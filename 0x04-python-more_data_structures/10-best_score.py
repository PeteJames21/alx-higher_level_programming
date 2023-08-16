#!/usr/bin/python3

def best_score(a_dictionary):
    """Return the key with the biggest integer value."""
    if not a_dictionary:
        return None

    key_max = None
    for k, v in a_dictionary.items():
        if key_max is None:
            val_max = v
            key_max = k

        if v > val_max:
            key_max = k
            val_max = v

    return key_max
