sudoku=[[5,1,7,6,0,0,0,3,4],
        [2,8,9,0,0,4,0,0,0],
        [3,4,6,2,0,5,0,9,0],
        [6,0,2,0,0,0,0,1,0],
        [0,3,8,0,0,6,0,4,7],
        [0,0,0,0,0,0,0,0,0],
        [0,9,0,0,0,0,0,7,8],
        [7,0,3,4,0,0,5,6,0],
        [0,0,0,0,0,0,0,0,0]] 

def sudokuSolver(grid):
    """
    :type sudoku: given as above, should work on any variation
    :rtype: True or False
    """
    backtrack_sudoku(grid)

#check row, column and 3 x 3 grid
def check_rc (row, col, grid, n):
    for i in range(9):
        if grid[row][i] != 0 and grid[row][i] == n:
            return False
        if grid[i][col] != 0 and grid[i][col] == n:
            return False
        if grid[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] != 0 and grid[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == n:
            return False
    return True

#sudoku backtracking solution
def backtrack_sudoku(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if check_rc(i, j, grid, n):
                        grid[i][j] = n
                        if backtrack_sudoku(grid):
                            return True
                        else:
                            grid[i][j] = 0
                return False
    return True
