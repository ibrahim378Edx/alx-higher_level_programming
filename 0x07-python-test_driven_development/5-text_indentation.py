#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """Print newline after  '.', '?', and ':'.

    Args:
        text : txt to scan
    Raises:
        TypeError: if no txt
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        z += 1

    while z < len(text):
        print(text[z], end="")
        if text[z] == "\n" or text[c] in ".?:":
            if text[z] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
