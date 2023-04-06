'''hackerrank "Merge the Tools!" challenge '''

from textwrap import wrap

def merge_the_tools(string, k):
    split_string = wrap(string, k)
    for item in split_string:
        result = item[0]
        for i in range(len(item) - 1):
            if item[i + 1] not in result:
                result = result + item[i + 1]
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
