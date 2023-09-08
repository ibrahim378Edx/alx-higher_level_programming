#!/usr/bin/python3

if __name__ == "__main__":
    """

    Print all names in hidden4

    """
    import hidden_4

    namer = dir(hidden_4)
    for name in namer:
        if name[:2] != "__":
            print(name)
