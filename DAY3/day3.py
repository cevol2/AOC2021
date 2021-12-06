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

# Part II

data = open('input.txt', 'r')
list = data.readlines()

# Remove items from list, 
# input: list, index, binary bit 

def removeItems(list, index, binary):
    result = [x for x in list if int(x[index]) == binary]
    list = result
    return list


for x in range(12):
    one_count = 0
    zero_count = 0
    for line in list:
        if int(line[x]) == 1:
            one_count += 1
        if int(line[x]) == 0:
            zero_count += 1
    if one_count < zero_count:
        list = removeItems (list,x,0)
    if one_count > zero_count or one_count == zero_count:
        list = removeItems (list,x,1)
    if len(list) < 1:
        break

oxy_bin   = list
oxy_bin = ''.join([str(n) for n in list])

data = open('input.txt', 'r')
list = data.readlines()

for x in range(12):
    one_count = 0
    zero_count = 0
    for line in list:
        if int(line[x]) == 1:
            one_count += 1
        if int(line[x]) == 0:
            zero_count += 1
    if one_count > zero_count:
        list = removeItems (list,x,0)
    if one_count < zero_count:
        list = removeItems (list,x,1)
    if one_count == zero_count:
        list = removeItems (list,x,0)
    if len(list) < 2:
        break


co2_bin = list
co2_bin = ''.join([str(n) for n in list])

print(int(co2_bin,2) * int(oxy_bin,2))
