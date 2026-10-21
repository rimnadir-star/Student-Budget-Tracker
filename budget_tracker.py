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