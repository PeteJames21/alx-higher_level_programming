#!/usr/bin/python3

def no_c(my_string):
    s = ""
    for char in my_string:
        if char not in "cC":
            s += char

    return s
#!/usr/bin/python3
