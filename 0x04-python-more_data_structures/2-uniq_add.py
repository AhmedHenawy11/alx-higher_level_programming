#!/usr/bin/python3
def uniq_add(my_list=[]):
    list = set(my_list.copy())
    sum = 0
    for i in list:
        sum += i
    return sum
