def print_pattern (x) :
    if(x<1) :
        return False;
    else :
        z=int(x);
        if(z-x) :
            return False;
          
line = input("Enter Number Of lines: ")
line = int(line);
k = print_pattern(line);
base_width=line;
line_to_print_number = line+1;
total_number_of_spaces = 3*line;
number_of_stars = 0;
#to print the upper part without base
for i in range (0,line*2) :
    print()