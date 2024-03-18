import random

def generate_sudoku():
    grid = [[0 for _ in range(9)] for _ in range(9)]

    if fill_grid(grid):
        return grid
    else:
        return None

def fill_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                valid_numbers = [n for n in range(1, 10) if is_valid(grid, i, j, n)]
                if valid_numbers:
                    random.shuffle(valid_numbers)  # Shuffle for variety
                    for num in valid_numbers:
                        grid[i][j] = num
                        if fill_grid(grid):  # Backtrack if needed
                            return True
                        else:
                            grid[i][j] = 0  # Reset cell if backtracking fails
                return False  # Propagate failure back up
    return True  # Grid is filled


def is_valid(grid, row, col, n):
    # Check if the number already exists in the row
    if n in grid[row]:
        return False

    # Check if the number already exists in the column
    for i in range(9):
        if n == grid[i][col]:
            return False

    # Check if the number already exists in the 3x3 box
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if grid[i][j] == n:
                return False

    return True


def print_sudoku(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' ')
        print()


# Generate a Sudoku puzzle
grid = generate_sudoku()
if grid:
    print_sudoku(grid)
else:
    print("Unable to generate a Sudoku puzzle.")