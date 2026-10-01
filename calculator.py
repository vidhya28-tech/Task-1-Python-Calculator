def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def display_menu():
    print("\n===== Python CLI Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("================================")


def calculator():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("\nThank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select a number from 1 to 5.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        else:
            result = divide(num1, num2)
            operator = "/"

        print(f"\nResult: {num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    calculator()