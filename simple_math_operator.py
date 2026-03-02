# USING CONDITIONAL STATEMENT

num1 = float(input("enter first number:  "))
num2 = float(input("enter second number:  "))

choice = input("enter your choice +, -, *, /, //, %, ** =  ")

if (choice == "+"):
    print (f"Addition: {num1+num2}")

elif(choice == "-"):
    print(f"Subtraction:{num1-num2}")
    
elif(choice == "*"):
    print(f"Multiplication:{num1*num2}")
    
elif(choice == "/"):
    print(f"Division:{num1/num2}")
    
elif(choice == "//"):
    print(f"Floor Division:{num1//num2}") # remove decimal
    
elif(choice == "%"):
    print(f"Module:{num1 % num2}") # give reminder 
    
elif(choice == "**"):
    print(f"Exponent:{num1 ** num2}") # power 
    
else:
    print("invalid choice") 

