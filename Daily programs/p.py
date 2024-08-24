def isPalindrome(s: str) -> bool:
        string_after = ""
        for i in s :
            if ord(i) <= 122 and ord(i) >= 97 or ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 48 and ord(i) <= 57 :
                string_after = string_after + i.lower()
        temp = reversed(string_after)
        if "".join(temp) == string_after :
            return True
        else :
            return False

print(isPalindrome(",,,,,,,,,,,.....,acva"))