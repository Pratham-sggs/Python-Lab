import random
import math

# Check if a number is valid in a specific position
def is_valid_move(grid, row, col, num, size):
    # Check row and column
    for i in range(size):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check sub-box
    box_size = int(math.sqrt(size))  # Box size (e.g., 3 for 9x9)
    box_row_start = row - row % box_size
    box_col_start = col - col % box_size

    for i in range(box_size):
        for j in range(box_size):
            if box_row_start + i < size and box_col_start + j < size:
                if grid[box_row_start + i][box_col_start + j] == num:
                    return False

    return True

# Recursive function to fill the grid
def fill_grid(grid, size):
    def fill_recursive():
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 0:
                    nums = list(range(1, size + 1))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid_move(grid, i, j, num, size):
                            grid[i][j] = num
                            if fill_recursive():
                                return True
                            grid[i][j] = 0
                    return False
        return True

    fill_recursive()

# Generate a valid Sudoku grid
def generate_sudoku(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    fill_grid(grid, size)
    return grid

# Remove elements based on difficulty
def remove_elements(grid, size, difficulty):
    total_elements = size * size
    if difficulty == 'easy':
        num_to_remove = int(0.4 * total_elements)
    elif difficulty == 'medium':
        num_to_remove = int(0.6 * total_elements)
    elif difficulty == 'hard':
        num_to_remove = int(0.7 * total_elements)
    else:
        raise ValueError("Invalid difficulty level")

    removed_positions = set()
    while len(removed_positions) < num_to_remove:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if (row, col) not in removed_positions:
            grid[row][col] = 0  # 0 represents an empty cell
            removed_positions.add((row, col))

# Print the Sudoku grid
def print_sudoku(grid, size):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Main game logic
def sudoku_game():
    size = int(input("Enter the size of the Sudoku grid (maximum 11): "))
    if size < 2 or size > 11:
        print("Invalid size. Please enter a number between 2 and 11.")
        return

    difficulty = input("Enter difficulty level (easy, medium, hard): ").lower()
    
    # Generate a valid Sudoku grid
    grid = generate_sudoku(size)
    
    # Remove elements based on difficulty
    remove_elements(grid, size, difficulty)
    
    # Print the initial Sudoku grid
    print("Sudoku Puzzle:")
    print_sudoku(grid, size)

# Run the game
sudoku_game()
