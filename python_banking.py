class Account:

    def __init__(self, name, email, phone_number, password):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.balance = 1000 

    def account_details(self):
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print(f'Phone number: {self.phone_number}')
        print('--------------------------------')
        print('Would you like to;')
        print('1) Return to homepage')
        print('2) Quit')
        while True:
            account_details_choice = input('Enter here: ')
            if account_details_choice == '1':
                homepage()
            elif account_details_choice == '2':
                quit()
            else:
                print('Invalid input, try again.')
                continue

    def bank_account(self):
        print(f'Account: £{self.balance}')

    def account_deposit(self):
        while True:
            deposit_amount = float(input('How much would you like to deposit: £'))
            print('Enter password to confirm transaction or [c] to change amount.')
            confirm_deposit = input('Enter here: ')
            if confirm_deposit == self.password:
                break
            elif confirm_deposit == 'c':
                continue 
            else:
                print('Invalid input, try again.')
                continue
        self.balance += deposit_amount
        print('--------------------------------')
        print(f'Deposited £{deposit_amount}')
        print(f'Balance: £{self.balance}')
        homepage()

    def account_withdraw(self):
        while True:
            withdraw_amount = float(input('How much would you like to withdraw: £'))
            if withdraw_amount > self.balance:
                print(f'Unable to make transaction as you have £{self.balance} in your' 
                f' account and are trying to withdraw £{withdraw_amount}')
                continue
            print('Enter password to confirm transaction or [c] to change amount being withdrawn.')
            confirm_withdraw = input('Enter here: ')
            if confirm_withdraw == self.password:
                break
            elif confirm_withdraw == 'c':
                continue
            else:
                print('Invalid input, try again.')
                continue
        self.balance -= withdraw_amount
        print('--------------------------------')
        print(f'Withdrawn £{withdraw_amount}')
        print(f'Balance: £{self.balance}')
        homepage()


def homepage():
    while True:
        print('--------------------------------')
        print('Would you like to;')
        print('1) View account details')
        print('2) View bank account')
        print('3) Make a deposit')
        print('4) Make a withdrawl')
        print('5) Quit')
        choice = input('Enter here: ')

        if choice == '1':
            print('--------------------------------')
            account_1.account_details()
            break
        elif choice == '2':
            print('--------------------------------')
            account_1.bank_account()
        elif choice == '3':
            print('--------------------------------')
            account_1.account_deposit()
        elif choice == '4':
                print('--------------------------------')
                account_1.account_withdraw()
        elif choice == '5':
            quit()
        else:
            print('Invalid input, enter only 1, 2, 3, 4, or 5.')
            continue


name = input('Enter full name: ')
email = input('Enter email: ')
while True:
    phone_number = input('Enter phone number: ')
    if len(phone_number) != 11:
        print('Invalid phone number')
        continue
    else:
        break
password = input('Set a password: ')
while True:
    password_confirm = input('Confirm password here: ')
    if password_confirm != password:
        print('Password does not match.')
        continue
    else:
        break

account_1 = Account(name, email, phone_number, password)


homepage()
