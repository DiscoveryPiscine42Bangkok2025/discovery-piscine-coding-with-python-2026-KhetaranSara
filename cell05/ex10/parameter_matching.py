import sys

if len(sys.argv) == 2:
    param = sys.argv[1]
    user_word = input("What was the parameter? ")
    if user_word == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")