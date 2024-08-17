def count(String, sub_str, truth_value, start=0):
    length = len(sub_str)
    if start > len(String) - length:
        return 0
    
    if String[start:start + length] == sub_str:
        if truth_value:
            return 1 + count(String, sub_str, truth_value, start + 1)
        else:
            return 1 + count(String, sub_str, truth_value, start + length)
    else:
        return count(String, sub_str, truth_value, start + 1)

print(count("sgsgsgsg", "sgs", True))
