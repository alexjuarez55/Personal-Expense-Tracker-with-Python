import os

class Password:
    @staticmethod
    def prompt_for_password():
        try:
            with open('password.txt', 'r') as file:
                saved_password = file.read().strip()

            entered_password = input('Enter your password: ')
            if entered_password == saved_password:
                print('Access granted.')
                if saved_password == 'Default':
                    update = input('Would you like to update the password? (y/n): ').strip().lower()
                    if update == 'y':
                        create_new_password()

                else:
                    print('Incorrect assoword')

        except FileNotFoundError:
            print('Password file not found. Please make sure password.txt exists.')

    @staticmethod
    def create_new_password():
        while True:
            new_password = input("Create a new password: ")
            confirm_password = input("Enter your new password again: ")
            if new_password == confirm_password:
                # Write the new password to the file
                with open('password.txt', 'w') as file:
                    file.write(new_password)
                print('Password updated successfully!')
                break
            else:
                print("Passwords do not match. Please try again.")


