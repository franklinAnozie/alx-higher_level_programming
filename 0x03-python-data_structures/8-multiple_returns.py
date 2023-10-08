#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_xter = None
    else:
        first_xter = sentence[0]

    rtVal = (length, first_xter)

    return rtVal


if __name__ == "__main__":
    multiple_returns()
