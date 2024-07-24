pattern_lines = int(input("Number of lines in Pattern (must be odd): "))

# Ensure the number of lines is odd
if pattern_lines % 2 == 0:
    print("Please enter an odd number.")
else:
    # Top half including the middle line
    for i in range((pattern_lines // 2) + 1):
        spaces = ' ' * (pattern_lines // 2 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

    # Bottom half
    for i in range((pattern_lines // 2) - 1, -1, -1):
        spaces = ' ' * (pattern_lines // 2 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
