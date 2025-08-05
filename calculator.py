def calculate(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b if b != 0 else "Cannot divide by zero"
    else: return "Invalid operation"

def save_to_history(expression, result):
    with open("history.txt", "a") as f:
        f.write(f"{expression} = {result}\n")

while True:
    print("\n--- CALCULATOR ---")
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))
        result = calculate(a, b, op)
        print("Result:", result)
        save_to_history(f"{a} {op} {b}", result)
    except ValueError:
        print("Invalid input.")

    cont = input("Do you want to calculate again? (y/n): ")
    if cont.lower() != 'y':
        break
