import os
import pyautogui
import time
import sys

if sys.version_info[0] != 3 and sys.version_info[1] != 10:
    raise Exception("Python3.10 is needed to run this program!")

class tic_tac_toe_game:
    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append(str(i + 1))

    def start(self):
        turn = 'X'
        winner = 'None'
        wrong = False

        self.clear_console()
        self.print_board()

        while winner == 'None':
            if wrong:
                self.clear_last_line()
                wrong = False
            self.print(f'Enter integer to place {turn} into: ', 'red')
            try:
                temp = int(input())
            except ValueError:
                wrong = True
            self.print('\n', 'yellow')

            if temp < 1 or temp > 9 or self.board[temp - 1] == 'X' or self.board[temp - 1] == 'O':
                wrong = True
                continue
            
            self.board[temp - 1] = turn
            turn = 'X' if turn == 'O' else 'O'

            winner = self.check_winner()
            self.clear_console()
            self.print_board()

        self.clear_console()
        self.print(f'\rWinner: {winner}', 'purple')
        time.sleep(3)
        self.clear_console()

    def clear_last_line(self):
        self.clear_console()
        self.print_board()

    def print_board(self):
        counter = 0
        for i in range(7):
            if i % 2 == 0:
                self.print('|---|---|---|\n', 'yellow')
            else:
                self.print('|', 'yellow')
                self.print(self.board[counter], 'red')
                self.print('|', 'yellow')
                self.print(self.board[counter + 1], 'red')
                self.print('|', 'yellow')
                self.print(self.board[counter + 2], 'red')
                self.print('|\n', 'yellow')
                counter += 3
    
    def check_winner(self):
        counter = 0
        
        for i in range(9):
            if i == 0:
                line = self.board[0] + self.board[1] + self.board[2]
            elif i == 1:
                line = self.board[3] + self.board[4] + self.board[5]
            elif i == 2:
                line = self.board[6] + self.board[7] + self.board[8]
            elif i == 3:
                line = self.board[0] + self.board[3] + self.board[6]
            elif i == 4:
                line = self.board[1] + self.board[4] + self.board[7]
            elif i == 5:
                line = self.board[2] + self.board[5] + self.board[8]
            elif i == 6:
                line = self.board[0] + self.board[4] + self.board[8]
            elif i == 7:
                line = self.board[2] + self.board[4] + self.board[6]

            if line == 'XXX':
                return 'X'
            elif line == 'OOO':
                return 'O'

            if str(i + 1) == self.board[i]:
                counter += 1
        
        if counter == 0:
            return 'Draw'

        return 'None'

    def clear_console(self):
        os.system('cls' if 'nt' in os.name else 'clear')
    
    def print(self, text, color):
        match color:
            case 'red':
                print(f'\033[1;31m {text}', end='')
            case 'yellow':
                print(f'\033[1;33m {text}', end='')
            case 'purple':
                print(f'\033[1;35m {text}', end='')
            case _:
                return


if __name__ == '__main__':
    game = tic_tac_toe_game()
    game.start()
    
