"""hackerrank 'Map and Lambda Function' challenge """
cube = lambda x: x**3


def fibonacci(n):
    if n > 1:
        fibs = [0, 1]
        for i in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])
    elif n == 1:
        fibs = [0]
    elif n == 0:
        fibs = []

    return fibs


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
