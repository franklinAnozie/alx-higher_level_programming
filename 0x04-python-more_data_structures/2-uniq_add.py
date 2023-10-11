#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
    print(new_list)
    sum = 0
    for i in range(len(new_list)):
        sum += new_list[i]
    
    return sum


if __name__ == "__main__":
    uniq_add()