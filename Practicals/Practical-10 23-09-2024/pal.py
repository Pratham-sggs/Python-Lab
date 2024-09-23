def is_palindrome(text):
    return text == text[::-1]

def fun(L):
    count = 0
    valid_obj_count = [int, str]
    valid_obj = [list, tuple, set]
    for i in L:
        t = type(i)
        if t in valid_obj_count:
            if t == int:
                i = str(i)
            if len(i) % 5 == 3:
                count += is_palindrome(i)
        elif t in valid_obj:
                count += fun(i)
    
    return count
print(fun([12345, "level", 1221, [54321, 131], {"racecar", 131 , 98789}]))