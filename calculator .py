#!/usr/bin/env python3
"""
Simple Calculator with History
Basic calculator with +, -, *, /, % operations and calculation history.
"""

# Store calculation history
calculation_history = []

def add_to_history(expression, result):
    """Add calculation to history list."""
    calculation_history.append(f"{expression} = {result}")

def show_history():
    """Display all previous calculations."""
    if not calculation_history:
        print("No calculations in history.")
        return
    
    print("\n--- Calculation History ---")
    for i, calc in enumerate(calculation_history, 1):
        print(f"{i}. {calc}")
    print(f"Total calculations: {len(calculation_history)}\n")

def clear_history():
    """Clear all calculation history."""
    global calculation_history
    calculation_history = []
    print("History cleared!")

def calculate(num1, operator, num2):
    """Perform calculation and handle errors."""
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero!"
            result = num1 / num2
        elif operator == '%':
            if num2 == 0:
                return "Error: Division by zero!"
            result = num1 % num2
        else:
            return "Error: Invalid operator!"
        
        # Add to history
        expression = f"{num1} {operator} {num2}"
        add_to_history(expression, result)
        return result
    
    except Exception as e:
        return f"Error: {e}"

def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def main():
    """Main calculator program."""
    print("🧮 Simple Calculator with History")
    print("Supported operations: +, -, *, /, %")
    print("Commands: 'history', 'clear', 'quit'\n")
    
    while True:
        print("--- Calculator Menu ---")
        print("1. New Calculation")
        print("2. View History")
        print("3. Clear History")
        print("4. Quit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            # New calculation
            num1 = get_number("Enter first number: ")
            operator = input("Enter operator (+, -, *, /, %): ").strip()
            num2 = get_number("Enter second number: ")
            
            result = calculate(num1, operator, num2)
            print(f"Result: {num1} {operator} {num2} = {result}\n")
        
        elif choice == '2':
            # View history
            show_history()
        
        elif choice == '3':
            # Clear history
            confirm = input("Clear all history? (y/n): ").lower()
            if confirm == 'y':
                clear_history()
        
        elif choice == '4':
            # Quit
            print("Thanks for using the calculator!")
            break
        
        else:
            print("Invalid choice! Please enter 1-4.\n")

if __name__ == "__main__":
    main()