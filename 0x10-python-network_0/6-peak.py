#!/usr/bin/python3

def find_peak(list_of_integers):
    l = list_of_integers
    m = len(l) // 2

    if not l:
        return None
    elif (l[m] >= l[m-1]) and (l[m] >= l[m+1]):
        return l[m]
    elif l[0] >= l[1]:
        return l[0]
    elif l[-1] >= l[-2]:
        return l[-1]
    elif (m > 0) and (l[m] <= l[m-1]):
        i = m - 1
        while i > 0:
            if l[i] >= l[i - 1]:
                return l[i]
            i = i - 1
    else:
        i = m + 1
        while i < (len(l) - 1):
            if l[i] >= l[i + 1]:
                return l[i]
            i = i + 1
