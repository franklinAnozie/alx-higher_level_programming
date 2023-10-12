#!/usr/bin/python3
def best_score(a_dictionary):
    biggest_key = None
    if a_dictionary is not None:
        biggest = 0
        for key, value in a_dictionary.items():
            if a_dictionary[key] > biggest:
                biggest = value
                biggest_key = key

    return biggest_key


if __name__ == "__main__":
    best_score()
