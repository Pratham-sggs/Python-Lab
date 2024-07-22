pattern_lines = int(input("Number of lines in Pattern: "))
for i in range(pattern_lines):
    spaces = ' ' * (pattern_lines - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
