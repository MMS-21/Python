import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expenses.json")

def load_expenses():
    """Load existing expenses from the JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(amount, category, description=""):
    """Add a new expense entry."""
    expenses = load_expenses()
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Added {amount} in '{category}' category.")

def view_summary():
    """View total spending and category breakdown."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(e["amount"] for e in expenses)
    print(f"\n💵 Total Expenses: ${total:.2f}\n")

    categories = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

    for cat, amt in categories.items():
        print(f"- {cat}: ${amt:.2f}")

def main():
    print("📘 Simple Expense Tracker")
    while True:
        print("\nChoose an option:")
        print("1️⃣ Add expense")
        print("2️⃣ View summary")
        print("3️⃣ Exit")
        choice = input("> ")

        if choice == "1":
            try:
                amount = float(input("Amount: $"))
                category = input("Category: ")
                description = input("Description (optional): ")
                add_expense(amount, category, description)
            except ValueError:
                print("❌ Please enter a valid amount.")
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
