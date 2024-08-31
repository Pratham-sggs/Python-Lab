short_form = {"0B","0X","0O"}
number_system = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def base(text,input_base,output_base) :
    int_num = inte(text,input_base)
    if not(isinstance(int_num, int)) :
            return int_num
    if output_base == "r" or output_base == "R" :
        result = int_to_rom(int_num)
        return result 
    else :
        if output_base > 36 or output_base < 2   :
            return "Error! Base should not be greater than 36 or smaller than 2"
        
        valid_char = number_system[0:output_base]
        quotient = int_num
        remainder = 0
        result = ""
        while quotient != 0 :
            remainder = quotient % output_base
            result = valid_char[remainder] + result
            quotient  = quotient // output_base
        return result
def inte (num,base = 10) :
    if base == "R" or base == "r" :
        return rom_to_int(num)
    if base > 36 or base < 2:
        return "Error! Base should not be greater than 36 or smaller than 2"
    num = str(num)
    num = num.upper()
    small_str = num[0:2]
    if "0B" == small_str and base != 2 :
            if base < 12 :
                return "0B should be used when base is 2 or base < 11"
    elif "0X" == small_str and base != 16 :
            if base < 34 :
                return "0X should be used when base is 16 or base > 33 "
    elif "0O" == small_str and base != 8  :
            if base < 25 :
                return "0O should be used when base is 8 or base > 24 "
    
    if (num.startswith("0B") and base == 2) or (num.startswith("0X") and base == 16) or num.startswith("0O") and base == 8 :
        num = num[2:]

    valid_char = number_system[0:base]
    for i in num :
        if not (i in valid_char) :
            return "Enter Valid Number or Base"
    number_in_decimal = 0
    length = len(num) - 1
    for i in num :
        number_in_decimal = number_in_decimal + valid_char.index(i) * (base ** length)
        length -= 1
    return number_in_decimal

def int_to_rom (num) :
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
def rom_to_int (s) :
        list_of_rom = list(s)
        number = 0
        
        while list_of_rom:
            letter = list_of_rom.pop()
            
            if letter == "I":
                number += 1
                
            elif letter == "V":
                if list_of_rom and list_of_rom[-1] == "I":
                    number += 4
                    list_of_rom.pop()
                else:
                    number += 5
                
            elif letter == "X":
                if list_of_rom and list_of_rom[-1] == "I":
                    number += 9
                    list_of_rom.pop()
                else:
                    number += 10
                
            elif letter == "L":
                if list_of_rom and list_of_rom[-1] == "X":
                    number += 40
                    list_of_rom.pop()
                else:
                    number += 50
                
            elif letter == "C":
                if list_of_rom and list_of_rom[-1] == "X":
                    number += 90
                    list_of_rom.pop()
                else:
                    number += 100
                
            elif letter == "D":
                if list_of_rom and list_of_rom[-1] == "C":
                    number += 400
                    list_of_rom.pop()
                else:
                    number += 500
                
            elif letter == "M":
                if list_of_rom and list_of_rom[-1] == "C":
                    number += 900
                    list_of_rom.pop()
                else:
                    number += 1000
        
        return number

print(base("XX","R",2))