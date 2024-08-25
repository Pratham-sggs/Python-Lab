import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        list_chr = [48,49,50,51,52,53,54,55,56,57]
        number1 = 0
        num1 = reversed(num1)
        num1 = "".join(num1)
        num2 = reversed(num2)
        num2 = "".join(num2)
        number2 = 0
        k = 1
        count = 0
        for i in num1 :
            ord_num = ord(i)
            num = list_chr.index(ord_num)
            if count > 0 :
                num = num*k
            number1 += num
            k = k*10
            count += 1
        count = 0
        k = 1
        for i in num2 :
            ord_num = ord(i)
            num = list_chr.index(ord_num)
            if count > 0 :
                num = num*k
            number2 += num
            k = k*10
            count += 1
        return str(number1+number2)