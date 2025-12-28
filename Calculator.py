def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    print("--- Python CLI Calculator ---")
    print("Operations: 1.Add | 2.Subtract | 3.Multiply | 4.Divide | Q.Quit")
    
    while True:
        try:
            choice = input("\nChoose an operation: ").lower()
            if choice == 'q':
                print("Exiting...")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please select 1-4 or Q.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1': print(f"Result: {add(num1, num2)}")
            elif choice == '2': print(f"Result: {subtract(num1, num2)}")
            elif choice == '3': print(f"Result: {multiply(num1, num2)}")
            elif choice == '4': print(f"Result: {divide(num1, num2)}")

        except ValueError as e:
            print(f"Input Error: {e}. Please enter numeric values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()