import random
from datetime import datetime

now = datetime.now()
curr_date_time = now.strftime("%A,%dth of %B %Y %H:%M:%S")
print(curr_date_time)
new_user = {}
registered_customer = {2208847740: ["olarindeallitaiwo@gmail.com", "Alli", "Olarinde", 0000]}
database = [new_user, registered_customer]


def generate_account_number():
    """
    :return: The account number generated
    """
    return random.randrange(1111111111, 9999999999)


count = 0  # count the number of times the function runs, i need it to run once


def init():
    """Initializes the banking system"""
    global count
    if count == 0:
        print("Welcome to Polymath bank")
    count = 1
    have_account = int(input("Do you have an account with us? Input 1 for Yes and 2 for No \n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("Invalid selection!!")
        init()


def login():
    """Log in Operations"""
    print("Login to your account")
    account_number_from_user = int(input("What is your account number? \n"))
    pin = int(input("Input your pin \n"))
    for dicts in database:
        for account_number, user_details in dicts.items():
            if account_number != account_number_from_user | account_number != 2208847740:
                print("Account number incorrect, please try again")
                login()
            if user_details[3] != pin | user_details[3] != 0000:
                print("Invalid pin")
                login()
            else:
                bank_operation(user_details)


def register():
    """New registration"""
    print("******** Register ********\n")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    while True:
        try:
            pin = int(input("Create your desired pin, must be 4 digit \n"))
            if len(str(pin)) != 4:
                print("Pin must be 4 digits")
            else:
                break
        except ValueError:
            print("Pin must be an integer, please input again")

    account_number = generate_account_number()
    new_user[account_number] = [email, first_name, last_name, pin]
    print(new_user)
    print("Your account has been created successfully!")
    print("== ==== ===== ===== =====")
    print("Your account number is: %d" % account_number)
    print("== ==== ===== ===== =====")
    login()


def bank_operation(user):
    """
    Bank operation, which includes withdrawal, deposit,
    complaints, logging out and exiting the operation
    :param user: A list containing current user details: First name and Last name
    """
    global count
    if count == 0:
        print(f'Welcome {user[1] + " " + user[2]} to our bank')
    count = 1

    selected_option = int(input(
        "What would you like to do? \ninput (1) for deposit (2) for withdrawal (3) for complaints (4) for logout (5) "
        "for exit\n"))

    if selected_option == 1:
        deposit_operation()
    elif selected_option == 2:
        withdrawal_operation()
    elif selected_option == 3:
        complaints()
    elif selected_option == 4:
        print("Logged out successfully")
        login()
    elif selected_option == 5:
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)


def another_transaction():
    """
    Asks user if needed to perform another transaction
    """
    reply = input("Would you like to perform another transaction? Input (1) for Yes and (2) for No\n")
    if reply == "1":
        login()
    elif reply == "2":
        print("Thank you for banking with us")
        exit()


def withdrawal_operation():
    """Withdrawal operation"""
    while True:
        try:
            amount_to_withdraw = int(input("How much will you like to withdraw? \n"))
            print(f"You have successfully withdraw {amount_to_withdraw}\nPlease take your cash")
            another_transaction()
            break
        except ValueError:
            print("Please input an integer")


def deposit_operation():
    """Deposit operation"""
    while True:
        try:
            amount_to_deposit = int(input("How much will you like to deposit? \n"))
            print(f"You have successfully deposited {amount_to_deposit} to your account")
            another_transaction()
            break
        except ValueError:
            print("Please input an integer")


def complaints():
    """Complaints"""
    issue = input("Please state your complaints \n")
    print("Thank you for contacting us, we will get back to you shortly")


init()
