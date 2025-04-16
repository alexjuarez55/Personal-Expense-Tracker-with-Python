from PasswordSetup import Password
from menu import Menu
from expense_tracker import ExpenseTracker



def main():

    tracker = ExpenseTracker()

    Menu.print_repeated_char('x', 40)
    print()
    print('             Security Center')
    print()
    Menu.print_repeated_char('x', 40)
    print()
    Password.prompt_for_password()


    while True:
        Menu.display_menu()
        print()
        choice = input('Choose an option: ')

        if choice == '1':
            date = input('Enter the data (YYYY-MM-DD: ')
            category = input('Enter category (e.g., Food, Entertainment, Transportation')
            amount = input('Enter amount: ')
            description = input('Enter a description: ')


            tracker.add_expense(date, category, amount, description)
            print(f'Date: {date}, Category: {category}, Amount: {amount}, Description: {description}')
            print('Has been added.')

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            budget = float(input('Enter your budget: '))
            tracker.set_budget(budget)

        elif choice == '4':
            tracker.calculate_total_spent()

        elif choice == '5':
            tracker.visualize_expenses()

        elif choice == '6':
            Password.create_new_password()

        elif choice == '7':
            print("Exiting the Personal Expense Tracker. Goodbye!")
            break






if __name__=="__main__":
    main()
