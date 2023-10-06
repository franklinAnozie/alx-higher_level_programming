#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

length = len(argv)
len_gth = length - 1

if len_gth == 1:
    print("{} argument:".format(len_gth))
elif len_gth == 0:
    print("{} arguments.".format(len_gth))
else:
    print("{} arguments:".format(len_gth))

if len_gth > 0:
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))
