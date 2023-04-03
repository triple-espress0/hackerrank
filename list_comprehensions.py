'''hackerrank "List Comprehensions" challenge '''

x, y, z, n = (int(input()) for _ in range(4))

ls_coordinates = [[a, b, c] for a in list(range(x+1)) for b in list(range(y+1)) for c in list(range(z+1)) if a+b+c != n]

print(ls_coordinates)
