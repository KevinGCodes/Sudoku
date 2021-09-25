import math


class sudoku_solver:

    def __init__(self, game):
        self.game = game
        self.solution = [[0 for i in range(0, game.width)] for j in range(0, game.height)]

    def solve_recursive_helper(self, i, j, cells_left):
        if cells_left == 0 or i >= self.game.height or j >= self.game.width:
            if self.game.is_solved():
                self.game.visualize()
                self.solution = [[self.game.board[k][l] for k in range(0, self.game.width)] for l in
                                 range(0, self.game.height)]
                return True

        elif self.game.preset[i][j]:
            if j < self.game.width - 1:
                if self.solve_recursive_helper(i, j + 1, cells_left - 1):
                    return True
            else:
                if self.solve_recursive_helper(i + 1, 0, cells_left - 1):
                    return True
        else:
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
        res = self.solve_recursive_helper(0, 0, self.game.width * self.game.height)
        if res:
            self.game.board = self.solution
        return res
