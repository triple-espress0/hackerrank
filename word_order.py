'''"""hackerrank "Word order" challenge """'''
from collections import Counter

n = int(input().rstrip())
ls_words = []
for _ in range(n):
    ls_words.append(input().rstrip())

counter_words = Counter(ls_words)

print(len(counter_words))
print(*[v for k, v in counter_words])
