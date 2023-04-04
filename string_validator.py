'''hackerrank "String Validators" challenge '''

if __name__ == '__main__':
    s = input()    
    result = [False for i in list(range(5))]

    for char in list(s):
        if str(char).isalnum(): 
            if result[0] is False:
                result[0] = True
        if str(char).isalpha(): 
            if result[1] is False:
                result[1] = True
        if str(char).isdigit(): 
            if result[2] is False:
                result[2] = True
        if str(char).islower(): 
            if result[3] is False:
                result[3] = True
        if str(char).isupper(): 
            if result[4] is False:
                result[4] = True

    print('\n'.join(result))
    