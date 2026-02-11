#!/usr/bin/env py

def add_one(x):
    x = x + 1
    return x

my_number = 10
print(f"Before calling method: {my_number}")
add_one(my_number)
print(f"After calling method:  {my_number}")