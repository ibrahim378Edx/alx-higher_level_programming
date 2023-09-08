#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    namer = dir(hidden_4)

    for i in range(len(namer)):
        if namer[i][:2] != '__':
            print(namer[i])
