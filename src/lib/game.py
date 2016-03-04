import random


class Game(object):
    def __init__(self, us):
        self.__board = ["..."] * 10
        self.__userSymbol = us
        self.__botSymbol = self.getBotSymbol()

    def getUserSymbol(self):
        return self.__userSymbol

    def isSpaceFree(self, param):
        return self.__board[param] == "..."

    def makeMove(self, move, symbol):
        if self.isSpaceFree(move):
            self.__board[move] = str(symbol)

    def isBoardFull(self):
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def getBotSymbol(self):
        symbols = {"O": "X", "X": "O"}
        return symbols[self.__userSymbol]

    def isWinner(self, symbol):
        return ((self.__board[7] == symbol and self.__board[8] == symbol and self.__board[9] == symbol) or
                (self.__board[4] == symbol and self.__board[5] == symbol and self.__board[6] == symbol) or
                (self.__board[1] == symbol and self.__board[2] == symbol and self.__board[3] == symbol) or
                (self.__board[7] == symbol and self.__board[4] == symbol and self.__board[1] == symbol) or
                (self.__board[8] == symbol and self.__board[5] == symbol and self.__board[2] == symbol) or
                (self.__board[9] == symbol and self.__board[6] == symbol and self.__board[3] == symbol) or
                (self.__board[7] == symbol and self.__board[5] == symbol and self.__board[3] == symbol) or
                (self.__board[9] == symbol and self.__board[5] == symbol and self.__board[1] == symbol))

    def getRandomMoveFromList(self, list):
        possibleMoves = []
        for i in list:
            if self.isSpaceFree(i):
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def __canWiniInNextRound(self, symbol):
        for i in range(1, 10):
            copy = self.__board[:]
            dummy = Game(symbol)
            dummy.__board = copy
            if dummy.isSpaceFree(i):
                dummy.makeMove(i, symbol)
            if dummy.isWinner(symbol):
                return i

    def getBotMove(self):
        if self.__canWiniInNextRound(self.__botSymbol) != None:
            return self.__canWiniInNextRound(self.__botSymbol)
        if self.__canWiniInNextRound(self.__userSymbol) != None:
            return self.__canWiniInNextRound(self.__userSymbol)
        if self.isSpaceFree(5):
            return 5
        move = self.getRandomMoveFromList([1, 3, 7, 9])
        if move != None:
            return move
        return self.getRandomMoveFromList([2, 4, 6, 8])

    def getInitialMove(self):
        if random.randint(0, 1) == 0:
            return "Bot"
        return "Player"

    def getBoard(self):
        return self.__board[:]
