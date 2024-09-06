valid_num = {1,0}
def binary_subtraction (a,b) :
    a = a.lower()
    b = b.lower()

    value = 1

    if a.startswith("-0b") :
        a = "-" + a[3:]
    elif a.startswith("0b") :
        a = a[2:]
    
    if b.startswith("-0b") :
        b = "-" + a[3:]
    elif b.startswith("0b") :
        b = a[2:]
    
    if "-" in a and "-" in b :
        value = 4 
        a = a[1:]
        b = b[1:]
    elif "-" in a :
        value = 3
        a = a[1:]
        return "-" + binary_addition(a,b)
    elif "-" in b :
        value = 2
        b = b[1:]
        return binary_addition(a,b)

    for i in a :
        if not(i in valid_num) :
            return "Invalid Binary Numbers"
    for i in b :
        if not(i in valid_num) :
            return "Invalid Binary Numbers"
    
    return 0

def binary_addition (num1,num2) :
    num1 = "".join(reversed(num1))
    num2 = "".join(reversed(num2))
    length_num1 = len(num1)
    length_num2 = len(num2)
    carry = 0
    result = ""
    if length_num1 > length_num2 :
        num2 = num2.ljust(length_num1,"0")
    elif length_num2 > length_num1 :
        num1 = num1.ljust(length_num2,"0")
    for i in range(0,length_num1) :
            a = 0 if num1[i] == "0" else 1
            b = 0 if num2[i] == "0" else 1
            c = a + b + carry
            if c == 0 or c == 1 :
                result =str(c) + result
                carry = 0
            elif c == 2 :
                result = "0" + result
                carry = 1
            elif c == 3 :
                result = "1" + result
                carry = 1
    if carry == 1 :
        result = "1" + result
    return result

        

print(binary_subtraction("-1011","1011"))

    
