def print_pattern (line) :
    list=[]
    if(line<1) :
        list.append("Invalid Number");
        return list;
    else :
        z=int(line);
        if(z-line) :
            list.append("Invalid Number");
            return list;
        line=int(line)
        total_number_of_spaces = 2*(line+2);
        number_of_spaces = 0;
        star = 0;
        number = " ";
        inc = 0;
        #to print the upper part without base
        for i in range (1,line+2) :
            list.append(" "*(total_number_of_spaces - i*2) + "*" + " " * (number_of_spaces) + str(number) + " " * (number_of_spaces-inc) +"*" * (star));
            if(i==1) :
                star = star+1;
                number_of_spaces = 1;
            if(i>1) :
                number_of_spaces = number_of_spaces +2;
            if(i==(line)) :
                number = line;
                inc = len(str(line))-1
        # to PRINT LOWER PYRAMID
        if(line>1) :
            number = " ";
            total_number_of_spaces=2;
            num=line-1;
            number_of_spaces=3+(num*4);
            for i in range (1,line) :
                list.append(" "*(total_number_of_spaces + i*2) + "*" + " " * (number_of_spaces-4) + "*");
                number_of_spaces=number_of_spaces-4
        #print base
        for i in range (0,line) :
            total_number_of_spaces=5;
            list.append("* "*(total_number_of_spaces+(2*(line-1))));
    return list;
          
k = print_pattern(45.0000);
for i in range(0,len(k)) :
    print(k[i])
