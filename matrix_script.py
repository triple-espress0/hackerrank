"""hackerrank "Matrix script" challenge """
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

ls = [item[i] for i in range(m) for item in matrix]
s = "".join(ls)
formatted_s = re.sub(r"(?<=\w)\W+(?=\w)", " ", s)
print(formatted_s)
