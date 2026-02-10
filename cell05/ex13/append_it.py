import sys

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if arg.endswith("ism"):
            continue
        print(arg + "ism")