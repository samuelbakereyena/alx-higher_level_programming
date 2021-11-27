#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bg = -1
    bk = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > bg:
            bk = a_dictionary[key]
            bk = key
            return bk
