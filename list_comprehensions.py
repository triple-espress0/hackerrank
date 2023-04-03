'''hackerrank "List Comprehensions" challenge '''

x = int(input())
y = int(input())
z = int(input())
n = int(input())

ls_coordinates = [[a, b, c] for a in list(range(x+1)) for b in list(range(y+1)) for c in list(range(z+1)) if a+b+c != n]

print(ls_coordinates)
