"""hackerrank "String formatting" challenge """


def print_formatted(number):
    f_len = len(bin(number)) - 2
    for i in range(1, number + 1):
        f_oct = oct(i)
        f_hex = hex(i)
        f_bin = bin(i)

        print(
            f"{str(i).rjust(f_len)} {f_oct[2:].rjust(f_len)} {f_hex[2:].upper().rjust(f_len)} {f_bin[2:].rjust(f_len)}"
        )


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
