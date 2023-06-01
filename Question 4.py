import threading


class Customer:
    def __init__(self, name, amount, rate, duration):
        self.customer = name
        self.amount = amount
        # Interest rate in percentage
        self.interest_rate = rate
        self.duration = duration

    def repayment(self):
        # Total amount need to pay
        interest_amount = self.amount * (self.interest_rate + 100) / 100
        # Repayment per month
        payment = round(interest_amount / self.duration / 12, 2)
        print(self.customer, "\nLoan Amount: RM", self.amount, "\nInterest Rate:", self.interest_rate, "%\nDuration:",
              self.duration, "years\nMonthly Repayment: RM", payment, "\n")

customers = []
customer1 = Customer("John", 100000, 3.78, 5)
customers.append(customer1)
customer2 = Customer("Sarah", 230000, 4.22, 8)
customers.append(customer2)
customer3 = Customer("Rachel", 80000, 3.75, 4)
customers.append(customer3)

threads = []
for customer in customers:
    thread = threading.Thread(target=customer.repayment())
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
