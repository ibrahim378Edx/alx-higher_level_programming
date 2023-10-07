#!/usr/bin/python3
"""
module to add new line at . / ? / :
    * There should be no space at the beginning or
    at the end of each printed line

"""


def text_indentation(text):
    """

    Prints a text with indentation

    Args:
        text : the text to work on

    Raises:
        TypeError: If `text` isn't string.

    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    text_length = len(text)
    idx = 0
    new_string = ''
    starting = True

    while idx < text_length:
        if text[idx] == ' ' and starting is True:
            idx += 1
            continue

        starting = False

        if text[idx] in '.?:':
            new_string += text[idx]
            new_string += '\n'
            new_string += '\n'
            idx += 1

            while idx < text_length and text[idx] == ' ':
                idx += 1

            continue

        if idx < text_length:
            new_string += text[idx]
            idx += 1

    print(new_string, end='')
