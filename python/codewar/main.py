def valid_parentheses(string):
    valid = True
    
    if (string == ''): 
        return True
    new_str = ""
    for str in string:
        if (str == '(' or str == ')'):
            new_str = new_str + str

    if (new_str[0] != '('):
        valid = False
    if (new_str[-1] != ')'):
        valid = False

    n = 0
    for str in new_str:
        if (str == '('):
            n = n + 1
        else:
            n = n - 1
            if (n < 0):
                return False
    if (n != 0):
        valid = False
    return valid