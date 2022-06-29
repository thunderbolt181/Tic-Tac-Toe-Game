# Tic-Tac-Toe-Game
=> A basic tic tac toe game in Python with two modes. 
- AI vs P
- PvP

**This code is like an api. You can use specific functions for specific things**
- pvp(player, row, column) => it make a move by taking 'player', 'row' and 'column' as parameters.
- AI() => it returns 'row' and 'column' number at which AI wants to make its move.
- check_win() => Checks if game has been finished by a win or not.
- check_tie() => Checks if game has been finished by a tie.
- check_pos(row, column) => Checks if given position is empty or not by taking 'row' and 'column' as parameters.

## AI
- It uses Minimax Algorithm to predict its move.
- Scope of improvements:
    - Implementing depth for decreasing time for 1st move.
    - Using Alpha-Beta Pruning for decreasing overall time.

**For working Example You can refer to {if __name__=="__main__":} block in the code.**
