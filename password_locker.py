
#!/usr/bin/env python3.6
import pyperclip
# imp
from user import User
from user import Credential


def create_user(first_name, last_name, email, phone_number, password):
    '''
    Function to create a new user account
    '''
    new_user = User(first_name, last_name, email, phone_number, password)
    return new_user


def create_credential(user_name, site_name, account_name, password):
    '''
    Function to create a new user account
    '''
    new_credential = Credential(user_name, site_name, account_name, password)
    return new_credential


def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)


def save_credentials(credential):
    '''
    Function to save a new user account
    '''
    Credential.save_credentials(credential)


def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credential.check_user(first_name, password)
    return checking_user


def generate_password(pass_len):
    '''
    A funtion to generate password, combining random letters and digits
    '''
    return Credential.generate_password(pass_len)


@classmethod
def find_by_site_name(cls, site_name):
    '''
    A function to search for credentials when given an account site search as google, or twitter.
    '''
    return cls.find_by_site_name(cls, site_name)


@classmethod
def copy_credentials(cls, site_name):
    '''
    A class method to enable us to copy credentials of a given site name.
    '''
    return cls.copy_credentials(cls, site_name)


def main():
    guest_name = input("What is your name?")
    print(f"Hello {guest_name}, welcome to Password Locker:")
    print('\n')
    while True:
        print('\n')
        print(r"*"*30)
        print('\n')
        print("Use these short codes to navigate through Password_Locker:\n ln to log in \n ca to create a new account. \n ex to exit")
        print('\n')
        short_code = input().lower()
        if short_code == 'ca':
            print("New Account")
            print("-"*10)
            print("Enter First Name ...")
            first_name = input()
            print("Enter Last Name ...")
            last_name = input()
            print("Enter Phone Number ...")
            phone_number = input()
            print(" Enter Email Address ...")
            email = input()
            # p_word = input("Enter a password you can remember")
            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit... ")
            password_choice = input()
            password = ''
            if password_choice == 'cyo':
                password = password.join(
                    input("Enter a password of your choice..."))
                # break
            elif password_choice == 'gp':
                print("Enter the length of the password you wish to generate eg 9 ")
                pass_len = input()
                password = password.join(
                    Credential.generate_password(pass_len))
                # break
            elif password_choice == 'ex':
                break
            else:
                print("Sorry I did not get that. Please try again")
                # password = input("Enter a password of your choice...")
            # Create and save new user
            save_user(create_user(first_name, last_name,
                                  email, phone_number, password))
            print('\n')
            print(f"New Account for {first_name} {last_name} created.")
            print('\n')
            print(
                f"Your password is {password} :-Use it to log in using short code ln")
            print('\n')
        elif short_code == 'ln':
            print('\n')
            print("Enter your account details to log in: \n Enter your first name...")
            first_name = input()
            print("Enter your password...")
            password = input()
            account_exist = verify_user(first_name, password)
            if account_exist == first_name:
                print('\n')
                print(
                    f"Welcome to your Password locker account {first_name}: \n Please choose an option to continue...")
                print('\n')
                while True:
                    print('\n')
                    print("Navigation short codes: \n cc to create new credentials: \n dc to display credentials: \n sc to search credentials: \n rm to remove or delete credentials: \n copy to copy credentials: \n ex to exit")
                    print('\n')
                    short_code = input().lower()
                    if short_code == 'cc':
                        print('\n')
                        print("Enter your credential details")
                        print("Enter account type... eg \'google\'")
                        account_name = input()
                        print(f"Enter username ")
                        user_name = input()
                        print(f"Enter site name")
                        site_name = input()
                        print(
                            f"Enter the username you used or would love to use on {site_name}")
                        user_name = input()
                        while True:
                            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit... ")
                            password_choice = input()
                            if password_choice == 'cyo':
                                password = input(
                                    "Enter a password of your choice...")
                                break
                            elif password_choice == 'gp':
                                print(
                                    "Enter the length of the password you wish to generate eg 9 ")
                                pass_len = input()
                                pass_len = int(pass_len)
                                password = Credential.generate_password(
                                    pass_len)
                                break
                            elif password_choice == 'ex':
                                break
                            else:
                                print("Sorry I did not get that. Please try again")
                        # return at_password
                        save_credentials(create_credential(
                            user_name, site_name, account_name, password))
                        print(' \n')
                        print(
                            f'Credential Created:\n Account type: {site_name}  \n Account Username: {user_name} \n Account Password: {password}')
                        print('\n ')

                    else:
                        print("I did not get that, please try again")
            else:
                print(
                    f"Sorry, we could not find any account under the name {first_name}")
                print('\n')
        elif short_code == 'ex':
            break
        else:
            print("I really did not get that, please use the short code ")


print('\n')
if __name__ == '__main__':
    main()
