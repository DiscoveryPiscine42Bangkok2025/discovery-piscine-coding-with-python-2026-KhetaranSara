import sys
if len(sys.argv) < 3:
    print("none")
else:
    params = sys.argv[1:]
    for p in reversed(params):
        print(p)