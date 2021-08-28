import os
from random import randint

def print_board(board):
    print("    0   1   2\n")
    for count, row in enumerate(board):
        print(count,end="  ")
        for i in range(len(row)):
            if row[i]==1:
                print(f" X ",end="")
            elif row[i]==-1:
                print(f" O ",end="")
            else:
                print(f"   ",end="")
            if i!=2:
                print("|",end="")
            else:
                print("")
        if count!=2:
            print("   -----------")
    print("")

def check_tie(game):
    for row in game:
        if 0 in row:
            return False
    return True

def check_win(game):
    win = False
    if game[1][1] !=0:
        if game[0][0]==game[1][1] and game[1][1]==game[2][2]:
            win = True
        elif game[0][2]==game[1][1] and game[1][1]==game[2][0]:
            win = True
        if win:
            return win
    l=[0,0,0]
    for row in game:
        if (1 not in row or -1 not in row) and 0 not in row:
            win = True
            return win
        else:
            for i in range(3):
                if row[i]!=0:
                    l[i]+=row[i]
    if -3 in l or 3 in l:
        win = True
    return win

def computer_game(game,turn):
    # Checking diagonals
    if sum([game[0][0],game[1][1],game[2][2]]) == 2 or sum([game[0][0],game[1][1],game[2][2]]) == -2:
        for i in range(len(game)):
            if game[i][i] == 0:
                if turn:game[i][i]=1
                else : game[i][i]=-1
                return game
    elif sum([game[0][2],game[1][1],game[2][0]]) == 2 or sum([game[0][2],game[1][1],game[2][0]]) == -2:
        j=2
        for i in range(len(game)):
            if game[i][j] == 0:
                if turn:game[i][j]=1
                else : game[i][j]=-1
                return game
            j-=1
    # checking rows
    if turn:
        a=[sum(game[0]),sum(game[1]),sum(game[2])]
        if 2 in a:
            j=a.index(2)
            for i in range(3):
                if game[j][i]==0:
                    game[j][i]=-1
                    return game
        elif -2 in a:
            j=a.index(-2)
            for i in range(3):
                if game[j][i]==0:
                    game[j][i]=1
                    return game
    else:
        a=[sum(game[0]),sum(game[1]),sum(game[2])]
        if -2 in a:
            j=a.index(-2)
            for i in range(3):
                if game[j][i]==0:
                    game[j][i]=1
                    return game
        elif 2 in a:
            j=a.index(2)
            for i in range(3):
                if game[j][i]==0:
                    game[j][i]=-1
                    return game
    # Checking columns
    l=[0,0,0]
    for row in game:
        for i in range(3):
                if row[i]!=0:
                    l[i]+=row[i]
    if turn:
        if 2 in l:
            for i in range(3):
                if l[i] == 2 :
                    for row in game:
                        if row[i] == 0:
                            row[i]=1
                            return game
        elif -2 in l:
            for i in range(3):
                if l[i]==-2:
                    for row in game:
                        if row[i] == 0:
                            row[i]=1
                            return game
    else:
        if -2 in l:
            for i in range(3):
                if l[i] == -2 :
                    for row in game:
                        if row[i] == 0:
                            row[i]=-1
                            return game
        elif 2 in l:
            for i in range(3):
                if l[i]==2:
                    for row in game:
                        if row[i] == 0:
                            row[i]=-1
                            return game

    if sum([sum(game[0]),sum(game[1]),sum(game[2])]) ==1:
        if (game[0][1] == 1 and game[1][2] == 1) or (game[1][0] == 1 and game[2][1] == 1 ):
            a=randint(0,1)
            if a:game[0][0]=-1
            else:game[2][2]=-1
            return game
        elif (game[0][1] == 1 and game[1][0] == 1) or (game[1][2] == 1 and game[2][1] == 1 ):
            a=randint(0,1)
            if a:game[2][0]=-1
            else:game[0][2]=-1
            return game
    
    if game[1][1]==-1:
        if (game[0][0]==1 and game[2][2]==1) or (game[2][0]==1 and game[0][2]==1):
            p=[[1,0],[1,2],[2,1],[0,1]]
            a=randint(0,4)
            i,j=p[a]
            game[i][j]=-1
            return game

    if game[0][0]==0 or game[1][1]==0 or game[2][2]==0 or game[2][0]==0 or game[0][2]==0:
        if sum([sum(game[0]),sum(game[1]),sum(game[2])]) != 0 and game[1][1] == 0:
            if turn:game[1][1]=1
            else:game[1][1]=-1
        else:
            p=[[0,0],[1,1],[2,2],[2,0],[0,2]]
            while True:
                a=randint(0,len(p)-1)
                i,j=p[a]
                if game[i][j]==0:
                    if turn:
                        game[i][j]=1
                    else:
                        game[i][j]=-1  
                    break
                else:
                    p.pop(a)
    else:
        for row in game:
            for i in row:
                if row[i]==0:
                    if turn : row[i]=1
                    else: row[i]=-1
    return game

def two_player(game,turn,w_move,error,player,start = False):
    if start:
        print("Player 1 is 'X' and Player 2 is 'O'\nTo make a move enter row and column number")
        print("First Input row then input column seperated with a column\n")
    else:
        os.system('cls')
    print_board(game)
    print(game)
    if w_move:
        print("That place already taken, Choose anothe place\n")
    if error:
        print(" Wrong Input Enter Again")
    if player:
        if turn:
            step = input("Player 1 =>")
        else:
            step = input("Player 2 =>")
    else:
        if turn:
            step = input("Player's Turn =>")
        else:
            game = computer_game(game,turn)
            if check_win(game):
                os.system('cls')
                print_board(game)
                if turn:
                    print("player 1 Won!")
                    return 0
                else:
                    print("CPU won!")
                    return 0
            else:
                if not check_tie(game):
                    two_player(game,not turn,0,False,player)
                    return 0
                else:
                    os.system('cls')
                    print_board(game)
                    print("It's a Tie")
                    return 0
    if not(not player and not turn):
        try:
            row,column = map(int,step.split(" "))
        except:
            two_player(game,turn,0,True,player)
            return 0
        if row in [0,1,2] and column  in [0,1,2]:
            if game[row][column] != 0 :
                os.system('cls')
                print_board(game)
                two_player(game,turn,1,False,player)
                return 0
            else:
                os.system('cls')
                if turn:game[row][column]=1
                else:game[row][column]=-1
                if check_win(game):
                    print_board(game)
                    if turn:
                        print("player 1 Won!")
                        return 0
                    else:
                        print("Player 2 won!")
                        return 0
                else:
                    if not check_tie(game):
                        two_player(game,not turn,0,False,player)
                        return 0
                    else:
                        print_board(game)
                        print("It's a Tie")
                        return 0
        else:
            two_player(game,turn,0,True,player)
            return 0

if __name__=="__main__":
    game = [[ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ]]
    while True:
        player = int(input("Choose one of the following:\n1.P v P\n2.CPU vs P\n=> "))
        if player == 1:
            two_player(game,True,0,False,True,True)
            break
        elif player == 2:
            two_player(game,randint(0,1),0,False,False,True)
            break
        else:
            print("Wrong input! Enter Again")