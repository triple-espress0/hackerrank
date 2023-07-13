"""hackerrank 'Triangle quest' challenge """

for i in range(1, int(input())):
    print(
        i
        * (
            (lambda x: 1 if x >= 8 else 0)(i) * (10**7)
            + (lambda x: 1 if x >= 7 else 0)(i) * (10**6)
            + (lambda x: 1 if x >= 6 else 0)(i) * (10**5)
            + (lambda x: 1 if x >= 5 else 0)(i) * (10**4)
            + (lambda x: 1 if x >= 4 else 0)(i) * (10**3)
            + (lambda x: 1 if x >= 3 else 0)(i) * (10**2)
            + (lambda x: 1 if x >= 2 else 0)(i) * (10**1)
            + 1
        )
    )
