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

    return s_capitalized


if __name__ == "__main__":
    os.environ["OUTPUT_PATH"] = os.getcwd() + "/foo.txt"
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    fptr.write(result + "\n")

    fptr.close()
