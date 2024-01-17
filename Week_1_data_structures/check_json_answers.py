#!/usr/bin/env python3
# Just a helper function to check if two json files are the same

import numpy as np
import json as json

# Compare dictionaries or data to files
def compare_files(student_answer, soln_file_name):
    # Student is always the first argument
    student = student_answer
    # If it's a file name, then load that file
    if isinstance(student_answer, str):
        with open("Data/" + student_answer, "r") as fp:
            student = json.load(fp)

    # Second filename is always the solution, stored in a file or a dictionary. Load it if it is a file.
    soln = soln_file_name
    if isinstance(soln_file_name, str):
        with open("Data/" + soln_file_name, "r") as fp:
            soln = json.load(fp)

    # If soln is a dictionary, then do the first if statement
    if isinstance(soln, dict):
        # Loop through all elements of the dictionary
        for k, v in soln.items():
            try:
                if k == "Data channels":
                    # The data channels list
                    for i, d in enumerate(student[k]):
                        if d != v[i]:
                            print(f"miss-match value {d} {v[i]}")
                            return False
                else:
                    if v != student[k]:
                        print(f"Miss-match key-item {k} {v} {student[k]}")
                        return False
            except KeyError:
                print(f"Missing key {k}")
                return False
        return True
    else:
        # soln is a list.
        if len(soln) != len(student):   # Check lists are same length
            print(f"Mismatched number of elements, solution {len(soln)} yours {len(student)}")            
            return False

        # For each item in each list
        for ce, cs in zip(soln, student):
            # Each item is a dictionary - loop through the solution keys
            for k, v in ce.items():
                try:
                    # Check if the values in the keys are similar
                    if not np.isclose(v, cs[k], atol=0.01):
                        print(f"Value for key {k} is {cs[k]}, expected {v}")
                        return False
                except KeyError:
                    print(f"Missing key {k} or not a number {cs[k]}")
                    return False
    return True
        
    
