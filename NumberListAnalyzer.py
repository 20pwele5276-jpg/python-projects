# Number List Analyzer
# Function to find second largest number
def second_largest(numbers):
    if len(numbers) < 2:
        return None  # not enough numbers
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

# Function to remove duplicates
def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Main program
def main():
    user_input = input("Enter numbers separated by space: ")
    numbers = [int(x) for x in user_input.split()]

    second = second_largest(numbers)
    if second is None:
        print("Not enough numbers to find second largest.")
    else:
        print(f"Second largest number: {second}")

    no_duplicates = remove_duplicates(numbers)
    print(f"List without duplicates: {no_duplicates}")

main()