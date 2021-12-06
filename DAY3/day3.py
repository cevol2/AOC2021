#!/usr/bin/python3
# Advent of Code Day 3
# https://adventofcode.com/2021/day/3
# Richard Y


# Part I

data = open('input.txt', 'r')

lines = data.readlines()

gamma   =     [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon =     [0,0,0,0,0,0,0,0,0,0,0,0]
total_g =     [0,0,0,0,0,0,0,0,0,0,0,0]
total_e =     [0,0,0,0,0,0,0,0,0,0,0,0]

for line in lines:
    for x in range (12):
        if int(line[x]) == 0:
            gamma[x] += 1
        if int(line[x]) == 1:
            epsilon[x] += 1

#print(gamma)
#print(epsilon)

for x in range (12):
    if gamma[x] > epsilon[x]:
        total_g[x] = 1

for x in range(12):
    if total_g[x] == 1:
        total_e[x] = 0
    if total_g[x] == 0:
        total_e[x] = 1

gamma_bin   = ''.join([str(n) for n in total_g])
epsilon_bin = ''.join([str(n) for n in total_e])

print (int(gamma_bin, 2)*int(epsilon_bin,2))
