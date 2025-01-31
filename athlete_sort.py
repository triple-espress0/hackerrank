"""hackerrank 'Athlete sort' challenge """

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    arr_sorted = sorted(arr, key=lambda x: x[k])

    for i in range(n):
        print(*[*arr_sorted[i]])
