def print_pattern(x) :
    zero_spaces = 1;
    three_spaces= 2;
    six_spaces = 3;
    for i in range (1,x+1) :
        if i == zero_spaces :
            print("*");
            zero_spaces = 4 + zero_spaces
        if i == three_spaces :
            print("   *");
            three_spaces = three_spaces + 2;
        if i == six_spaces :
            print("      *");
            six_spaces = six_spaces + 4;
k=int(input("number: "))
print_pattern(k);