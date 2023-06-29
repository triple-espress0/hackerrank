"""hackerrank "Maximize it" challenge """
from itertools import product


count_denominator = input().split()
input_lists = list()

for _ in range(int(count_denominator[0])):
    current_input = input().split()
    input_lists.append(current_input[1:])


power_lists = [[pow(int(i), 2) for i in sublist] for sublist in input_lists]


max_s = 0
for item in list(product(*power_lists)):
    if sum(item) % int(count_denominator[1]) > max_s:
        max_s = sum(item) % int(count_denominator[1])

print(max_s)
