import random
import random as r


class Game:

    def __init__(self, n):
        self.width = n
        self.height = n
        self.board = [[0 for i in range(self.width)] for j in range(self.height)]
        self.preset = [[False for i in range(self.width)] for j in range(self.height)]
        self.randomize()

    def randomize(self):
        possible_amount_of_clues = [18, 19, 20]
        amount_of_clues = possible_amount_of_clues[random.randrange(0, 3, 1)]
        count = 0
        probability = amount_of_clues / (self.width * self.height)

        for i in range(self.height):
            for j in range(self.width):
                self.preset[i][j] = False
                self.board[i][j] = 0
        while count < amount_of_clues:
            for i in range(self.height):
                for j in range(self.width):
                    n = r.random()
                    if n < probability:
                        num = r.randrange(1, 10, 1)
                        while not self.can_be_placed(i, j, num):
                            num = r.randrange(1, 10, 1)
                        self.preset[i][j] = True
                        self.board[i][j] = num
                        count += 1
                        if count == amount_of_clues:
                            return count
        return count

    def is_solved(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0: return False
                if not self.can_be_placed(i, j, self.board[i][j]):
                    return False
        return True

    def enter_number(self, i, j, num):
        if self.preset[i][j]:
            return
        self.board[i][j] = num

    def can_be_placed(self, i, j, num):
        if num < 1 or num > 9:
            return False
        for k in range(self.width):
            if self.board[i][k] == num and k != j:
                return False
            if self.board[k][j] == num and k != i:
                return False
        square_x = j // 3
        square_y = i // 3
        for a in range(3):
            for b in range(3):
                row = square_y * 3 + a
                col = square_x * 3 + b
                if self.board[row][col] == num:
                    if row != i or col != j:
                        return False

        return True
