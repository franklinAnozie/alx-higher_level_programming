#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

length = len(argv)

if length == 1:
    print(f"{length-1} arguments.")
elif length == 2:
    print(f"{length-1} argument:")
else:
    print(f"{length-1} arguments:")

for i in range(length):
    print(f"{i}: {argv[i]}")
