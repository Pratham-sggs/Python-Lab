valid_op_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def rom(string, base=10):
    string = string.upper()

    if base > 36 or base < 2:
        return "Error! Base should not be greater than 36 or smaller than 2"
    
    # Check first 2 characters
    small_str = string[0:2]

    if "0B" == small_str and base != 2 :
            if base < 12 :
                return "0B should be used when base is 2 or base < 11"
    elif "0X" == small_str and base != 16 :
            if base < 34 :
                return "0X should be used when base is 16 or base > 33 "
    elif "0O" == small_str and base != 8  :
            if base < 25 :
                return "0O should be used when base is 8 or base > 24 "
    
    # Strip prefixes if valid
    if string.startswith("0B") and base == 2:
        string = string[2:]
    elif string.startswith("0X") and base == 16:
        string = string[2:]
    elif string.startswith("0O") and base == 8:
        string = string[2:]

    if string_is_valid(string, base):
        num = int(string, base)
        result = ""
        roman_numerals = [
             (100000, 'C̅'), (90000, 'X̅C̅'),
            (50000, 'L̅'), (40000, 'X̅L̅'), (10000, 'X̅'), (9000, 'I̅X̅'), (5000, 'V̅'),
            (4000, 'I̅V̅'), (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
            (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        for value, symbol in roman_numerals:
            while num >= value:
                result += symbol
                num -= value

        return result
    else:
        return "Invalid Number"

def string_is_valid(string, base):
    valid_elements = valid_op_list[0:base]
    for i in string:
        if i not in valid_elements:
            return False
    return True

print(rom("90000"))
