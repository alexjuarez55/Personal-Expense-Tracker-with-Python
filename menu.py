


class Menu:
    @staticmethod
    def print_repeated_char(char, times):
        print(char * times)

    @staticmethod
    def display_menu():

        Menu.print_repeated_char('*', 40)
        print()

        print("*    1. Add Expense  💰➕")
        print("*    2. View Expensees  📜👀")
        print("*    3. Set Budget  🎯💵")
        print("*    4. Calculate Total Spent  📊🧮")
        print("*    5. Visualize Expenses  📈🍕")
        print("*    6. Change Password  🔐🔄")
        print("*    7. Exit  🚪👋")

        print()
        Menu.print_repeated_char('*', 40)

