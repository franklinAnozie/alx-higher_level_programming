#!/usr/bin/python3
""" stats module """
from sys import stdin


if __name__ == "__main__":
    """ stats module """
    count = 0
    size = 0
    status = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in stdin:
            count += 1
            data = line.split()
            if len(data) > 2:
                size += int(data[-1])
                if data[-2] in status:
                    status[data[-2]] += 1
            if count % 10 == 0:
                print("File size: {}".format(size))
                for key in sorted(status.keys()):
                    if status[key] != 0:
                        print("{}: {}".format(key, status[key]))
    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key in sorted(status.keys()):
            if status[key] != 0:
                print("{}: {}".format(key, status[key]))
        raise
    print("File size: {}".format(size))
    for key in sorted(status.keys()):
        if status[key] != 0:
            print("{}: {}".format(key, status[key]))
