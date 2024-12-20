import time

History=[["No","Item", "Quantity", "Price($)","Day/Date/Time/Year"]]
recipt = [["No","Item", "Quantity", "Price($)"]]
cart = [["No", "ITEM", "QUANTITY", "PRICE($)"], [1, "LAPTOP", 1, 1500], [2, "DHANIA", 25, 5], [3, "PODINA", 10, 2], [4, "MOBILE", 2, 1000]]


def display_table(data):
    for row in data:
        for item in row:
            print(f"{item:<20}", end="")
        print()


def cart_button():
    while True:
        back_button = input("(a)Exit Cart (b)Back (c)View History : ")
        if back_button.lower() == "a":
            return "Exit"
        elif back_button.lower() == "b":
            return "Back"
        elif back_button == "c":
            print("                    >>>HISTORY<<<              ")
            display_table(History)
            while True:
                go_back=input("Press (b) to go back to the previous option : ")
                if go_back.lower()=="b":
                    break
                else:
                    print("Please enter a valid option!!!")

        else:
            print("Please Enter a valid option!!!")


def buy_products():
    for i in range(1, len(cart)):
        recipt.append([len(recipt),cart[i][1], cart[i][2], cart[i][3]])
        History.append([len(History),cart[i][1], cart[i][2], cart[i][3],time.ctime()])
    print("                    >>>RECEIPT<<<              ")
    display_table(recipt)

    # If the user wants to buy all the products.
    bill = sum(item[3] for item in cart[1:])
    print(f"your total bill is {bill}$")
    print("Thank you for shopping!!!")

    # Remove all the products from the cart as the user has bought all of these and now he doesn't need it.
    cart.clear()
    cart.append(["No","ITEM", "QUANTITY", "PRICE($)"])
    recipt.clear()
    recipt.append(["No","ITEM", "QUANTITY", "PRICE($)"])


def select_products_to_buy():
    # If the user wants to buy specific products.
    choice3 = input("Enter numbers of products you want to buy separated by spaces: ").strip()
    indices_to_buy = [int(index) for index in choice3.split()]

    # Check if indices are valid
    if any(index < 1 or index >= len(cart) for index in indices_to_buy):
        print("Invalid product numbers. Please enter valid numbers.")
        return "Back"

    for j in indices_to_buy:
        recipt.append([len(recipt),cart[j][1], cart[j][2], cart[j][3]])
        History.append([len(History),cart[j][1], cart[j][2], cart[j][3],time.ctime()])
    print("                    >>>RECEIPT<<<              ")
    display_table(recipt)

    bill = sum(cart[index][3] for index in indices_to_buy)
    # Now the bill has been created so we have to simply print it.
    print(f"Your Total bill is {bill}$.")
    print("Thank you for shopping!!!.")

    # We need to sort the list in descending order because we have to pop the bought items through iteration,
    # and when one item is popped, the index of the whole list is changed so we are doing it in descending order
    # because it is more reliable.
    indices_to_buy.sort(reverse=True)
    for index in indices_to_buy:
        cart.pop(index)
    for k in range(1, len(cart)):
        cart[k][0] = k
    # Now the items that have been bought are popped from the cart.
    recipt.clear()
    recipt.append(["No","ITEM", "QUANTITY", "PRICE($)"])
    return cart_button()


def remove_products():
    # When the user enters 'b', remove products from the cart.
    indices_to_remove = input("Enter numbers of products you want to remove, separated by spaces: ").strip()
    indices_to_remove = [int(index) for index in indices_to_remove.split()]

    # Check if indices are valid
    if any(index < 1 or index >= len(cart) for index in indices_to_remove):
        print("Invalid product numbers. Please enter valid numbers.")
        return "Back"

    # We will append the choices in the separate list through iteration.
    indices_to_remove.sort(reverse=True)
    for index in indices_to_remove:
        cart.pop(index)

    for k in range(1, len(cart)):
        cart[k][0] = k

    while True:
        exit_option = input("(a)Display cart (b)Exit Cart: ")
        if exit_option.lower() == "a":
            display_table(cart)
            return "Back"
        elif exit_option.lower() == "b":
            return "Exit"
        else:
            print("Please enter valid option!!!")


def thela():
    global cart
    global recipt
    global History

    display_table(cart)

    while True:
        # Display the options whether the user wants to buy products or remove products from cart.
        choice = input("(a)Buy now (b)Remove products from cart (c)Back: ")

        if choice.lower() == "a":
            # When the user enters a, display whether the user wants to buy all the products or some of them.
            while True:
                choice2 = input("(a)Buy all (b)Select products to buy: ")

                if choice2.lower() == "a":
                    buy_products()
                    cart_button_result = cart_button()
                    if cart_button_result == "Exit":
                        return
                    elif cart_button_result == "Back":
                        display_table(cart)
                        break

                elif choice2.lower() == "b":
                    cart_button_result = select_products_to_buy()
                    if cart_button_result == "Exit":
                        return
                    elif cart_button_result == "Back":
                        display_table(cart)
                        break

                else:
                    print("Please choose the right option.")

        elif choice.lower() == "b":
            cart_button_result = remove_products()
            if cart_button_result == "Exit":
                return
            elif cart_button_result == "Back":
                continue

        elif choice.lower() == "c":
            return

        else:
            print("Please enter the right option.")


thela()

