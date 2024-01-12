#!/usr/bin/env python3
# Just a helper function to check if two json files are the same

import numpy as np
import json as json


def compare_files(fname_1, fname_2):
    student = fname_1
    if isinstance(fname_1, str):
        with open("Data/" + fname_1, "r") as fp:
            student = json.load(fp)

    check = fname_2
    if isinstance(fname_2, str):
        with open("Data/" + fname_2, "r") as fp:
            check = json.load(fp)

    if isinstance(check, dict):
        for k, v in check.items():
            try:
                if k == "Data channels":
                    # The data channels list
                    for i, d in enumerate(student[k]):
                        if not d == v[i]:
                            print(f"miss-match {d} {v[i]}")
                            return False
                else:
                    if not v == student[k]:
                        print(f"Miss-match key-item {k} {v} {student[k]}")
                        return False
            except KeyError:
                print(f"Missing key {k}")
                return False
        return True
    else:
        if len(check) != len(student):
            print(f"Mismatched number of elements")            
            return False

        for ce, cs in zip(check, student):
            for k, v in ce.items():
                try:
                    if not v == cs[k]:
                        print(f"Miss-match key-item {k} {v} {cs[k]}")
                        return False
                except KeyError:
                    print(f"Missing key {k}")
                    return False
    return True
        
    
