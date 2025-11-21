def simple_calculator():
    """Simple calculator function"""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                return "Error: Cannot divide by zero!"
            result = a / b
        else:
            return "Error: Invalid operation!"
            
        return f"{a} {op} {b} = {result}"
        
    except ValueError:
        return "Error: Please enter valid numbers!"

# Usage
print(simple_calculator())