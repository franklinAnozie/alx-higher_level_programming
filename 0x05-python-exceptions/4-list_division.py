#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div = 0
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
            div = 0
    return new_list


if __name__ == "__main__":
    list_division()
