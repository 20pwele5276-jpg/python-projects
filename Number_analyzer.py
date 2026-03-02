# Number Analyzer

# Function to find maximum
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Function to find minimum
def findMin(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

# Function to find average
def find_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

# Function to count even numbers
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

# Main program
def main():
    user_input = input("Enter numbers separated by space: ")
    numbers = [int(x) for x in user_input.split()]
    
    print(f"Maximum number: {find_max(numbers)}")
    print(f"Minimum number: {findMin(numbers)}")
    print(f"Average: {find_average(numbers)}")
    print(f"Count of even numbers: {count_even(numbers)}")

main()