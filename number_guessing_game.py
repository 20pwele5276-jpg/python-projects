import random
n = random.randint(1,50)

print("Guess the correct number between 1 to 150")

turn =0

while(True):
    guess = int(input("Enter your guess: "))
    turn+=1
    if(guess> n):
        print ( "Too high, try again")
    elif(guess< n):
        print("Too low! try again")
    else:
        print(f" congratulation! You guessed the correct number:  {n} in {turn} turns.")
        break


    