# Valid Parentheses Checker

# Function to check valid parentheses
def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping.values():  # opening brackets
            stack.append(char)
        elif char in mapping.keys():  # closing brackets
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
    return not stack  # True if stack is empty

# Main program
def main():
    user_input = input("Enter a string with parentheses: ")
    if is_valid_parentheses(user_input):
        print("Parentheses are valid.\n")
    else:
        print("Parentheses are not valid.\n")

main()