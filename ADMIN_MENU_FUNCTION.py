

        

            
def reading_dictionary(dictionary,myfile):
    with open(f"{myfile}.txt", "r") as f:
        lines=f.readlines()
        for line in lines:
            line = line.strip()
            key, value = line.split(' ', 1)
            dictionary[int(key)] = value
# Initialize an empty list to store product data
products = []

# Dictionary to store product descriptions
d =  {}

# Function to display a table of data
def display_table(data):
    for row in data:
        for item in row:
            print(f"{item:<20}", end="")
        print()

# Function to read data from a file into a list
def reading_data(list_, myfile):
    with open(f"{myfile}.txt", "r") as file:
        data = file.readlines()
        for line in data:
            values = line.strip().split(",")
            converted_values = [int(k) if k.isdigit() else float(k) if "." in k else k for k in values]
            list_.append(converted_values)

# Function to write data from a list to a file
def writing_data(list_,myfile):
    with open(f"{myfile}.txt","w") as f:
        for i in range(len(list_)):
            for j in range(len(list_[0])):
                if list_[i][j]==list_[i][len(list_[i])-1]:
                    f.write(str(list_[i][j])+"\n")
                else:
                    f.write(str(list_[i][j])+",")

def writing_dictionary(dictionary,myfile):
    with open(f"{myfile}.txt", "w") as g:
        for i in dictionary.items():
            for j in i:
                if j==i[0]:
                    g.write(str(j)+" ")
                else:
                    g.write(j+"\n")


# Function to get valid integer input from the user
def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid number.")

# Function to handle checkout or back option
def checkout_or_back_2():
    while True:
        exit_choice = input("(a)Checkout (b)Back to menu : ").lower()
        if exit_choice == "a":
            print("            >>>CHECKOUT<<<          ")
            print("Thank you for visiting us!!!")
            return "checkout"
        elif exit_choice == "b":
            return "back"
        else:
            print("Please enter the right option.")

# Function to display the admin menu
def display_admin_menu():
    # Read data from file into the products list
    reading_data(products, "data")
    reading_dictionary(d,"dictionary")

    # Display the current product table
    display_table(products)

    while True:
        # Admin menu options
        admin_choice = input("(a)Remove any product (b)Add any Product (c)Edit Stock (d)Edit any Product's detail (e)Edit product price (f)Back : ")

        if admin_choice.lower() == "a":
            # Remove product option
                while True:
                    admin_choice2 = get_valid_input("Enter the number of product you want to Remove: ")
                    if 0 < admin_choice2 < len(products):
                        # Remove the product from both the list and the dictionary
                        removed_product_number = products.pop(admin_choice2)[0]
                        d.pop(removed_product_number)

                        # Update remaining dictionary keys sequentially
                        for key in range(removed_product_number + 1, len(d) + 2):
                            d[key - 1] = d.pop(key)

                        # Update product numbers
                        for k in range(1, len(products)):
                            products[k][0] = k

                        print("Your product has been removed!!!")
                        writing_data(products,"data")
                        writing_dictionary(d,"dictionary")

                        # Check if user wants to checkout or go back
                        back = checkout_or_back_2()
                        if back == "checkout":
                            return "checkout"
                        else:
                            display_table(products)
                            break
                    else:
                        print("Please enter a valid product number!!!")


        elif admin_choice.lower() == "b":
            # Add product option
            while True:
                add1 = input("Enter the name of product: ")
                if "A" <= add1 <= "Z" or "a" <= add1 <= "z":
                    break
                else:
                    print("Please Enter a valid name!!!")

            add2 = get_valid_input("Enter the stock of product.")
            add3 = get_valid_input("Enter the price of product.")

            while True:
                add4 = input("Enter the details of product: ")
                if "A" <= add4 <= "Z" or "a" <= add4 <= "z":
                    break
                else:
                    print("Please Enter a valid input!!!")

            # Add the new product to the list and update the description dictionary
            products.append([len(products), add1, add2, add3])
            length = len(d) + 1
            d[length] = add4
            

            print("Your product has been added to the product list!!!")
            writing_data(products,"data")
            writing_dictionary(d,"dictionary")

            # Check if user wants to checkout or go back
            back2 = checkout_or_back_2()
            if back2 == "checkout":
                return "checkout"
            else:
                display_table(products)
                continue

        elif admin_choice.lower() == "c":
            # Edit stock option
            while True:
                edit_stock = get_valid_input("Enter the number of product to edit the product's stock: ")
                if 1<edit_stock<len(products):
                    enter_stock = get_valid_input("Enter the stock:")
                    products[edit_stock][2] = enter_stock
                    print("Your stock has been updated!!!")
                    writing_data(products,"data")
                    break
                else:
                    print("Please Enter valid product number!!!")

            # Check if user wants to checkout or go back
            back3 = checkout_or_back_2()
            if back3 == "checkout":
                return "checkout"
            else:
                display_table(products)
                continue

        elif admin_choice.lower() == "d":
            # Edit product detail option
            while True:
                edit_detail = get_valid_input("Enter the number of product to edit the product's detail: ")
                if 1<edit_detail<len(products):
                    while True:
                        add5 = input("Enter the details of product: ")
                        if "A" <= add5 <= "Z" or "a" <= add5 <= "z":
                            break
                        else:
                            print("Please Enter a valid input!!!")
                    d[edit_detail] = add5
                    print("The details of the product have been updated!!!")
                    writing_dictionary(d,"dictionary")
                    break
                else:
                    print("Please Enter valid product number!!!")

            # Check if user wants to checkout or go back
            back4 = checkout_or_back_2()
            if back4 == "checkout":
                return "checkout"
            else:
                display_table(products)
                continue

        elif admin_choice.lower()=="e":
            while True:
                edit_price = get_valid_input("Enter the number of product to edit the product's price: ")
                if 1<edit_price<len(products):
                    enter_price = get_valid_input("Enter the price:")
                    products[edit_price][3] = enter_price
                    print("Your price has been updated!!!")
                    writing_data(products,"data")
                    break
                else:
                    print("Please enter valid product number!!!")

            # Check if user wants to checkout or go back
            back5 = checkout_or_back_2()
            if back5 == "checkout":
                return "checkout"
            else:
                display_table(products)
                continue

        elif admin_choice.lower() == "f":
            # Go back option
            return "back"

        else:
            print("Please enter a valid option.")

# Call the display_admin_menu function


# Print the updated product description dictionary

