def print_pattern(x):
    if x < 1:
        return False
    else:
        z = int(x)
        if z != x:
            return False
    return True

line = int(input("Enter Number Of Lines: "))

if not print_pattern(line):
    print("Invalid input. Please enter a positive integer.")
else:
    base_width = line
    line_to_print_number = line + 1
    total_number_of_spaces = 2 * (line + 2)
    number_of_spaces = 0
    star = 0
    number = " "

    # To print the upper part without the base
    for i in range(1, line + 2):
        if i == line_to_print_number :
            number = str(line)
        print(" " * (total_number_of_spaces - i * 2) + "*" + " " * number_of_spaces + str(number) + " " * number_of_spaces + "*" * star)
        if i == 1:
            star += 1
            number_of_spaces = 1
        elif i > 1:
            number_of_spaces += 2

    # To print lower pyramid
    if line > 1:
        number = " "
        total_number_of_spaces = 2
        number_of_spaces = 3 + (line - 1) * 4
        for i in range(1, line):
            print(" " * (total_number_of_spaces + i * 2) + "*" + " " * (number_of_spaces - 4) + "*")
            number_of_spaces -= 4

    # Print base
    for i in range(0, line):
        print("* " * (5 + (2 * (line - 1))))
