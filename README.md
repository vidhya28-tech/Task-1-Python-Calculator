# 🐍 Python Internship – Task 1

## CLI Calculator

This project is part of the **Python Internship – Task 1**, focused on developing a simple command-line calculator using Python. The application allows users to perform basic arithmetic operations through an interactive menu and continues running until the user chooses to exit.

### 🎯 Objective

To build a menu-driven command-line calculator that performs basic arithmetic operations while demonstrating the use of Python functions, loops, conditionals, user input, and exception handling.

### 🛠️ Tools Used

* Python
* VS Code
* Terminal

### 🧮 Features

* Addition of two numbers
* Subtraction of two numbers
* Multiplication of two numbers
* Division of two numbers
* Handles division by zero
* Validates invalid menu choices
* Handles non-numeric user input
* Allows multiple calculations without restarting the program
* Provides an option to exit the calculator

### ⚙️ Operations

| Choice | Operation      | Example               |
| ------ | -------------- | --------------------- |
| 1      | Addition       | 25 + 15 = 40          |
| 2      | Subtraction    | 25 - 15 = 10          |
| 3      | Multiplication | 25 × 15 = 375         |
| 4      | Division       | 25 ÷ 5 = 5            |
| 5      | Exit           | Closes the calculator |

### 📚 Key Concepts

* **Functions** — separate functions are used for each arithmetic operation.
* **Loops** — the calculator continues running until the user selects the exit option.
* **Conditionals** — menu choices determine which operation is performed.
* **User Input** — numbers and operation choices are taken through `input()`.
* **Exception Handling** — invalid numeric input is handled using `try-except`.
* **Input Validation** — invalid menu selections are detected and handled.
* **Error Handling** — division by zero is prevented.

### 📁 Project Structure

```text
Task-1-Python-Calculator/
│
├── calculator.py
└── README.md
```

### ▶️ How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python calculator.py
```

4. Select an operation from the displayed menu.
5. Enter the required numbers.
6. View the calculation result.
7. Continue performing calculations or select **5** to exit.

### 💻 Sample Interaction

```text
===== Python CLI Calculator =====
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
================================
Enter your choice (1-5): 1

Enter the first number: 25
Enter the second number: 15

Result: 25.0 + 15.0 = 40.0
```

### 🔍 Error Handling

The application handles common input errors such as:

* Entering an invalid menu option
* Entering text instead of a number
* Attempting to divide by zero

This prevents the program from terminating unexpectedly during normal user interaction.
