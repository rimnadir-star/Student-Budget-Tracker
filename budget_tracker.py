def show_menu():
    """Display the main menu."""
    print("\n===== STUDENT BUDGET TRACKER =====")
    print("1. Set monthly budget")
    print("2. Add an expense")
    print("3. View expenses")
    print("4. View budget summary")
    print("5. Exit")


def set_budget():
    """Ask the user for their monthly budget."""
    while True:
        try:
            budget = float(input("Enter your monthly budget ($): "))
            if budget < 0:
                print("Budget cannot be negative.")
            else:
                return budget
        except ValueError:
            print("Please enter a valid number.")

def add_expense(expenses):
    """Record a new expense."""
    description = input("Expense description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    categories = [
        "Food",
        "Transportation",
        "Housing",
        "Education",
        "Entertainment",
        "Other"
    ]
    print("\nChoose a category:")

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    try:
        choice = int(input("Category number: "))

        if choice < 1 or choice > len(categories):
            print("Invalid category.")
            return

    except ValueError:
        print("Please enter a valid category number.")
        return

    try:
        amount = float(input("Expense amount ($): "))

        if amount <= 0:
            print("Expense must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "description": description,
        "category": categories[choice - 1],
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")
def view_expenses(expenses):
    """Display all recorded expenses."""

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n===== YOUR EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['description']} | "
            f"{expense['category']} | "
            f"${expense['amount']:.2f}"
        )


def view_summary(budget, expenses):
    """Display the budget, spending, and remaining balance."""

    total_spent = sum(expense["amount"] for expense in expenses)
    remaining = budget - total_spent

    print("\n===== BUDGET SUMMARY =====")
    print(f"Monthly budget: ${budget:.2f}")
    print(f"Total spent:    ${total_spent:.2f}")
    print(f"Money left:     ${remaining:.2f}")

    if remaining < 0:
        print(f"You are ${-remaining:.2f} over budget!")
    elif remaining == 0:
        print("You have used your entire budget.")
    else:
        print("You are still within your budget.")


def main():
    """Run the budget tracker."""

    budget = 0.0
    expenses = []

    print("Welcome to the Student Budget Tracker!")

    while True:
        show_menu()

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            budget = set_budget()
            print(f"Monthly budget set to ${budget:.2f}.")

        elif choice == "2":
            add_expense(expenses)

        elif choice == "3":
            view_expenses(expenses)

        elif choice == "4":
            view_summary(budget, expenses)

        elif choice == "5":
            print("Thanks for using the Student Budget Tracker!")
            break

        else:
            print("Invalid option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()

