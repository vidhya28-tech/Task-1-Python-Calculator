# Python CLI Calculator

## Calculator Application

A simple command-line calculator developed using Python. The application allows users to perform basic arithmetic operations through an interactive menu and continues running until the user chooses to exit.

## Objective

To develop a menu-driven command-line calculator that performs basic arithmetic operations while demonstrating Python functions, loops, conditional statements, user input, and exception handling.

## Tools Used

* Python
* VS Code
* Terminal

## Features

* Addition of two numbers
* Subtraction of two numbers
* Multiplication of two numbers
* Division of two numbers
* Continuous menu-driven interaction
* Input validation
* Division-by-zero handling
* Invalid input handling
* Multiple calculations without restarting
* Exit option

## Operations

| Choice | Operation      | Example               |
| ------ | -------------- | --------------------- |
| 1      | Addition       | 25 + 15 = 40          |
| 2      | Subtraction    | 25 - 15 = 10          |
| 3      | Multiplication | 25 × 15 = 375         |
| 4      | Division       | 25 ÷ 5 = 5            |
| 5      | Exit           | Closes the calculator |

## Key Concepts

* Functions for individual arithmetic operations
* Loops for continuous interaction
* Conditional statements for menu selection
* User input using `input()`
* Exception handling for invalid input
* Input validation
* Error handling for division by zero

## Project Structure

```text
Task-1-Python-Calculator/
|
|-- calculator.py
|-- README.md
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python calculator.py
```

4. Select an operation from the menu.
5. Enter the required numbers.
6. View the result.
7. Continue performing calculations or select option 5 to exit.

## Sample Interaction

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

## Error Handling

The application handles common input errors such as:

* Invalid menu choices
* Non-numeric input
* Division by zero
