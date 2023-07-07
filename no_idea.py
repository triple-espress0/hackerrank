'''"""hackerrank "No idea" challenge """'''
from collections import Counter


m, n = map(int, input().split())

arr_counter = dict(Counter(input().split()))

happiness = 0

set_a = set(input().split())
set_b = set(input().split())

happiness += sum(
    {
        k: v if k in set_a else v * -1 if k in set_b else 0
        for k, v in arr_counter.items()
    }.values()
)

print(happiness)
