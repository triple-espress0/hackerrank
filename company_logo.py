"""hackerrank "Company Logo" challenge """
from collections import Counter

if __name__ == "__main__":
    s = input()
    letters = Counter(s)
    sorted_letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))

    for x, y in sorted_letters[:3]:
        print(x, y)
