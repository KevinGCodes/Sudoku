class sudoku_solver:

    def __init__(self, game):
        self.game = game
        self.solution = [[0 for i in range(self.game.width)] for j in range(self.game.height)]

    def solve_recursive_helper(self, i, j, cells_left):
        if cells_left == 0 and self.game.is_solved():
            for row in range(0, self.game.height):
                for col in range(0, self.game.width):
                    self.solution[row][col] = self.game.board[row][col]
            return True
        elif cells_left > 0 and self.game.board[i][j] != 0:
            if not self.game.can_be_placed(i, j, self.game.board[i][j]):
                return False
            if j < self.game.width - 1:
                if self.solve_recursive_helper(i, j + 1, cells_left - 1):
                    return True
            else:
                if self.solve_recursive_helper(i + 1, 0, cells_left - 1):
                    return True

        elif cells_left > 0:
            for num in range(1, 10):
                if not self.game.can_be_placed(i, j, num):
                    continue
                self.game.board[i][j] = num
                if j < self.game.width - 1:
                    if self.solve_recursive_helper(i, j + 1, cells_left - 1):
                        return True
                else:
                    if self.solve_recursive_helper(i + 1, 0, cells_left - 1):
                        return True
                self.game.board[i][j] = 0
        return False

    def solve(self):
        for row in range(self.game.height):
            for col in range(self.game.width):
                self.solution[row][col] = 0

        res = self.solve_recursive_helper(0, 0, self.game.width * self.game.height)
        if res:
            for row in range(self.game.height):
                for col in range(self.game.width):
                    self.game.board[row][col] = self.solution[row][col]
        return res
