#!/usr/bin/python3
# Advent of Code Day 2
# https://adventofcode.com/2021/day/2
# Richard Y


# Part I

import os

data = open('input.txt', 'r')
forward = 0
up = 0
down = 0

lines = data.readlines()

for line in lines:    
    if line.split()[0] == "forward":
        forward += int(line.split()[1])
    if line.split()[0] == "down":
        down += int(line.split()[1])
    if line.split()[0] == "up":
        up += int(line.split()[1])

horizontal = down - up

print (forward * horizontal)

# Part 2

data = open('input.txt', 'r')
horizontal = 0
aim = 0
depth = 0

lines = data.readlines()

for line in lines:    
    if line.split()[0] == "forward":
        horizontal += int(line.split()[1])
        depth += aim * int(line.split()[1])
    if line.split()[0] == "down":
        aim += int(line.split()[1])
    if line.split()[0] == "up":
        aim -= int(line.split()[1])
    
print (depth * horizontal)

