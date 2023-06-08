import pyfiglet
import os
import re
import random


class Program:
    def __init__(self):
        self.order_id = int
        self.quantity = int
        self.total = 0

        # Create a dictionary to store order and cake object
        self.order_object = {}
        self.cake_object = {}

        # Starting of the program
        print(pyfiglet.figlet_format("WELCOME", font="cursive", justify="center", width=125))

        # A loop to ask user input their member/customer id correctly
        while True:
            try:
                customer_id = int(input("Enter your member id: "))
                # Validation of the customer id
                if customer_id > 0:
                    break
                else:
                    print("Please reenter a valid member id.\n")
            # Error handling of the customer id when that is not in integer
            except ValueError:
                print("Please reenter a valid customer id.\n")

        # A loop to ask the user input their name correctly
        while True:
            customer_name = str(input("Enter your name: "))
            # Validation of the customer name by regex
            if not re.match("^[a-zA-Z\s'/-]+$", customer_name):
                print("Please reenter a valid name.\n")
            else:
                break

        # A loop to ask the user input their address correctly
        while True:
            location = str(input("Enter the address of the location: "))
            # Validation of the location address by regex
            if not re.match(r"^[a-zA-Z0-9\s,./'-]{3,}$", location):
                print("Please reenter a valid location.\n")
            else:
                break

        # A loop to ask the user input their contact number correctly
        while True:
            try:
                phone = int(input("Enter your phone number: "))
                # Validation of the contact number
                if phone > 0:
                    if 9 <= len(str(phone)) <= 10:
                        break
                    else:
                        print("Please reenter a valid phone number.\n")
                else:
                    print("Please reenter a valid phone number.\n")
            # Error handling of the contact number when that is not in integer
            except ValueError:
                print("Please reenter a valid phone number.\n")

        # Print out the customer details
        print("\n##################################################\nCustomer id: " + str(customer_id) + "\nName: " +
              customer_name + "\nAddress: " + location + "\nPhone number: 0" + str(phone) + "\n########################"
                                                                                            "##########################"
                                                                                            "\n")

        # A loop to ask the user confirm the infomation they provided
        while True:
            print("Please confirm the infomation you provided is correct to order your cake.")
            confirm_info = str(input("Are you confirm? (yes/no)\n")).upper()

            # Validation of the confirmation
            if confirm_info == "YES":
                # Create an object to the Customer class
                self.cus = Customer(customer_id, customer_name, location, phone)
                os.system("cls")
                self.menu()
                return

            elif confirm_info == "NO":
                os.system("cls")
                Program()
                return

            else:
                print("Please enter a valid input.\n")

    # A menu page
    def menu(self):
        print(pyfiglet.figlet_format("WELCOME", font="cursive", justify="center", width=125))
        # Display the menu
        print("1. Add new cake order".center(120))
        print("2. View cake order list".center(122))
        print("3. Edit cake order".center(115))
        print("4. Cancel cake order".center(117))
        print("*press other number to exit*".center(122))

        # A loop to ask the user input the selection from the menu
        while True:
            try:
                menu = int(input("\n\t\t\t\t\t   Enter a number to choose from menu: "))
                break
            # Error handling of the selection when that is not in integer
            except ValueError:
                print("Please reenter in a valid number.".center(125))

        # Validation of the selection
        if menu == 1:
            os.system("cls")
            self.add()

        elif menu == 2:
            os.system("cls")
            self.view()

        elif menu == 3:
            os.system("cls")
            self.edit()

        elif menu == 4:
            os.system("cls")
            self.delete()

        else:
            quit()

    # Place order page
    def add(self):
        print("***Add new cake order***")

        # A loop to ask the user input the selection of the cake flavor
        while True:
            try:
                # Display the cake flavor available
                print("1. Strawberry\n2. Chocolate\n3. Matcha\n*press other number to go back to the menu*\n")
                flavors = int(input("Enter a number to select the flavor of cake: "))

                # Validation of the selection of the cake flavor
                if flavors == 1:
                    flavor = "Strawberry"
                    break

                elif flavors == 2:
                    flavor = "Chocolate"
                    break

                elif flavors == 3:
                    flavor = "Matcha"
                    break

                else:
                    # A loop asks the user to confirm whether to exit this page
                    while True:
                        confirm_infomation = str(input("The order is not save. Are you sure want to exit? (yes/no)\n"))\
                            .upper()

                        # Validation of the confirmation
                        if confirm_infomation == "YES":
                            os.system("cls")
                            self.menu()
                            return

                        elif confirm_infomation == "NO":
                            os.system("cls")
                            self.add()
                            return

                        else:
                            print("Please enter a valid input.\n")

            # Error handling of the selection of the cake flavor when that is not in integer
            except ValueError:
                os.system('cls')
                print("Please reenter in number.\n")

        # Display the cake weight available
        print("\n1. 250 -- RM30\n2. 500 -- RM60\n3. 750 -- RM120\n4. 1000 -- RM180\n*press other number to go back to "
              "the menu*\n")

        # A loop to ask user input the selection of the cake weight
        while True:
            try:
                size = int(input("Enter a number to select the weight of the cake(gram): "))

                # Validation of the selection of the cake weight
                if size == 1:
                    weight = 250
                    price = 30
                    break

                elif size == 2:
                    weight = 500
                    price = 60
                    break

                elif size == 3:
                    weight = 750
                    price = 120
                    break

                elif size == 4:
                    weight = 1000
                    price = 180
                    break

                else:
                    # A loop asks the user to confirm whether to exit this page
                    while True:
                        confirm_massage = str(input("The order is not save. Are you sure want to exit? (yes/no)\n")). \
                            upper()

                        # Validation of the confirmation
                        if confirm_massage == "YES":
                            os.system("cls")
                            self.menu()
                            return

                        elif confirm_massage == "NO":
                            print("")
                            break

                        else:
                            print("Please enter a valid input.\n")

            # Error handling of the selection of the cake weight when that is not in integer
            except ValueError:
                print("Please reenter in number.\n")

        # A loop to ask user input the quantity of the cake
        while True:
            try:
                print("\n*press 0 to go back to the menu*")
                quantity = int(input("Enter the quantity of the cake: "))

                # Validation of the cake quantity
                if quantity == 0:
                    # A loop asks the user to confirm whether to exit this page
                    while True:
                        confirm_massage = str(input("The order is not save. Are you sure want to exit? (yes/no)\n")). \
                            upper()

                        # Validation of the confirmation
                        if confirm_massage == "YES":
                            os.system("cls")
                            self.menu()
                            return

                        elif confirm_massage == "NO":
                            print("")
                            break

                        else:
                            print("Please enter a valid input.\n")

                elif quantity < 0:
                    print("Please enter a valid quantity.")

                else:
                    break

            # Error handling of the quantity of the cake when that is not in integer
            except ValueError:
                print("Please enter a valid input.\n")

        self.total = price * quantity
        self.quantity = quantity

        # Display the details of the order
        print("\n##################################################\nFlavor: " + flavor + "\nWeight: " + str(weight) +
              " gram\nUnit Price: RM " + str(price) + "\nQuantity: " + str(quantity) + "\nTotal: RM " + str(self.total)
              + "\n##################################################")

        # A loop to ask the user confirm the order
        while True:
            print("\nPlease confirm your cake order.")
            confirm_order = str(input("Are you confirm? (yes/no)\n")).upper()

            # Validation of the confirmation
            if confirm_order == "YES":
                if flavor == "Strawberry":
                    if size == 1:
                        cake_code = 1
                    elif size == 2:
                        cake_code = 2
                    elif size == 3:
                        cake_code = 3
                    else:
                        cake_code = 4

                elif flavor == "Chocolate":
                    if size == 1:
                        cake_code = 5
                    elif size == 2:
                        cake_code = 6
                    elif size == 3:
                        cake_code = 7
                    else:
                        cake_code = 8

                else:
                    if size == 1:
                        cake_code = 9
                    elif size == 2:
                        cake_code = 10
                    elif size == 3:
                        cake_code = 11
                    else:
                        cake_code = 12

                # Random generate order id
                self.order_id = random.randint(1, 10000)

                # Insert order id to BST
                self.order_id = bst.insert(self.order_id)

                # Add cake and order object to the dictionary
                self.cake_object[self.order_id] = Cake(cake_code, flavor, weight, price)
                self.order_object[self.order_id] = Order(self.cake_object[self.order_id], self.cus, self)

                print("Order added.\nThank you for your support!!!\n")

                # A loop to ask user whether to place an order again
                while True:
                    again = str(input("\nDo you want to order again? (yes/no)\n")).upper()

                    # Validation of the user input
                    if again == "YES":
                        os.system("cls")
                        self.add()
                        return

                    elif again == "NO":
                        os.system("cls")
                        self.menu()
                        return

                    else:
                        print("Please enter a valid input.")

            elif confirm_order == "NO":
                # A loop to ask user whether to place an order again
                while True:
                    again = str(input("\nDo you want to order again? (yes/no)\n")).upper()

                    # Validation of the user input
                    if again == "YES":
                        os.system("cls")
                        self.add()
                        return

                    elif again == "NO":
                        os.system("cls")
                        self.menu()
                        return

                    else:
                        print("Please enter a valid input.")

            else:
                print("Please enter a valid input.")

    # View order page
    def view(self):
        # If the BST is empty
        if bst.size() == 0:
            print("***View order details***\nYou have " + str(bst.size()) + " order.\nNothing show here......\n\n*press"
                                                                            " enter to go back to the menu*")
            input()
            os.system("cls")
            self.menu()

        else:
            # A loop to ask user input the order id
            while True:
                try:
                    # Display the order in the BST
                    print("***View order details***\nYou have " + str(bst.size()) + " order.\nHere is the order list in"
                                                                                    " order id:")
                    bst.display()

                    print("\nChoose an order id that display above to view that order details.\n*press 0 to go back to"
                          " the menu*")
                    detail = int(input("Order id: "))

                    # Validation of the order id
                    if detail == 0:
                        os.system("cls")
                        self.menu()
                        return

                    else:
                        # Validate the order id exist in the BST
                        if bst.search(detail):
                            os.system("cls")

                            # Retrieve the order object from the dictionary
                            order = self.order_object[detail]

                            # Display the order details
                            print("***Order Details***\n\nOrder ID:", order.order_id, "\nCustomer ID:",
                                  order.customer_id, "\nCustomer Name:", order.customer_name, "\nCustomer Address:",
                                  order.customer_address, "\nCustomer Contact:", order.customer_contact, "\nCake Code:",
                                  order.cake_code, "\nCake Flavor:", order.cake_flavor, "\nCake Weight:",
                                  order.cake_weight, "gram\nCake Unit Price: RM", order.cake_price, "\nCake Quantity:",
                                  order.cake_quantity, "\nTotal: RM", order.total)

                            # A loop to ask user whether to view an order again
                            while True:
                                view = str(input("\nDo you want to view your order again? (yes/no)\n")).upper()

                                # Validation of the user input
                                if view == "YES":
                                    os.system("cls")
                                    self.view()
                                    return

                                elif view == "NO":
                                    os.system("cls")
                                    self.menu()
                                    return

                                else:
                                    print("Please enter a valid input.")

                        else:
                            os.system("cls")
                            print("Please choose the order id that show in the list.\n")

                # Error handling of the order id when that is not in integer
                except ValueError:
                    os.system("cls")
                    print("Please enter a valid input.\n")

    # Modify order page
    def edit(self):
        # If the BST is empty
        if bst.size() == 0:
            print("***Edit cake order***\nYou have " + str(bst.size()) + " order.\nNothing show here......\n\n*press "
                                                                         "enter to go back to the menu*")
            input()
            os.system("cls")
            self.menu()
        else:
            # A loop to ask user input the order id
            while True:
                # Display the order in the BST
                print("***Edit cake order***\nYou have " + str(bst.size()) + " order.\nHere is the order list in order "
                                                                             "id:")
                bst.display()

                print("\nChoose an order id that display above to edit that order details.\n*press 0 to go back to the "
                      "menu*")
                try:
                    details = int(input("Order id: "))

                    # Validation of the order id
                    if details == 0:
                        os.system("cls")
                        self.menu()
                        return

                    else:
                        # Validate the order id exist in the BST
                        if bst.search(details):
                            os.system("cls")

                            # Retrieve the cake and order object from the dictionary
                            order = self.order_object[details]
                            cake = self.cake_object[details]
                            confirm_infomation = str

                            # A loop to ask user input an attribute to modify
                            while True:
                                # Display the order details
                                print("***Order Details***\n\nOrder ID:", order.order_id, "\nCake Code:",
                                      order.cake_code, "\n1. Cake Flavor:", order.cake_flavor, "\n2. Cake Weight:",
                                      order.cake_weight, "gram\n3. Cake Quantity:", order.cake_quantity,
                                      "\nCake Unit Price: RM", cake.price, "\nTotal: RM", order.total,
                                      "\n\n*press other number to go back to the order list*")
                                try:
                                    attribute = int(input("Enter a number to modify the selected attribute: "))

                                    # Validation of the attribute
                                    if attribute == 1:
                                        os.system("cls")
                                        new_flavor = int

                                        # A loop to ask user input the new flavor of cake
                                        while True:
                                            try:
                                                # Display the cake flavor available
                                                print("***Modify Cake Flavor***\n\n1. Strawberry\n2. Chocolate\n3. "
                                                      "Matcha\n*press other number to go back to the order details*\n")

                                                new_flavour = int(input("Enter a number to select the flavor of cake: ")
                                                                  )

                                                # Validation of the new flavor of cake
                                                if new_flavour == 1:
                                                    new_flavor = "Strawberry"
                                                    break

                                                elif new_flavour == 2:
                                                    new_flavor = "Chocolate"
                                                    break

                                                elif new_flavour == 3:
                                                    new_flavor = "Matcha"
                                                    break

                                                else:
                                                    # A loop asks the user to confirm whether to exit this page
                                                    while True:
                                                        confirm_infomation = str(input("The order is notting update. "
                                                                                       "Are you sure want to exit? "
                                                                                       "(yes/no)\n")).upper()

                                                        # Validation of the confirmation
                                                        if confirm_infomation == "YES":
                                                            break

                                                        elif confirm_infomation == "NO":
                                                            os.system("cls")
                                                            break

                                                        else:
                                                            print("Please enter a valid input.\n")

                                                    # Break the loop that ask user to input the new flavor of the cake
                                                    if confirm_infomation == "YES":
                                                        break

                                            # Error handling of the cake flavor when that is not in integer
                                            except ValueError:
                                                os.system("cls")
                                                print("Please reenter in number.\n")

                                        # A loop to ask the user confirm update the order
                                        while True:
                                            # To exit this loop when the user want to exit previously
                                            if confirm_infomation == "YES":
                                                confirm_infomation = None
                                                os.system("cls")
                                                break

                                            confirm_flavor = str(input("Are you confirm to update the cake flavor? "
                                                                       "(yes/no)\n")).upper()

                                            # Validation of the confirmation
                                            if confirm_flavor == "YES":
                                                if new_flavor == "Strawberry":
                                                    if order.cake_weight == 250:
                                                        new_cake_code = 1

                                                    elif order.cake_weight == 500:
                                                        new_cake_code = 2

                                                    elif order.cake_weight == 750:
                                                        new_cake_code = 3

                                                    else:
                                                        new_cake_code = 4

                                                elif new_flavor == "Chocolate":
                                                    if order.cake_weight == 250:
                                                        new_cake_code = 5

                                                    elif order.cake_weight == 500:
                                                        new_cake_code = 6

                                                    elif order.cake_weight == 750:
                                                        new_cake_code = 7

                                                    else:
                                                        new_cake_code = 8

                                                else:
                                                    if order.cake_weight == 250:
                                                        new_cake_code = 9

                                                    elif order.cake_weight == 500:
                                                        new_cake_code = 10

                                                    elif order.cake_weight == 750:
                                                        new_cake_code = 11

                                                    else:
                                                        new_cake_code = 12

                                                # Update the cake code and flavor to order class and cake class
                                                order.cake_code = new_cake_code
                                                order.cake_flavor = new_flavor
                                                cake.cake_id = new_cake_code
                                                cake.flavor = new_flavor

                                                # Display status
                                                print("\n###### Cake flavor has been updated to", new_flavor, "######")
                                                input("\nPress enter to continue.")
                                                os.system("cls")
                                                break

                                            elif confirm_flavor == "NO":
                                                # Display status
                                                print("\n###### No change to cake flavor ######")
                                                input("\nPress enter to continue.")
                                                os.system("cls")
                                                break

                                            else:
                                                print("Please enter a valid input.\n")

                                    elif attribute == 2:
                                        os.system("cls")
                                        new_weight = int
                                        new_price = int

                                        # A loop to ask user input the new weight of the cake
                                        while True:
                                            try:
                                                # Display the cake weight available
                                                print("***Modify Cake Weight***\n\n1. 250 -- RM30\n2. 500 -- RM60\n3. "
                                                      "750 -- RM120\n4. 1000 -- RM180\n*press other number to go back "
                                                      "to the order details*\n")

                                                new_weigh = int(input("Enter a number to select the weight of cake"
                                                                      "(gram): "))

                                                # Validation of the new weight of cake
                                                if new_weigh == 1:
                                                    new_weight = 250
                                                    new_price = 30
                                                    break

                                                elif new_weigh == 2:
                                                    new_weight = 500
                                                    new_price = 60
                                                    break

                                                elif new_weigh == 3:
                                                    new_weight = 750
                                                    new_price = 120
                                                    break

                                                elif new_weigh == 4:
                                                    new_weight = 1000
                                                    new_price = 180
                                                    break

                                                else:
                                                    # A loop asks the user to confirm whether to exit this page
                                                    while True:
                                                        confirm_infomation = str(input("The order is notting update. "
                                                                                       "Are you sure want to exit? "
                                                                                       "(yes/no)\n")).upper()

                                                        # Validation of the confirmation
                                                        if confirm_infomation == "YES":
                                                            break

                                                        elif confirm_infomation == "NO":
                                                            os.system("cls")
                                                            break

                                                        else:
                                                            print("Please enter a valid input.\n")

                                                    # Break the loop that ask user to input the new weight of the cake
                                                    if confirm_infomation == "YES":
                                                        break

                                            # Error handling of the cake weight when that is not in integer
                                            except ValueError:
                                                os.system("cls")
                                                print("Please reenter in number.\n")

                                        # A loop to ask the user confirm update the order
                                        while True:
                                            # To exit this loop when the user want to exit previously
                                            if confirm_infomation == "YES":
                                                confirm_infomation = None
                                                os.system("cls")
                                                break

                                            confirm_weight = str(input("Are you confirm to update the cake weight? "
                                                                       "(yes/no)\n")).upper()

                                            # Validation of the confirmation
                                            if confirm_weight == "YES":
                                                if order.cake_flavor == "Strawberry":
                                                    if new_weight == 250:
                                                        new_cake_code = 1

                                                    elif new_weight == 500:
                                                        new_cake_code = 2

                                                    elif new_weight == 750:
                                                        new_cake_code = 3

                                                    else:
                                                        new_cake_code = 4

                                                elif order.cake_flavor == "Chocolate":
                                                    if new_weight == 250:
                                                        new_cake_code = 5

                                                    elif new_weight == 500:
                                                        new_cake_code = 6

                                                    elif new_weight == 750:
                                                        new_cake_code = 7

                                                    else:
                                                        new_cake_code = 8

                                                else:
                                                    if new_weight == 250:
                                                        new_cake_code = 9

                                                    elif new_weight == 500:
                                                        new_cake_code = 10

                                                    elif new_weight == 750:
                                                        new_cake_code = 11

                                                    else:
                                                        new_cake_code = 12

                                                # Update the cake code, weight, unit price and total price to order
                                                # class and cake class
                                                new_total = new_price * order.cake_quantity
                                                order.cake_code = new_cake_code
                                                order.cake_weight = new_weight
                                                order.total = new_total
                                                cake.cake_id = new_cake_code
                                                cake.weight = new_weight
                                                cake.price = new_price

                                                # Display status
                                                print("\n###### Cake weight has been updated to", new_weight, "gram "
                                                                                                              "######")
                                                input("\nPress enter to continue.")
                                                os.system("cls")
                                                break

                                            elif confirm_weight == "NO":
                                                # Display status
                                                print("\n##### No change to cake weight ######")
                                                input("\nPress enter to continue.")
                                                os.system("cls")
                                                break

                                            else:
                                                print("Please enter a valid input.\n")

                                    elif attribute == 3:
                                        os.system("cls")

                                        # A loop to ask user input the new quantity of the cake
                                        while True:
                                            try:
                                                print("***Modify Cake Quantity***\n\n*press 0 to go back to the order "
                                                      "details*")
                                                new_quantity = int(input("Enter the quantity of the cake: "))

                                                # Validation of the new quantity of cake
                                                if new_quantity == 0:
                                                    # A loop asks the user to confirm whether to exit this page
                                                    while True:
                                                        confirm_infomation = str(input("The order is notting update. "
                                                                                       "Are you sure want to exit? "
                                                                                       "(yes/no)\n")).upper()

                                                        # Validation of the confirmation
                                                        if confirm_infomation == "YES":
                                                            break

                                                        elif confirm_infomation == "NO":
                                                            os.system("cls")
                                                            break

                                                        else:
                                                            print("Please enter a valid input.\n")

                                                    # Break the loop that ask user to input the new quantity of the cake
                                                    if confirm_infomation == "YES":
                                                        os.system("cls")
                                                        break

                                                elif new_quantity < 0:
                                                    # Display status
                                                    print("Please enter a valid quantity.\n\n###### No change to cake "
                                                          "quantity ######")
                                                    input("\nPress enter to continue.")
                                                    os.system("cls")
                                                    break

                                                else:
                                                    # A loop to ask the user confirm update the order
                                                    while True:
                                                        confirm_quantity = str(input("Are you confirm to update the "
                                                                                     "cake quantity? (yes/no)\n")) \
                                                            .upper()

                                                        # Validation of the confirmation
                                                        if confirm_quantity == "YES":
                                                            # Update the cake quantity and total price to order class
                                                            # and cake class
                                                            new_total = cake.price * new_quantity
                                                            order.cake_quantity = new_quantity
                                                            order.total = new_total

                                                            # Display status
                                                            print("\n###### Cake quantity has been updated to",
                                                                  new_quantity, "######")
                                                            input("\nPress enter to continue.")
                                                            os.system("cls")
                                                            break

                                                        elif confirm_quantity == "NO":
                                                            # Display status
                                                            print("\n###### No change to cake quantity ######")
                                                            input("\nPress enter to continue.")
                                                            os.system("cls")
                                                            break

                                                        else:
                                                            print("Please enter a valid input.\n")

                                                    # Break the loop that ask user to input the new quantity of the cake
                                                    if confirm_quantity == "YES" or confirm_quantity == "NO":
                                                        break

                                            # Error handling of the cake quantity when that is not in integer
                                            except ValueError:
                                                os.system("cls")
                                                print("Please reenter in number.\n")

                                    else:
                                        os.system("cls")
                                        break

                                # Error handling of the attribute of the cake when that is not in integer
                                except ValueError:
                                    os.system("cls")
                                    print("Please reenter in number.\n")

                        else:
                            os.system("cls")
                            print("Please choose the order id that show in the list.\n")

                # Error handling of the order id when that is not in integer
                except ValueError:
                    os.system("cls")
                    print("Please enter a valid input.\n")

    # Cancel order page
    def delete(self):
        # If the BST is empty
        if bst.size() == 0:
            print("***Cancel order***\nYou have " + str(bst.size()) + " order.\nNothing show here......\n\n*press enter"
                                                                      " to go back to the menu*")
            input()
            os.system("cls")
            self.menu()

        else:
            # A loop to ask user input the order id
            while True:
                try:
                    # Display the order in the BST
                    print("***Cancel order***\nYou have " + str(bst.size()) + " order.\nHere is the order list in order"
                                                                              " id:")
                    bst.display()

                    print("\nChoose an order id to cancel the order.\n*press 0 to go back to the menu*")
                    cancel = int(input("Order id: "))

                    # Validation of the order id
                    if cancel == 0:
                        os.system("cls")
                        self.menu()
                        return

                    else:
                        # Validate the order id exist in the BST
                        if bst.search(cancel):
                            os.system("cls")

                            # Retrieve the order object from the dictionary
                            order = self.order_object[cancel]

                            # Display order details
                            print("***Order Details***\n\nOrder ID:", order.order_id, "\nCake Code:", order.cake_code,
                                  "\nCake Flavor:", order.cake_flavor, "\nCake Weight:", order.cake_weight, "gram\nCake"
                                                                                                            " Unit "
                                                                                                            "Price: RM",
                                  order.cake_price, "\nCake Quantity:", order.cake_quantity, "\nTotal: RM", order.total,
                                  "\n")

                            # A loop to ask the user confirm cancel the order
                            while True:
                                confirm_cancel = str(input("Are you sure you want to cancel this order? (yes/no)\n")) \
                                    .upper()

                                # Validation of the confirmation
                                if confirm_cancel == "YES":
                                    # Delete the cake and order object from the dictionary
                                    del self.cake_object[cancel]
                                    del self.order_object[cancel]

                                    # Remove the order node from the BST
                                    bst.remove(cancel)

                                    # Display status
                                    print("\n###### Order successfully cancelled ######")
                                    input("Press enter to continue.")
                                    os.system("cls")
                                    self.delete()
                                    return

                                elif confirm_cancel == "NO":
                                    # Display status
                                    print("\n###### Order not canceled ######")
                                    input("Press enter to continue.")
                                    os.system("cls")
                                    self.delete()
                                    return

                                else:
                                    print("\nPlease enter a valid input.")

                        else:
                            os.system("cls")
                            print("Please choose the order id that show in the list.\n")

                # Error handling of the order id when that is not in integer
                except ValueError:
                    os.system("cls")
                    print("Please enter a valid input.\n")

    def get_quantity(self):
        return self.quantity

    def get_total(self):
        return self.total


class Order:
    def __init__(self, cake, customer, program):
        self.order_id = program.order_id
        self.customer_id = customer.customer_id
        self.customer_name = customer.name
        self.customer_address = customer.address
        self.customer_contact = customer.contact
        self.cake_code = cake.cake_id
        self.cake_flavor = cake.flavor
        self.cake_weight = cake.weight
        self.cake_price = cake.price
        self.cake_quantity = program.get_quantity()
        self.total = program.get_total()


class Cake:
    def __init__(self, cake_code, flavor, weight, price):
        self.cake_id = cake_code
        self.flavor = flavor
        self.weight = weight
        self.price = price


class Customer:
    def __init__(self, customer_id, name, address, contact):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.contact = contact


class TreeNode:
    def __init__(self, order_id):
        self.item = order_id
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.__root = None
        self.__numOfItem = 0

    def size(self):
        return self.__numOfItem

    def search(self, order_id):
        if self.__root is None:
            return False

        current = self.__root

        while current is not None:
            if order_id == current.item:
                return True

            elif order_id < current.item:
                current = current.left_child

            else:
                current = current.right_child

        return False

    def insert(self, order_id):
        # A loop to check duplication of order id before insertion
        while self.search(order_id):
            order_id = random.randint(1, 10000)

        new_node = TreeNode(order_id)
        if self.__root is None:
            self.__root = new_node

        else:
            current = self.__root
            parent = None

            while current is not None:
                parent = current

                if order_id < current.item:
                    current = current.left_child

                else:
                    current = current.right_child

            if order_id < parent.item:
                parent.left_child = new_node

            else:
                parent.right_child = new_node

        # Display information
        print("\nThe order id of this order is " + str(order_id) + ".\nYou can view, edit and cancel the order by this "
                                                                   "id.")

        self.__numOfItem += 1
        return order_id

    def display(self):
        self.__in_order(self.__root)

    def __in_order(self, node):
        if node is None:
            return

        self.__in_order(node.left_child)
        print(node.item)
        self.__in_order(node.right_child)

    def remove(self, order_id):
        if self.__root is None:
            return False

        current = self.__root
        current_left_parent = None
        current_right_parent = None

        # A loop to find the order id to be deleted
        while current.item != order_id:
            if order_id < current.item and current.left_child is not None:
                current_left_parent = current
                current_right_parent = None
                current = current.left_child

            elif order_id > current.item and current.right_child is not None:
                current_left_parent = None
                current_right_parent = current
                current = current.right_child

            else:
                print("The order id is not found.")
                return False

        # When the current node is a leaf
        if current.left_child is None and current.right_child is None:
            if current == self.__root:
                self.__root = None

            else:
                if current_left_parent is not None:
                    current_left_parent.left_child = None

                if current_right_parent is not None:
                    current_right_parent.right_child = None

                del current

        # When the current node has a left child
        elif current.left_child is not None and current.right_child is None:
            if current == self.__root:
                self.__root = current.left_child

            else:
                if current_left_parent is not None:
                    current_left_parent.left_child = current.left_child

                if current_right_parent is not None:
                    current_right_parent.right_child = current.left_child

                del current

        # When the current node has a right child
        elif current.left_child is None and current.right_child is not None:
            if current == self.__root:
                self.__root = current.right_child

            else:
                if current_left_parent is not None:
                    current_left_parent.left_child = current.right_child

                if current_right_parent is not None:
                    current_right_parent.right_child = current.right_child

                del current

        # When the curr node have both left and right child
        else:
            # Move traversal node to right subtree of the current node
            traversal = current.right_child
            traversal_parent = current

            # A loop to move traversal node to the smallest node in the right subtree
            while traversal.left_child is not None:
                traversal_parent = traversal
                traversal = traversal.left_child

            # Replace the smallest node in the right subtree to the current node that to be deleted
            current.item = traversal.item

            # When does not go through the while loop
            if traversal_parent == current:
                traversal_parent.right_child = traversal.right_child
            else:
                traversal_parent.left_child = traversal.right_child

            del traversal
        self.__numOfItem -= 1
        return True


bst = BST()
Program()
