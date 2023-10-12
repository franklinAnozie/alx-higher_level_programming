#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    score = 0
    weight = 0
    if my_list is not None:
        for i in range(len(my_list)):
            score = score + my_list[i][0] * my_list[i][1]
            weight += my_list[i][1]
        average = score / weight
    return average
