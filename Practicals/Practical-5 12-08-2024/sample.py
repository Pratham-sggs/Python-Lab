def change_case(string, style):
    if style == "c" or style == "C":
        result_list = []
        result = ""
        for i in range(len(string)):
            if string[i].isdigit():
                result_list.append(string[i])
            else:
                for k in range(97, 123):
                    l = chr(k)
                    if l == string[i]:
                        result_list.append(chr(k - 32))
                        break
                    else:
                        if chr(k - 32) == string[i]:
                            result_list.append(string[i])
        for i in range(len(result_list)):
            result = result + result_list[i]
        return result

    elif style == "s" or style == "S":
        result_list = []
        result = ""
        for i in range(len(string)):
            if string[i].isdigit():
                result_list.append(string[i])
            else:
                for k in range(65, 91):
                    l = chr(k)
                    if l == string[i]:
                        result_list.append(chr(k + 32))
                        break
                    else:
                        if chr(k + 32) == string[i]:
                            result_list.append(string[i])
        for i in range(len(result_list)):
            result = result + result_list[i]
        return result

    elif style == "r" or style == "R":
        result_list = []
        result = ""
        for i in range(len(string)):
            if string[i].isdigit():
                result_list.append(string[i])
            else:
                for k in range(65, 91):
                    if chr(k) == string[i]:
                        result_list.append(chr(k + 32))
                    if chr(k + 32) == string[i]:
                        result_list.append(chr(k))
        for i in range(len(result_list)):
            result = result + result_list[i]
        return result
    
    elif style == "U" or style == "u":
        result_list = []
        result = ""
        first_letter_capital = 'A' <= string[0] <= 'Z'
        
        for i in range(len(string)):
            if string[i].isdigit():
                result_list.append(string[i])
            else:
                if (i % 2 == 0 and first_letter_capital) or (i % 2 != 0 and not first_letter_capital):
                    
                    if 'A' <= string[i] <= 'Z':
                        result_list.append(chr(ord(string[i]) + 32))
                    else:
                        result_list.append(string[i])
                else:
                    if 'a' <= string[i] <= 'z':
                        result_list.append(chr(ord(string[i]) - 32))
                    else: 
                        result_list.append(string[i])
        
        result = ''.join(result_list)
        return result
            


print(change_case("SGg2S", "R"))
