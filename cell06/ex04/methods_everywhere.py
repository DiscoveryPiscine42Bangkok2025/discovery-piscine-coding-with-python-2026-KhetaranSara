#!/usr/bin/env py
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    needed = 8 - len(s)
    print(s + ('Z' * needed))

def main():
    if len(sys.argv) < 2:
        print("none")
        return
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

main()