'''hackerrank "Minnion Game" challenge '''

def minion_game(string):
    
    player_1_count = 0
    player_2_count = 0
    for i in range(len(string)):
        if string[i] in "AIEOU":
            player_1_count += len(string) - i
        else:
            player_2_count += len(string) - i
    
    if player_1_count > player_2_count:
        print('Kevin' + ' ' + str(player_1_count))
    elif player_2_count > player_1_count:
        print('Stuart' + ' ' + str(player_2_count))
    else:
        print('Draw')
        
if __name__ == '__main__':
    s = input()
    minion_game(s)