# Basic Calculator Program

def calculator():
    try:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")
        num2 = float(input("Enter the second number: "))

        # Perform the operation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        elif operator == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operator."

        # Display the result
        return f"The result is: {result}"

    except ValueError:
        return "Error: Invalid input. Please enter numbers only."

# Run the calculator
print(calculator())
