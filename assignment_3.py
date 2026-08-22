from abc import ABC, abstractmethod


# Strategy Interface
class PaymentMethod(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass


# Strategy 1
class CardPayment(PaymentMethod):

    def make_payment(self, amount):
        print("Amount:", amount)
        print("Payment completed using Card.")


# Strategy 2
class UpiPayment(PaymentMethod):

    def make_payment(self, amount):
        print("Amount:", amount)
        print("Payment completed using UPI.")


# Strategy 3
class CashPayment(PaymentMethod):

    def make_payment(self, amount):
        print("Amount:", amount)
        print("Payment completed using Cash.")


# Strategy 4
class BankPayment(PaymentMethod):

    def make_payment(self, amount):
        print("Amount:", amount)
        print("Payment completed using Net Banking.")


# Context Class
class PaymentSystem:

    def __init__(self):
        self.method = None

    def select_method(self, method):
        self.method = method

    def pay(self, amount):

        if self.method is None:
            print("Please select a payment method.")
        else:
            self.method.make_payment(amount)


# Main Program
payment = PaymentSystem()

while True:

    print("\n===== PAYMENT SYSTEM =====")
    print("1. Card Payment")
    print("2. UPI Payment")
    print("3. Cash Payment")
    print("4. Net Banking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using the Payment System.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        continue

    amount = float(input("Enter amount: "))

    if choice == "1":
        payment.select_method(CardPayment())

    elif choice == "2":
        payment.select_method(UpiPayment())

    elif choice == "3":
        payment.select_method(CashPayment())

    elif choice == "4":
        payment.select_method(BankPayment())

    payment.pay(amount)



OUTPUT

===== PAYMENT SYSTEM =====
1. Card Payment
2. UPI Payment
3. Cash Payment
4. Net Banking
5. Exit

Enter your choice: 2
Enter amount: 1500

Amount: 1500.0
Payment completed using UPI.

===== PAYMENT SYSTEM =====
1. Card Payment
2. UPI Payment
3. Cash Payment
4. Net Banking
5. Exit

Enter your choice: 1
Enter amount: 2500

Amount: 2500.0
Payment completed using Card.

===== PAYMENT SYSTEM =====
1. Card Payment
2. UPI Payment
3. Cash Payment
4. Net Banking
5. Exit

Enter your choice: 5
Thank you for using the Payment System.
