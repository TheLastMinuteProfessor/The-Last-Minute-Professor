"""
For step by step explanation, do visit

"""
import random
def user_turn(status):
    r=int(input("Enter row number"))
    c=int(input("Enter column number"))
    while r<0 or r>2 or c<0 or c>2 or status[r][c]!="~":
        r=int(input("Enter row number"))
        c=int(input("Enter column number"))
    status[r][c]="X"
    return status
def computer_turn(status):
    r=random.randint(0,2)
    c=random.randint(0,2)
    while status[r][c]!="~":
        r=random.randint(0,2)
        c=random.randint(0,2)
    status[r][c]="O"
    return status
def display_board(status):
    print("Board:")
    for i in range(3):
        print(end="  ")
        for j in range(3):
            print(status[i][j],end=" ")
            if j<2:
                print("|",end="  ")
        print()
        if i<2:
            print("——+——+——") 
    return status
def is_game_over(status,player):
    #DIAGONAL
    for i in range(3):
        if status[i][i]!=player:
            break
    else:
        return 1
    #Other diagonal
    i=2
    for j in range(3):
        if status[i][j]!=player:
            break
        i=i-1
    else:
        return 1
    #Row win?
    for i in range(3):
        for j in range(3):
            if status[i][j]!=player:
                break
        else:
            return 1
    #Column win?
    for i in range(3):
        for j in range(3):
            if status[j][i]!=player:
                break
        else:
            return 1
    return 0
status=[["~","~","~"],["~","~","~"],["~","~","~"]]
turn=1
while turn<10:
    if turn%2==1:
        status=user_turn(status)
        display_board(status)
        if (is_game_over(status,"X")):
            print("Game Over! You won!")
            break
    else:
        status=computer_turn(status)
        display_board(status)
        if (is_game_over(status,"O")):
            print("Game Over! Computer won!")
            break
    turn=turn+1
else:
    print("Game Over! No Winner!")
