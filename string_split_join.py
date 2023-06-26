"""hackerrank "String Split and Join" challenge """


def split_and_join(line):
    return "-".join(line.split())


if __name__ == "__main__":
    shoes_count = input()
    shoes_assort = input().split()
    print(f"{shoes_count} + {shoes_assort}")
