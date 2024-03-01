#!/usr/bin/python
''' Finding a peak element '''


def find_peak(lst):
    """
    find_peak

    Args:
        lst (list): list of elements
    Returns:
        int: a peak element
    """
    start, end = 0, len(lst) - 1

    if len(lst) < 1:
        return None

    while start < end:
        mid = start + (end - start) // 2
        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]

        if lst[mid - 1] > lst[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return lst[start]
