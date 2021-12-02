#!/usr/bin/python3

import os

data = open('input.txt', 'r')

increase = 0
decrease = 0
temp = 0

iterator = iter(data)
done_loop = False
while not done_loop:
    try:
        item = int(next(iterator))
    except StopIteration:
        done_loop = True
    else:
        if temp < item:
            increase += 1

        if temp > item:
            decrease += 1
        temp = item

print(increase-1)
print(decrease-1)
        
    