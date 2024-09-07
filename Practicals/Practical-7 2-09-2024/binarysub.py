valid_num = {'1', '0'}

def binary_subtraction(a, b):
    a = a.lower()
    b = b.lower()
    if a.startswith("-0b"):
        a = "-" + a[3:]
    elif a.startswith("0b"):
        a = a[2:]

    if b.startswith("-0b"):
        b = "-" + b[3:]
    elif b.startswith("0b"):
        b = b[2:]

    if "-" in a and "-" in b:
        a = a[1:]
        b = b[1:]
        a, b = b, a
        if is_valid_binary(a, b):
            return subtraction(a, b)
        else:
            return "Invalid Binary"
    elif "-" in a:
        a = a[1:]
        if is_valid_binary(a, b):
            return "-" + binary_addition(a, b)
        else:
            return "Invalid Binary"
    elif "-" in b:
        b = b[1:]
        if is_valid_binary(a, b):
            return binary_addition(a, b)
        else:
            return "Invalid Binary"
    else:
        if is_valid_binary(a, b):
            return subtraction(a, b)
        else:
            return "Invalid Binary"

def binary_addition(num1, num2):
    num1 = "".join(reversed(num1))
    num2 = "".join(reversed(num2))
    length_num1 = len(num1)
    length_num2 = len(num2)
    carry = 0
    result = ""
    if length_num1 > length_num2:
        num2 = num2.ljust(length_num1, "0")
    elif length_num2 > length_num1:
        num1 = num1.ljust(length_num2, "0")
    
    for i in range(len(num1)):
        a = 0 if num1[i] == "0" else 1
        b = 0 if num2[i] == "0" else 1
        c = a + b + carry
        if c == 0 or c == 1:
            result = str(c) + result
            carry = 0
        elif c == 2:
            result = "0" + result
            carry = 1
        elif c == 3:
            result = "1" + result
            carry = 1
    if carry == 1:
        result = "1" + result
    return result

def subtraction(num1, num2):
    length_num1 = len(num1)
    length_num2 = len(num2)
    result = ""
    if length_num1 > length_num2:
        num2 = num2.rjust(length_num1, "0")
    elif length_num2 > length_num1:
        num1 = num1.rjust(length_num2, "0")
    num2_compliment = ones_compliment(num2)
    addition_of_compliment = binary_addition(num1, num2_compliment)
    
    if len(addition_of_compliment) == len(num1):
        return "-" + ones_compliment(addition_of_compliment)
    else:
        result = addition_of_compliment[1:]
        result = binary_addition(result, "1")
        return result

def is_valid_binary(a, b):
    for i in a:
        if not(i in valid_num):
            return False
    for i in b:
        if not(i in valid_num):
            return False
    return True

def ones_compliment(number):
    r = ""
    for i in number:
        if i == "0":
            r = r + "1"
        else:
            r = r + "0"
    return r

print(binary_subtraction("01", "11"))