'''hackerrank "Tuples" challenge '''

n = int(input())

ls_numbers = list(input().split())
for i, v in enumerate(ls_numbers):
    ls_numbers[i] = int(v)

t = tuple(ls_numbers)
print(hash(t))
