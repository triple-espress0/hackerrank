'''hackerrank "Lists" challenge '''


ls_exercise = list()
commands = list()
n = int(input())
for _ in range(n):    
    commands.append(input().split(' '))

for command in commands:
    if len(command) == 1:
        if command[0] == 'print':
            exec(f"{command[0]}{'(ls_exercise)'}")
        else:
            exec(f"ls_exercise{'.'}{command[0]}{'()'}")
    else:
        exec(f"ls_exercise{'.'}{command[0]}{'('}{','.join(command[1:])}{')'}")
