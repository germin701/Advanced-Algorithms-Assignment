import threading
import re


class Customer:
    def __init__(self, name, amount, rate, duration):
        self.customer = name
        self.amount = amount
        self.interest_rate = rate
        self.duration = duration

    def repayment(self):
        # Total amount need to pay
        interest_amount = self.amount * (self.interest_rate + 100) / 100
        # Repayment per month
        payment = round(interest_amount / self.duration / 12, 2)
        print(f"{self.customer} Loan Amount: RM {self.amount}\n{self.customer} Interest Rate: {self.interest_rate} %\n"
              f"{self.customer} Duration: {self.duration} years\n{self.customer} Monthly Repayment: RM {payment}\n")


# A list to store 3 customer object
customers = []

# A loop to ask user to input the loan details of 3 customer
for i in range(3):
    print("User " + str(i+1))
    # A loop to ask the user input the name correctly
    while True:
        user_name = str(input("Enter the name of user " + str(i+1) + ": "))

        # Validation of the username by regex
        if not re.match("^[a-zA-Z\s'/-]+$", user_name):
            print("Please reenter a valid name.\n")

        else:
            break

    # A loop to ask user input the loan amount correctly
    while True:
        try:
            loan_amount = int(input("Enter the loan amount of user " + str(i+1) + ": "))

            # Validation of the loan amount
            if loan_amount > 0:
                break

            else:
                print("Please reenter the amount in positive number.\n")

        # Error handling of the loan amount when that is not in integer
        except ValueError:
            print("Please reenter a valid input.\n")

    # A loop to ask user input the interest rate correctly
    while True:
        try:
            loan_rate = float(input("Enter the interest rate of user " + str(i+1) + "(%): "))

            # Validation of the interest rate
            if loan_rate > 0:
                break

            else:
                print("Please reenter the interest rate in positive value.\n")

        # Error handling of the interest rate when that is not in float
        except ValueError:
            print("Please reenter a valid input.\n")

    # A loop to ask user input the loan duration correctly
    while True:
        try:
            loan_duration = int(input("Enter the loan duration of user " + str(i+1) + "(year): "))

            # Validation of the loan duration
            if loan_duration > 0:
                break

            else:
                print("Please reenter the duration in positive number.\n")

        # Error handling of the loan duration when that is not in integer
        except ValueError:
            print("Please reenter a valid input.\n")
    customers.append(Customer(user_name, loan_amount, loan_rate, loan_duration))
    print()

threads = []
for customer in customers:
    thread = threading.Thread(target=customer.repayment())
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
