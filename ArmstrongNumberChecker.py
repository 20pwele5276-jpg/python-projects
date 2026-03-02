def checkArmstrong():
    num = int(input("enter a number: "))
    total = 0
    temp = num
    while (temp > 0):
        digit = temp % 10 # get last digit
        total += digit ** 3  # cube it and add to total
        temp //= 10       # remove last digit
        
    if total == num :
        print(f"{num} is an armstrong number. ")
    else:
        print(f"{num} is not an armstrong number. ")
        
checkArmstrong()