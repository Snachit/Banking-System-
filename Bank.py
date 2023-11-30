import random
import csv

class BankAccount:
    def __init__(self, client_id, balance=0):
        self.client_id = client_id
        self.account_number = int(str(client_id) + str(random.randint(0, 100)))
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} units. New balance: {self.balance}")

    def display_info(self):
        print(f"Client ID: {self.client_id}, Account Number: {self.account_number}, Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.client_secret = {}
        self.client_account = {}

    def add_account(self, client_id):
        if client_id not in self.accounts:
            new_account = BankAccount(client_id)
            self.accounts[client_id] = new_account
            secret = input(f"Set a secret code for client {client_id}: ")
            self.client_secret[client_id] = secret
            self.client_account[client_id] = new_account.account_number
            print(f"Account created successfully for client {client_id}.")
        else:
            print(f"Account already exists for client {client_id}.")

    def remove_account(self, client_id):
        if client_id in self.accounts:
            del self.accounts[client_id]
            del self.client_secret[client_id]
            del self.client_account[client_id]
            print(f"Account removed successfully for client {client_id}.")
        else:
            print(f"No account found for client {client_id}.")

    def display_accounts(self):
        for account in self.accounts.values():
            account.display_info()

    def client_menu(self, client_id):
        while True:
            print("\nClient Menu:")
            print("1. Modify Password")
            print("2. Display Balance")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                new_password = input("Enter a new password: ")
                self.client_secret[client_id] = new_password
                print("Password modified successfully.")

            elif choice == '2':
                account_number = self.client_account[client_id]
                print(f"Your balance is: {self.accounts[client_id].balance}")

            elif choice == '3':
                amount = float(input("Enter the amount to deposit: "))
                self.accounts[client_id].deposit(amount)

            elif choice == '4':
                amount = float(input("Enter the amount to withdraw: "))
                self.accounts[client_id].withdraw(amount)

            elif choice == '5':
                print("Exiting client menu. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    def ajouterClient(self, numCl, MPC, numC, SoldeC):
        self.client_secret[numCl] = MPC
        self.accounts[numCl] = BankAccount(numCl, SoldeC)
        self.client_account[numCl] = numC

    def supprimerClient(self, numC):
        if numC in self.accounts:
            del self.accounts[numC]
            for client, account in self.client_account.items():
                if account == numC:
                    del self.client_secret[client]
                    del self.client_account[client]
                    break
            print(f"Client with account {numC} deleted successfully.")
        else:
            print(f"No account found with number {numC}.")

def modifierMPClient(bank, client_id, new_password):
    if client_id in bank.client_secret:
        bank.client_secret[client_id] = new_password
        print("Password modified successfully.")
    else:
        print(f"Client {client_id} not found.")

def deposer(bank, client_id, amount):
    if client_id in bank.client_account:
        account_number = bank.client_account[client_id]
        if account_number in bank.accounts:
            bank.accounts[account_number].deposit(amount)
        else:
            print(f"Account {account_number} not found.")
    else:
        print(f"Client {client_id} not found.")

def retirer(bank, client_id, amount):
    if client_id in bank.client_account:
        account_number = bank.client_account[client_id]
        if account_number in bank.accounts:
            bank.accounts[account_number].withdraw(amount)
        else:
            print(f"Account {account_number} not found.")
    else:
        print(f"Client {client_id} not found.")


# generation de numero de compte a partir de numero de client
genererNumCompte = lambda numCl: int(str(numCl) + str(random.randint(0, 100)))

def EcrireFichierCSV(bank, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Client', 'Code Secret']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for client, code_secret in bank.client_secret.items():
            writer.writerow({'Client': client, 'Code Secret': code_secret})
    print(f"Client information written to {filename}.")

def manipSTS(bank):
    compte_set = set(bank.client_account.values())
    compte_list = list(compte_set)
    compte_tuple = tuple(compte_list)
    return compte_list, compte_tuple, compte_set

#La Creation de banque
bank = Bank()

while True:
    print("\nMain Menu:")
    print("1. Bank Agent Menu")
    print("2. Client Menu")
    print("3. Quit")

    main_choice = input("Enter your choice: ")

    if main_choice == '1':
        print("\nBank Agent Menu:")
        print("1. Add a Client")
        print("2. Remove a Client")
        print("3. Display all Clients")
        print("4. Write to CSV")
        print("5. Manipulate Sets, Lists, and Tuples")
        print("6. Quit")

        agent_choice = input("Enter your choice: ")

        if agent_choice == '1':
            numCl = int(input("Enter client ID: "))
            MPC = input("Enter client password: ")
            numC = genererNumCompte(numCl)
            SoldeC = float(input("Enter initial balance: "))
            bank.ajouterClient(numCl, MPC, numC, SoldeC)

        elif agent_choice == '2':
            numC = int(input("Enter account number to remove: "))
            bank.supprimerClient(numC)

        elif agent_choice == '3':
            print("Clients:")
            for client, code_secret in bank.client_secret.items():
                print(f"Client {client}: Code Secret - {code_secret}")

        elif agent_choice == '4':
            filename = input("Enter CSV file name: ")
            EcrireFichierCSV(bank, filename)

        elif agent_choice == '5':
            compte_list, compte_tuple, compte_set = manipSTS(bank)
            print(f"List: {compte_list}")
            print(f"Tuple: {compte_tuple}")
            print(f"Set: {compte_set}")

        elif agent_choice == '6':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    elif main_choice == '2':
        client_id = int(input("Enter your client ID: "))
        if client_id in bank.client_secret:
            password = input("Enter your password: ")
            if password == bank.client_secret[client_id]:
                bank.client_menu(client_id)
            else:
                print("Incorrect password. Access denied.")
        else:
            print("Client not found.")

    elif main_choice == '3':
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
