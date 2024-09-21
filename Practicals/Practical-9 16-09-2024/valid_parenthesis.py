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

print(check_validity("{<{>"))