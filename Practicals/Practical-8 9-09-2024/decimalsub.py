valid_num = ["0","1","2","3","4","5","6","7","8","9"]

def decimal_subtraction (a,b) :
	num1 = str_to_int(a)
	num2 = str_to_int(b)
	

def str_to_int (text) :
	text = "".join(reversed(text))
	length = len(text)
	result = 0
	for i in range (0,length) :
		result += valid_num.index(text[i])  * (10**i)
	return result
print(str_to_int("9"))