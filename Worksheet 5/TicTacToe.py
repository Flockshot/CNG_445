class TicTacToe:

    def __init__(self):
        self.board = [['_' for i in range(3)] for i in range(3)]
        self.turn = 1
        self.finished = False

    def playPlayerTurn(self, row, col):
        row -= 1
        col -= 1
        if self.finished:
            raise Exception("Game Over!")
        if row < 0 or row >= 3 or col < 0 or col >= 3 or self.board[row][col] != '_':
            raise Exception("Incorrect Input")

        self.board[row][col] = "X" if self.turn % 2 == 1 else "O"
        self.turn += 1

        if self.check_win('X'):
            print("Player 1 won!")
            self.finished = True
        elif self.check_win('O'):
            print("Player 2 won!")
            self.finished = True
        elif self.isBoardFull():
            print("Draw!")
            self.finished = True


    def check_win(self, player):

        size = 3

        # Check horizontally
        for x in range(size):
            horizontal = True
            for y in range(size):
                horizontal = horizontal and player == self.board[x][y]
            if horizontal:
                return True

        # Check vertically
        for y in range(size):
            vertical = True
            for x in range(size):
                vertical = vertical and player == self.board[x][y]
            if vertical:
                return True

        # Check diagonally
        diagonal = True
        diagonal1 = True

        for x in range(size):
            diagonal = diagonal and player == self.board[x][x]
        for (x,y) in (range(3), range(2, -1, -1)):
            diagonal1 = diagonal1 and player == self.board[x][y]

        if diagonal or diagonal1:
            return True

        return False

    def isBoardFull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    return False
        return True

    def isFinished(self):
        return self.finished

    def printBoard(self):
        print("-------------\n")
        for i in range(3):
            for j in range(3):
                print("| {} ".format(self.board[i][j]), end="")
            print("|\n")
            print("-------------\n\n")

