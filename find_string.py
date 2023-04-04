'''hackerrank "Find a string" challenge '''

def count_substring(string, sub_string):
    count = 0
    index_found = string.find(sub_string)
    if index_found == -1:
        return 0
    else: count += 1
    while True:
        index_found = string.find(sub_string, index_found + 1)
        if index_found == -1:
            break
        count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)