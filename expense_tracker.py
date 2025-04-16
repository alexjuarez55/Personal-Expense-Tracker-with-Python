import csv
import os
import matplotlib.pyplot as plt

class ExpenseTracker:

    def __init__(self, filename='expenses'):
        self.filename = filename
        self.expenses = []
        self.budget = 0
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from a CSV file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                self.expenses = [row for row in reader]

    def save_expenses(self):
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)

    def add_expense(self, date, category, amount, description):
        self.expenses.append({
            'date': date,
            'category': category,
            'amount': float(amount),
            'description': description
        })
        self.save_expenses()

    def view_expenses(self):
        print("\nAll Expenses:")
        for expense in self.expenses:

            print(f"Date: {expense['date']}, Category: {expense['category']}, "
                  f"Amount: ${expense['amount']}, Description: {expense['description']}")




    def set_budget(self, budget):
        self.budget = budget
        print(f'Budget set to ${budget:.2f}')

    def calculate_total_spent(self):
        # Calculate the total amount spent
        total_spent = sum(float(expense['amount']) for expense in self.expenses)
        print(f"Total Spent: ${total_spent:.2f}")

        # Check if a budget is set
        if self.budget > 0.00:
            remaining_budget = self.budget - total_spent
            print(f"Remaining Budget: ${remaining_budget:.2f}")
            if remaining_budget < 0:
                print("You have exceeded your budget!")
            else:
                print("You are within your budget.")
        else:
            print("No budget set. Set a budget to track your spending.")

    def visualize_expenses(self):
        categories = {}

        for expense in self.expenses:
            category = expense['category']
            amount = float(expense['amount'])  # Ensure it's a float
            categories[category] = categories.get(category, 0) + amount

        if categories:
            plt.figure(figsize=(8, 6))
            plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
            plt.title('Expenses by Category')
            plt.show()
        else:
            print('No expenses to visualize.')


