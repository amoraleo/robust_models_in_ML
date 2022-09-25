import re

def check_regex(string): #using regular expressions(1st solution)
    string  = re.sub("[^{}()\[\]]", "", string)
    while "{}" in string or "()" in string or "[]" in string:
        string = string.replace("[]", "")
        string = string.replace("{}", "")
        string = string.replace("()", "")
    if string == "":
        return True
    else:
        return False

def check(string): #without using regular expressions(2nd solution)
    brackets_list = []
    for char in string:
        match char:
            case "(":
                brackets_list.append(char)
            case "{":
                brackets_list.append(char)
            case "[":
                brackets_list.append(char)
            case ")":
                if brackets_list:
                    if brackets_list.pop() != "(":
                        return False
                else:
                    return False
            case "}":
                if brackets_list:
                    if brackets_list.pop() != "{":
                        return False
                else:
                    return False
            case "]":
                if brackets_list:
                    if brackets_list.pop() != "[":
                        return False
                else:
                    return False
    if not brackets_list:
        return True
    else:
        return False


string = input()

print(check_regex(string))
print(check(string))