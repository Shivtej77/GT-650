# Function to add two numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# Input numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the function and display the result
result = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is", result);
