valid_symbol = {'(', '{', '[', '<', '>', ']', '}', ')'}
valid_dictonary = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'
}
def check_validity(text):
    stack = []
    for symbol in text:
        if symbol in valid_symbol:
            if symbol in valid_dictonary:
                    stack.append(symbol)
            else:
                if stack:
                    if valid_dictonary[stack[-1]] == symbol:
                        stack.pop()
                    else:
                        return f"Invalid: Mismatched brakcet '{stack[-1]}' and '{symbol}'"
                else:
                    return f"Invalid: Unmatched closing bracket '{symbol}'"
        else:
            return "Invalid: Non-bracket character '{symbol}'"
    if stack:
        return f"Invalid: Unmatched opening bracket '{stack[-1]}'"
    return "Valid"

def get_valid_invalid_text_count (list_of_text) :
    valid_text = 0
    invalid_text = 0
    for text in list_of_text :
        if type(text) in [str] :
            result = check_validity(text)
            if result == "Valid" :
                valid_text += 1
            else :
                invalid_text += 1
        elif type(text) in [list ,dict ,tuple] :
            result = get_valid_invalid_text_count(text)
            valid_text += result[0]
            invalid_text += result[1]
    return valid_text,invalid_text

print(get_valid_invalid_text_count(['[{(', [45 , ("()"),]]))