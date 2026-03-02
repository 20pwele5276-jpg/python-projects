# Palindrome Checker

# Function to check palindrome
def is_palindrome(value):
    value_str = str(value)             # convert to string
    reversed_str = value_str[::-1]     # reverse the string
    return value_str == reversed_str   # compare with original

# Main program
def main():
    user_input = input("Enter a number or string: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.\n")
    else:
        print(f"'{user_input}' is not a palindrome.\n")

main()