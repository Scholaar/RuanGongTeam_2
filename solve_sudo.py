class Sudoku:
    def is_place(self, board, row, col, num):
        # Check if it's possible to place 'num' at the given position
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        base_row, base_col = row // 3 * 3, col // 3 * 3
        for i in range(base_row, base_row + 3):
            for j in range(base_col, base_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtrace(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_place(board, row, col, num):
                            board[row][col] = num
                            if self.backtrace(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def solve_sudoku(self, problems):
        results = []
        for problem in problems:
            board = [row[:] for row in problem]  # Deep copy of the problem
            if self.backtrace(board):
                results.append(board)
        return results


if __name__ == "__main__":
    problems = [[
        [0, 0, 2, 0, 1, 0, 9, 0, 4],
        [0, 0, 0, 5, 0, 0, 6, 0, 8],
        [6, 1, 0, 9, 7, 0, 0, 3, 0],
        [7, 4, 6, 3, 2, 9, 1, 8, 5],
        [3, 2, 0, 1, 0, 0, 7, 0, 0],
        [1, 0, 5, 0, 0, 6, 3, 0, 0],
        [0, 9, 7, 8, 5, 0, 4, 6, 0],
        [0, 6, 1, 2, 0, 7, 8, 0, 3],
        [8, 5, 0, 4, 6, 1, 2, 9, 7]
    ]]

    # Solve the Sudoku problems
    solver = Sudoku()
    solutions = solver.solve_sudoku(problems)

    # Print the solutions
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(" ".join(map(str, row)))
