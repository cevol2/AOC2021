#!/usr/bin/python3
# Advent of Code Day 1
# https://adventofcode.com/2021/day/1
# Richard Y

import os

## PART I

data = open('input.txt', 'r')

increase = 0
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

        temp = item

print(increase-1)
        
## PART II 

def push_number(number):
    my_list[0] = my_list[1]
    my_list[1] = my_list[2]
    my_list[2] = int(number)

def check_increase():
    global increase
    if not(int(my_list[0]) == 0 or int(my_list[1]) == 0 or int(my_list[2]) == 0):
        total = int(my_list[0])+int(my_list[1])+int(my_list[2])
        if array_total < total:
            increase += 1

# Reopen File
data = open('input.txt', 'r')
lines = data.readlines()

my_list = [0,0,0]
array_total = 0
increase = 0

for line in lines:
    array_total = int(my_list[0])+int(my_list[1])+int(my_list[2])
    push_number(line)
    check_increase()

print(increase-1)
