# Personal Mini-Toolkit

def calculator():
    # Tool 1: Calculate two numbers.
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("You cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"The answer is {result}.")
    except ValueError:
        print("Please enter valid numbers.")


def todo_list():
    # Tool 2: Add and view tasks in a list.
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Return to main menu")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            if tasks:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your list is empty.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def even_odd_checker():
    # Tool 3: Check whether a number is even or odd.
    try:
        number = int(input("Enter a whole number: "))
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Please enter a valid whole number.")


def main():
    # Repeat the menu until the user chooses Quit.
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Even or Odd Checker")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            even_odd_checker()
        elif choice == "4":
            print("Thank you for using My Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not valid. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
