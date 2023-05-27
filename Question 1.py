import pyfiglet
import os
import re
import random


class Program:
    def __init__(self):
        self.order_id = int
        self.quantity = int
        self.total = 0
        self.order_object = {}
        self.cake_object = {}
        print(pyfiglet.figlet_format("WELCOME", font="cursive", justify="center", width=125))
        while True:
            try:
                customer_id = int(input("Enter your member id: "))
                if customer_id > 0:
                    break
                else:
                    print("Please reenter a valid member id.\n")
            except ValueError:
                print("Please reenter a valid customer id.\n")
        while True:
            customer_name = str(input("Enter your name: "))
            if not re.match("^[a-zA-Z\s'/-]+$", customer_name):
                print("Please reenter a valid name.\n")
            else:
                break
        while True:
            location = str(input("Enter the address of the location: "))
            if not re.match(r"^[a-zA-Z0-9\s,.\'-]{3,}$", location):
                print("Please reenter a valid location.\n")
            else:
                break
        while True:
            try:
                phone = int(input("Enter your phone number: "))
                if phone > 0:
                    if 9 <= len(str(phone)) <= 10:
                        break
                    else:
                        print("Please reenter a valid phone number.\n")
                else:
                    print("Please reenter a valid phone number.\n")
            except ValueError:
                print("Please reenter a valid phone number.\n")
        print("\n##################################################\nCustomer id: " + str(customer_id) + "\nName: " +
              customer_name + "\nAddress: " + location + "\nPhone number: 0" + str(phone) + "\n########################"
                                                                                            "##########################"
                                                                                            "\n")
        while True:
            print("Please confirm the infomation you provided is correct to order your cake.")
            confirm_info = str(input("Are you confirm? (yes/no)\n")).upper()
            if confirm_info == "YES":
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

    def menu(self):
        print(pyfiglet.figlet_format("WELCOME", font="cursive", justify="center", width=125))
        print("1. Add new cake order".center(120))
        print("2. View cake order list".center(122))
        print("3. Edit cake order".center(115))
        print("4. Cancel cake order".center(117))
        print("*press other number to exit*".center(122))
        while True:
            try:
                menu = int(input("\n\t\t\t\t\t   Enter a number to choose from menu: "))
                break
            except ValueError:
                print("Please reenter in a valid number.".center(125))
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

    def add(self):
        print("***Add new cake order***")
        while True:
            try:
                print("1. Strawberry\n2. Chocolate\n3. Matcha\n*press other number to go back to the menu*\n")
                flavors = int(input("Enter a number to select the flavor of cake: "))
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
                    while True:
                        confirm_infomation = str(input("The order is not save. Are you sure want to exit? (yes/no)\n"))\
                            .upper()
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
            except ValueError:
                os.system('cls')
                print("Please reenter in number.\n")
        print("\n1. 250 -- RM30\n2. 500 -- RM60\n3. 750 -- RM120\n4. 1000 -- RM180\n*press other number to go back to "
              "the menu*\n")
        while True:
            try:
                size = int(input("Enter a number to select the weight of the cake(gram): "))
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
                    while True:
                        confirm_massage = str(input("The order is not save. Are you sure want to exit? (yes/no)\n")).\
                            upper()
                        if confirm_massage == "YES":
                            os.system("cls")
                            self.menu()
                            return
                        elif confirm_massage == "NO":
                            print("")
                            break
                        else:
                            print("Please enter a valid input.\n")
            except ValueError:
                print("Please reenter in number.\n")
        while True:
            try:
                print("\n*press 0 to go back to the menu*")
                quantity = int(input("Enter the quantity of the cake: "))
                if quantity == 0:
                    while True:
                        confirm_massage = str(input("The order is not save. Are you sure want to exit? (yes/no)\n")).\
                            upper()
                        if confirm_massage == "YES":
                            os.system("cls")
                            self.menu()
                            return
                        elif confirm_massage == "NO":
                            print("")
                            break
                        else:
                            print("Please enter a valid input.\n")
                else:
                    break
            except ValueError:
                print("Please enter a valid input.\n")
        self.total = price * quantity
        self.quantity = quantity
        print("\n##################################################\nFlavor: " + flavor + "\nWeight: " + str(weight) +
              " gram\nUnit Price: RM " + str(price) + "\nQuantity: " + str(quantity) + "\nTotal: RM " + str(self.total)
              + "\n##################################################")
        while True:
            print("\nPlease confirm your cake order.")
            confirm_order = str(input("Are you confirm? (yes/no)\n")).upper()
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
                self.order_id = random.randint(1, 10000)
                self.order_id = bst.insert(self.order_id)
                self.cake_object[self.order_id] = Cake(cake_code, flavor, weight, price)
                self.order_object[self.order_id] = Order(self.cake_object[self.order_id], self.cus, self)
                print("Order added.\nThank you for your support!!!\n")
                while True:
                    again = str(input("\nDo you want to order again? (yes/no)\n")).upper()
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
                while True:
                    again = str(input("\nDo you want to order again? (yes/no)\n")).upper()
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

    def view(self):
        if bst.size() == 0:
            print("***View order details***\nYou have " + str(bst.size()) + " order.\nNothing show here......\n\n*press"
                                                                            " enter to go back to the menu*")
            input()
            os.system("cls")
            self.menu()
        else:
            while True:
                try:
                    print("***View order details***\nYou have " + str(bst.size()) + " order.\nHere is the order list in"
                                                                                    " order id:")
                    bst.display()
                    print("\nChoose an order id that display above to view that order details.\n*press 0 to go back to"
                          " the menu*")
                    detail = int(input("Order id: "))
                    if detail == 0:
                        os.system("cls")
                        self.menu()
                        return
                    else:
                        if bst.search(detail):
                            os.system("cls")
                            order = self.order_object[detail]
                            print("***Order Details***\n\nOrder ID:", order.order_id, "\nCustomer ID:",
                                  order.customer_id, "\nCustomer Name:", order.customer_name, "\nCustomer Address:",
                                  order.customer_address, "\nCustomer Contact:", order.customer_contact, "\nCake Code:",
                                  order.cake_code, "\nCake Flavor:", order.cake_flavor, "\nCake Weight:",
                                  order.cake_weight, "gram\nCake Unit Price: RM", order.cake_price, "\nCake Quantity:",
                                  order.cake_quantity, "\nTotal: RM", order.total)
                            while True:
                                view = str(input("\nDo you want to view your order again? (yes/no)\n")).upper()
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
                except ValueError:
                    os.system("cls")
                    print("Please enter a valid input.\n")

    def edit(self):
        if bst.size() == 0:
            print("***Edit cake order***\nYou have " + str(bst.size()) + " order.\nNothing show here......\n\n*press "
                                                                         "enter to go back to the menu*")
            input()
            os.system("cls")
            self.menu()
        else:
            while True:
                print("***Edit cake order***\nYou have " + str(bst.size()) + " order.\nHere is the order list in order "
                                                                             "id:")
                bst.display()
                print("\nChoose an order id that display above to edit that order details.\n*press 0 to go back to the "
                      "menu*")
                try:
                    details = int(input("Order id: "))
                    if details == 0:
                        os.system("cls")
                        self.menu()
                        return
                    else:
                        if bst.search(details):
                            os.system("cls")
                            order = self.order_object[details]
                            cake = self.cake_object[details]
                            confirm_infomation = str
                            while True:
                                print("***Order Details***\n\nOrder ID:", order.order_id, "\nCake Code:",
                                      order.cake_code, "\n1. Cake Flavor:", order.cake_flavor, "\n2. Cake Weight:",
                                      order.cake_weight, "gram\n3. Cake Quantity:", order.cake_quantity,
                                      "\nCake Unit Price: RM", cake.price, "\nTotal: RM", order.total,
                                      "\n\n*press other number to go back to the order list*")
                                try:
                                    attribute = int(input("Enter a number to modify the selected attribute: "))
                                    if attribute == 1:
                                        os.system("cls")
                                        new_flavor = int
                                        while True:
                                            try:
                                                print("***Modify Cake Flavor***\n\n1. Strawberry\n2. Chocolate\n3. "
                                                      "Matcha\n*press other number to go back to the order details*\n")
                                                new_flavour = int(input("Enter a number to select the flavor of cake: ")
                                                                  )
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
                                                    while True:
                                                        confirm_infomation = str(input("The order is notting update. "
                                                                                       "Are you sure want to exit? "
                                                                                       "(yes/no)\n")).upper()
                                                        if confirm_infomation == "YES":
                                                            break
                                                        elif confirm_infomation == "NO":
                                                            os.system("cls")
                                                            break
                                                        else:
                                                            print("Please enter a valid input.\n")
                                                    if confirm_infomation == "YES":
                                                        break
                                            except ValueError:
                                                os.system("cls")
                                                print("Please reenter in number.\n")
                                        while True:
                                            if confirm_infomation == "YES":
                                                confirm_infomation = None
                                                os.system("cls")
                                                break
                                            confirm_flavor = str(input("Are you confirm to update the cake flavor? "
                                                                       "(yes/no)\n")).upper()
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
                                                order.cake_code = new_cake_code
                                                order.cake_flavor = new_flavor
                                                cake.cake_id = new_cake_code
                                                cake.flavor = new_flavor
                                                print("\n###### Cake flavor has been updated to", new_flavor, "######")
                                                input("\nPress enter to continue.")
                                                os.system("cls")
                                                break
                                            elif confirm_flavor == "NO":
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
                                        while True:
                                            try:
                                                print("***Modify Cake Weight***\n\n1. 250 -- RM30\n2. 500 -- RM60\n3. "
                                                      "750 -- RM120\n4. 1000 -- RM180\n*press other number to go back "
                                                      "to the order details*\n")
                                                new_weigh = int(input("Enter a number to select the weight of cake"
                                                                      "(gram): "))
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
                                                    while True:
                                                        confirm_infomation = str(input("The order is notting update. "
                                                                                       "Are you sure want to exit? "
                                                                                       "(yes/no)\n")).upper()
                                                        if confirm_infomation == "YES":
                                                            break
                                                        elif confirm_infomation == "NO":
                                                            os.system("cls")
                                                            break
                                                        else:
                                                            print("Please enter a valid input.\n")
                                                    if confirm_infomation == "YES":
                                                        break
                                            except ValueError:
                                                os.system("cls")
                                                print("Please reenter in number.\n")
                                        while True:
                                            if confirm_infomation == "YES":
                                                confirm_infomation = None
                                                os.system("cls")
                                                break
                                            confirm_weight = str(input("Are you confirm to update the cake weight? "
                                                                       "(yes/no)\n")).upper()
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
                                                new_total = new_price * order.cake_quantity
                                                order.cake_code = new_cake_code
                                                order.cake_weight = new_weight
                                                order.total = new_total
                                                cake.cake_id = new_cake_code
                                                cake.weight = new_weight
                                                cake.price = new_price
                                                print("\n###### Cake weight has been updated to", new_weight, "gram "
                                                                                                              "######")
                                                input("\nPress enter to continue.")
                                                os.system("cls")
                                                break
                                            elif confirm_weight == "NO":
                                                print("\n##### No change to cake weight ######")
                                                input("\nPress enter to continue.")
                                                os.system("cls")
                                                break
                                            else:
                                                print("Please enter a valid input.\n")
                                    elif attribute == 3:
                                        os.system("cls")
                                        while True:
                                            try:
                                                print("***Modify Cake Quantity***\n\n*press 0 to go back to the order "
                                                      "details*\n")
                                                new_quantity = int(input("Enter the quantity of the cake: "))
                                                if new_quantity == 0:
                                                    while True:
                                                        confirm_infomation = str(input("The order is notting update. "
                                                                                       "Are you sure want to exit? "
                                                                                       "(yes/no)\n")).upper()
                                                        if confirm_infomation == "YES":
                                                            break
                                                        elif confirm_infomation == "NO":
                                                            os.system("cls")
                                                            break
                                                        else:
                                                            print("Please enter a valid input.\n")
                                                    if confirm_infomation == "YES":
                                                        os.system("cls")
                                                        break
                                                else:
                                                    while True:
                                                        confirm_quantity = str(input("Are you confirm to update the "
                                                                                     "cake quantity? (yes/no)\n"))\
                                                            .upper()
                                                        if confirm_quantity == "YES":
                                                            new_total = cake.price * new_quantity
                                                            order.cake_quantity = new_quantity
                                                            order.total = new_total
                                                            print("\n###### Cake quantity has been updated to",
                                                                  new_quantity, "######")
                                                            input("\nPress enter to continue.")
                                                            os.system("cls")
                                                            break
                                                        elif confirm_quantity == "NO":
                                                            print("\n###### No change to cake quantity ######")
                                                            input("\nPress enter to continue.")
                                                            os.system("cls")
                                                            break
                                                        else:
                                                            print("Please enter a valid input.\n")
                                                    if confirm_quantity == "YES" or confirm_quantity == "NO":
                                                        break
                                            except ValueError:
                                                os.system("cls")
                                                print("Please reenter in number.\n")
                                    else:
                                        os.system("cls")
                                        break
                                except ValueError:
                                    os.system("cls")
                                    print("Please reenter in number.\n")
                        else:
                            os.system("cls")
                            print("Please choose the order id that show in the list.\n")
                except ValueError:
                    os.system("cls")
                    print("Please enter a valid input.\n")

    def delete(self):
        if bst.size() == 0:
            print("***Cancel order***\nYou have " + str(bst.size()) + " order.\nNothing show here......\n\n*press enter"
                                                                      " to go back to the menu*")
            input()
            os.system("cls")
            self.menu()
        else:
            while True:
                try:
                    print("***Cancel order***\nYou have " + str(bst.size()) + " order.\nHere is the order list in order"
                                                                              " id:")
                    bst.display()
                    print("\nChoose an order id to cancel the order.\n*press 0 to go back to the menu*")
                    cancel = int(input("Order id: "))
                    if cancel == 0:
                        os.system("cls")
                        self.menu()
                        return
                    else:
                        if bst.search(cancel):
                            os.system("cls")
                            order = self.order_object[cancel]
                            print("***Order Details***\n\nOrder ID:", order.order_id, "\nCake Code:", order.cake_code,
                                  "\nCake Flavor:", order.cake_flavor, "\nCake Weight:", order.cake_weight, "gram\nCake"
                                                                                                            " Unit "
                                                                                                            "Price: RM",
                                  order.cake_price, "\nCake Quantity:", order.cake_quantity, "\nTotal: RM", order.total,
                                  "\n")
                            while True:
                                confirm_cancel = str(input("Are you sure you want to cancel this order? (yes/no)\n"))\
                                    .upper()
                                if confirm_cancel == "YES":
                                    del self.cake_object[cancel]
                                    del self.order_object[cancel]
                                    bst.remove(cancel)
                                    print("\n###### Order successfully cancelled ######")
                                    input("Press enter to continue.")
                                    os.system("cls")
                                    break
                                elif confirm_cancel == "NO":
                                    print("\n###### Order not canceled ######")
                                    input("Press enter to continue.")
                                    os.system("cls")
                                    break
                                else:
                                    print("\nPlease enter a valid input.")
                        else:
                            os.system("cls")
                            print("Please choose the order id that show in the list.\n")
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
        curr = self.__root
        while curr is not None:
            if order_id == curr.item:
                return True
            elif order_id < curr.item:
                curr = curr.left_child
            else:
                curr = curr.right_child
        return False

    def insert(self, order_id):
        while self.search(order_id):
            order_id = random.randint(1, 10000)
        new_node = TreeNode(order_id)
        if self.__root is None:
            self.__root = new_node
        else:
            curr = self.__root
            par = None
            while curr is not None:
                par = curr
                if order_id < curr.item:
                    curr = curr.left_child
                elif order_id > curr.item:
                    curr = curr.right_child
                else:
                    return False
            if order_id < par.item:
                par.left_child = new_node
            else:
                par.right_child = new_node
        print("\nThe order id of this order is " + str(order_id) + ".\nYou can view, edit and cancel the order by this "
                                                                   "id.")
        self.__numOfItem += 1
        return order_id

    def display(self):
        self.__in_order(self.__root)

    def __in_order(self, order_id):
        if order_id is None:
            return
        self.__in_order(order_id.left_child)
        print(order_id.item)
        self.__in_order(order_id.right_child)

    def remove(self, order_id):
        if self.__root is None:
            return False
        curr = self.__root
        parent_lp = None
        parent_rp = None
        while curr.item != order_id:
            if order_id < curr.item and curr.left_child is not None:
                parent_lp = curr
                parent_rp = None
                curr = curr.left_child
            elif order_id > curr.item and curr.right_child is not None:
                parent_lp = None
                parent_rp = curr
                curr = curr.right_child
            else:
                print("The order id is not found.")
                return
        if curr.left_child is None and curr.right_child is None:
            if curr == self.__root:
                self.__root = None
            else:
                if parent_lp is not None:
                    parent_lp.left_child = None
                if parent_rp is not None:
                    parent_rp.right_child = None
                del curr
        elif curr.left_child is not None and curr.right_child is None:
            if curr == self.__root:
                self.__root = curr.left_child
            else:
                if parent_lp is not None:
                    parent_lp.left_child = None
                if parent_rp is not None:
                    parent_rp.right_child = None
                del curr
        elif curr.left_child is None and curr.right_child is not None:
            if curr == self.__root:
                self.__root = curr.right_child
            else:
                if parent_lp is not None:
                    parent_lp.left_child = None
                if parent_rp is not None:
                    parent_rp.right_child = None
                del curr
        else:
            delete_node = curr
            curr = curr.right_child
            par = delete_node
            while curr.left_child is not None:
                par = curr
                curr = curr.left_child
            delete_node.item = curr.item
            if par == delete_node:
                par.rightChild = curr.right_child
            else:
                par.leftChild = curr.right_child
            del curr
        self.__numOfItem -= 1
        return True


bst = BST()
Program()
input()
 