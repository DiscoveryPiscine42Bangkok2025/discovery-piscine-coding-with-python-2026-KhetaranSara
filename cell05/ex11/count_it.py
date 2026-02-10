import sys

if len(sys.argv) < 2:
    print("none")
else:
    num_params = len(sys.argv) - 1
    print(f"parameters: {num_params}")
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")