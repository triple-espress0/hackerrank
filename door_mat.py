'''hackerrank "Designer Door Mat" challenge '''

while True:
    height, width = [int(x) for x in input().split()]
    
    if width / height != 3.0:
        print('Height must be 3 times Width!')
        continue
    else: break

top_lines = ''
bottom_lines = ''

for i in range(height // 2):
    top_lines = f"{top_lines}{(((width // 2) - (i * 3) - 1) * '-') + '.'}{i * '|..'}{'|'}{i * '..|'}{'.' + (((width // 2) - (i * 3) - 1) * '-')}"  + '\n'
    bottom_lines = f"{bottom_lines}{(((width // 2) - ((((height //2)) - i) * 3 - 2)) * '-') + '.'}{((height //2) - i - 1) * '|..'}{'|'}{((height //2) - i - 1) * '..|'}{'.' + (((width // 2) - ((((height //2)) - i ) * 3 - 2)) * '-')}"  + '\n'

middle_line = f"{((width - 7) // 2) * '-'}{'WELCOME'}{((width - 7) // 2) * '-'}"

print(top_lines.rstrip())
print(middle_line)
print(bottom_lines.rstrip())
