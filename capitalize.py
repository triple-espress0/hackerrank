"""hackerrank "Capitalize" challenge """
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    s_capitalized = s[0].upper()

    for i in range(1, len(s)):
        if s[i - 1] == " ":
            s_capitalized = s_capitalized + s[i].upper()
        else:
            s_capitalized = s_capitalized + s[i]

    # s_split = s.split()
    # s_capitalized = list()
    # for item in s_split:
    #     s_capitalized.append(item.capitalize())
    return s_capitalized


if __name__ == "__main__":
    os.environ["OUTPUT_PATH"] = os.getcwd() + "/asd.txt"
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    fptr.write(result + "\n")

    fptr.close()
