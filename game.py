import os
def two_player(game,turn,w_move,error,start = False):
    if start:
        print("Player 1 is 'X' and Player 2 is 'O'\nTo make a move enter row and column number")
        print("First Input row then input column seperated with a column\n")
        print_board(game)
    else:
        os.system('cls')
        print_board(game)
    if w_move:
        print("That place already taken, Choose anothe place\n")
    if error:
        print(" Wrong Input Enter Again")
    if turn:
        step = input("Player 1 =>")
    else:
        step = input("Player 2 =>")
    row,column = map(int,step.split(" "))
    if row in [0,1,2] and column  in [0,1,2]:
        if game[row][column] != 0:
            os.system('cls')
            print_board(game)
            two_player(game,turn,1,False)
        else:
            os.system('cls')
            if turn:game[row][column]=1
            else:game[row][column]=-1
            if check_win(game):
                print_board(game)
                if turn:
                    print("player 1 Won!")
                else:
                    print("Player 2 won!")
            else:
                two_player(game,not turn,0,False)
    else:
        two_player(game,turn,0,True)

def check_win(game):
    win = False
    if game[1][1] !=0:
        if game[0][0]==game[1][1] and game[1][1]==game[2][2]:
            win = True
        elif game[0][2]==game[1][1] and game[11]==game[2][0]:
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

game = [[ 0, 0, 0 ],
        [ 0, 0, 0 ],
        [ 0, 0, 0 ],]
two_player(game,True,0,False,True)