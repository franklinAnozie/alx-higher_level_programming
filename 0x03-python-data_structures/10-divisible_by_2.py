#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        new_list.append(i)
    for i in range(len(new_list)):
        if new_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list


if __name__ == "__main__":
    divisible_by_2()
