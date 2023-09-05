#!/usr/bin/python3
"""
Define a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
"""


def text_indentation(text):
    """Print text with each `.` , `?`, and `:` followed by 2 newlines."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    chars = ".?:"
    i = 0
    while i < len(text):
        if text[i] in chars:
            print(text[i], end="\n\n")
            i += 1
            # Skip whitespaces that come after the special chars.
            while text[i] == " ":
                i += 1
            continue

        print(text[i], end="")
        i += 1

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")