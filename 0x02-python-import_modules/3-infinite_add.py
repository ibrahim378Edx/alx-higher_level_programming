#!/usr/bin/python3
if __name__ == "__main__":
    """
    
    Print addition of args
    
    """
    import sys

    q = 0
    for i in range(len(sys.argv) - 1):
        q = q + int(sys.argv[i + 1])
    print("{}".format(q))
