def print_pattern(level):
    base_width = 15  # Width of the rectangle of stars

    # Top part of the pyramid
    for j in range(level):
        print(' ' * (level - j) + '*' * (2 * j + 1))

    # Number inside the pyramid
    print(' ' * (level - 1) + '*' + ' ' * (level - 1) + str(level) + ' ' * (level - 1) + '*')

    # Bottom part of the pyramid
    print('*' * base_width)

    # Rectangle of stars
    for k in range(level):
        print('*' * base_width)

# Ask the user for the number of levels
num_level = int(input("Enter the number of the pyramid level (1, 2, 3, etc.): "))

# Print the pattern corresponding to the entered level
print_pattern(num_level)
