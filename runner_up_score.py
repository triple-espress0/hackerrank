'''hackerrank "Find the Runner-Up Score!" challenge '''

n = int(input())
arr = map(int, input().split())
ls_nums = list(arr)
ls_nums.sort()
ls_nums.c

print(ls_nums[n - ls_nums.count(max(ls_nums)) - 1])
