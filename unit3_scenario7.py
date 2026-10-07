import csv
import re

FILE = "customers.csv"

def load_customers():
    try:
        with open(FILE, "r") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print("File not found!")
        return []


def display_customers(customers):
    for customer in customers:
        print("Account No:", customer["Account"])
        print("Name:", customer["Name"])
        print("Balance:", customer["Balance"])
        print("------------------------")


def search_customer(customers, account):
    # Regular Expression validation
    if not re.fullmatch(r"\d{6}", account):
        print("Invalid account number! Enter 6 digits.")
        return

    for customer in customers:
        if customer["Account"] == account:
            print("Customer Found!")
            print("Account No:", customer["Account"])
            print("Name:", customer["Name"])
            print("Balance:", customer["Balance"])
            return

    print("Customer not found!")


# Main program
customers = load_customers()

while True:
    print("\n--- Bank Customer Record System ---")
    print("1. Display All Customers")
    print("2. Search Account")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_customers(customers)

    elif choice == "2":
        account = input("Enter 6-digit Account Number: ")
        search_customer(customers, account)

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
