import time

Username="hashir"
History=[]
recipt = [["No", "Item", "Quantity", "Price($)"]]
cart = []
products = []

d = {}


def reading_data(list_,myfile):
    with open(f"{myfile}.txt","r") as g:
        data=g.readlines()
        for i in data:
            a=i.strip()
            a=a.split(",")
            m=[int(k) if k.isdigit() else float(k) if "." in k else k for k in a]
            list_.append(m)


# Function to write data from a list to a file
def writing_data(list_,myfile):
    with open(f"{myfile}.txt","w") as f:
        for i in range(len(list_)):
            for j in range(len(list_[0])):
                if list_[i][j]==list_[i][len(list_[i])-1]:
                    f.write(str(list_[i][j])+"\n")
                else:
                    f.write(str(list_[i][j])+",")





    

def reading_dictionary(dictionary,myfile):
    with open(f"{myfile}.txt", "r") as f:
        lines=f.readlines()
        for line in lines:
            line = line.strip()
            key, value = line.split(' ', 1)
            dictionary[int(key)] = value




def writing_dictionary(dictionary,myfile):
    with open(f"{myfile}.txt", "w") as g:
        for i in dictionary.items():
            for j in i:
                if j==i[0]:
                    g.write(str(j)+" ")
                else:
                    g.write(j+"\n")




def reading_dictionary(dictionary,myfile):
    with open(f"{myfile}.txt", "r") as f:
        lines=f.readlines()
        for line in lines:
            line = line.strip()
            key, value = line.split(' ', 1)
            dictionary[int(key)] = value




            
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




def display_table(data):
    for row in data:
        for item in row:
            print(f"{item:<20}", end="")
        print()


def checkout_or_back():
    while True:
        exit_choice = input("(a)Checkout (b)Back to menu (c)View shopping History : ").lower()
        if exit_choice == "a":
            print("            >>>CHECKOUT<<<          ")
            print("Thank you for visiting us!!!")
            return "checkout"
        elif exit_choice == "b":
            return "back"
        elif exit_choice == "c":
            print("                    >>>HISTORY<<<              ")
            display_table(History)
            while True:
                go_back=input("Press (b) to go back to the previous option : ")
                if go_back.lower()=="b":
                    break
                else:
                    print("Please enter a valid option!!!")

def checkout_or_back_2():
    while True:
        exit_choice = input("(a)Checkout (b)Back  : ").lower()
        if exit_choice == "a":
            print("            >>>CHECKOUT<<<          ")
            print("Thank you for visiting us!!!")
            return "checkout"
        elif exit_choice == "b":
            return "back"
        else:
            print("Please enter the right option.")



def product_detail(choice):
    print(d.get(choice))
    while True:
        option = input("(a)Buy Now  (b)Add To cart  (c)Back: ").lower()
        if option == "a":
            qty = get_valid_input("Enter the quantity: ")
            bill = qty * products[choice][3]
            print(f"Your bill is {bill}$")
            while True:
                confirm_choice = input("Do you want to confirm[y/n]: ").lower()
                if confirm_choice == "y":
                    products[choice][2] -= qty
                    if products[choice][2] >= 0:
                        recipt.append([len(recipt), products[choice][1], qty, bill])
                        History.append([len(History), products[choice][1], qty, bill,time.ctime()])
                        print("                    >>>RECEIPT<<<              ")
                        display_table(recipt)
                        print("Thank You For Shopping with us!!!!!!")
                        recipt.clear()
                        recipt.append(["No", "ITEM", "QUANTITY", "PRICE($)"])
                        return checkout_or_back()
                    else:
                        print("Insufficient Quantity")
                        products[choice][2] += qty
                        print(d.get(choice))
                        break
                elif confirm_choice == "n":
                    break
                else:
                    print("Please enter a valid option.")
        elif option == 'b':
            qty = get_valid_input("How many units: ")
            products[choice][2] -= qty
            if products[choice][2] >= 0:
                bill = qty * products[choice][3]
                cart.append([len(cart), products[choice][1], qty, bill])
                print("Your product has been added to cart!!!")
                while True:
                    cart_option = input("(a)View Cart (b)Back (c)Checkout from the app : ").lower()
                    if cart_option == "a":
                        thela()
                        Exit_cart=checkout_or_back_2()
                        if Exit_cart=="back":
                            return "back"
                        else:
                            return "checkout"
                    elif cart_option == "c":
                        print("            >>>CHECKOUT<<<          ")
                        print("Thank you for visiting us!!!")
                        return "checkout"
                    elif cart_option == "b":
                        print(d.get(choice))
                        break
                    else:
                        print("Please enter a valid input.")
            else:
                print("Insufficient Stock!!!")
                continue
        elif option == "c":
            return "back"  # Signal to display_menu that the user wants to go back
        else:
            print("Please enter a valid input.")


def display_menu():
    reading_data(products,"data")
    reading_dictionary(d,"dictionary")
    reading_data(cart,f"Database/{Username}_cart")
    reading_data(History,f"Database/{Username}_history")
    while True:
        display_table(products)
        choice = get_valid_input("Enter the number to view the detail of the product (0 to exit): ")
        if choice == 0:
            writing_data(products,"data")
            writing_data(cart,f"Database/{Username}_cart")
            writing_data(History,f"Database/{Username}_history")
            print("Thank you for shopping with us!")
            menu_exit=checkout_or_back_2()
            if menu_exit=="checkout":
                return "Exit"
            else:
                return "back"
        elif 1 <= choice < len(products):
            while True:
                result = product_detail(choice)
                if result == "checkout":
                    writing_data(products,"data")
                    writing_data(cart,f"Database/{Username}_cart")
                    writing_data(History,f"Database/{Username}_history")
                    return "Exit"
                elif result == "back":
                    break  # Go back to the product details
                else:
                    print("Invalid return value from product_detail.")
        else:
            print("Please enter a valid option.")


def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid number.")

display_menu()



