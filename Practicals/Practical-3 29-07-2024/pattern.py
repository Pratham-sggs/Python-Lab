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
total_number_of_spaces = 2*(line+2);
number_of_spaces = 0;
star = 0;
number = " ";
#to print the upper part without base
for i in range (1,line+2) :
    print(" "*(total_number_of_spaces - i*2) + "*" + " " * (number_of_spaces) + str(number) + " " * (number_of_spaces) +"*" * (star));
    if(i==1) :
        star = star+1;
        number_of_spaces = 1;
    if(i>1) :
        number_of_spaces = number_of_spaces +2;
    if(i==(line)) :
        number = line;
# to PRINT LOWER PYRAMID
if(line>1) :
    number = " ";
    total_number_of_spaces=2;
    num=line-1;
    number_of_spaces=3+(num*4);
    for i in range (1,line) :
        print(" "*(total_number_of_spaces + i*2) + "*" + " " * (number_of_spaces-4) + "*");
        number_of_spaces=number_of_spaces-4
#print base
for i in range (0,line) :
    total_number_of_spaces=5;
    print("* "*(total_number_of_spaces+(2*(line-1))));
