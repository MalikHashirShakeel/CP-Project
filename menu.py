recipt = [["Item", "Quantity", "Price($)"]]
cart = [["Item", "Quantity", "Price($)"]]
products = [["No", "Product", "stock", "Price($)"], [1, "Product", 50, 100], [2, "Product", 50, 100],
            [3, "Product", 50, 100], [4, "Product", 50, 100], [5, "Product", 50, 100], [6, "Product", 50, 100],
            [7, "Product", 50, 100], [8, "Product", 50, 100], [9, "Product", 50, 100], [10, "Product", 50, 100]]
d = {1: "........\n............\n...........\n..........", 2: "........\n............\n...........\n..........",
     3: "........\n............\n...........\n..........", 4: "........\n............\n...........\n..........",
     5: "........\n............\n...........\n..........", 6: "........\n............\n...........\n..........",
     7: "........\n............\n...........\n..........", 8: "........\n............\n...........\n..........",
     9: "........\n............\n...........\n..........", 10: "........\n............\n...........\n.........."}



def display_table(data):
    for row in data:
        for item in row:
            print(f"{item:<20}", end="")
        print()
















def product_detail(choice):
    print(d.get(choice))
    while True:
        option = input("(a)Buy Now  (b)Add To cart  (c)Back: ")
        if option == "a" or option == "A":
            qty = int(input("Enter the quantity: "))
            bill = qty * products[choice][3]
            print(f"Your bill is {bill}$")
            while True:
                option2 = input("Do you want to confirm[y/n]: ")
                if option2 == "y" or option2 == "Y":
                    products[choice][2] -= qty
                    if products[choice][2]>=0:
                        
                        recipt.append([products[choice][1], qty, bill])
                        print("                    >>>CHECKOUT<<<              ")
                        for i in range(len(recipt)):
                            for j in range(len(recipt[0])):
                                print(recipt[i][j], end="                   ")
                            print()
                        print("Thank You For Shopping with us!!!!!!")
                        return
                    else:
                        print('Insufficient Quantity')
                        products[choice][2]-=qty
                        break

                elif option2 == "n" or option2 == "N":
                    break
                else:
                    print("please enter a valid option.")
                    continue
        elif option == 'b' or option == "B":
            qty = int(input("How many units: "))
            products[choice][2] -= qty
            if products[choice][2]>=0:
                bill = qty * products[choice][3]
                cart.append([products[choice][1], qty, bill])
                print("Your product has been added to cart!!!")
                while True:
                    option3 = input("(a)View Cart (b)Back (c)Checkout: ")
                    if option3 == "a" or option3 == "A":
                        print("cart option is under making.")
                    elif option3 == "c" or option3 == "C":
                        print("            >>>CHECKOUT<<<          ")
                        print("Thank you for shopping with us!!!")
                        return
                    elif option3 == "b" or option3 == "B":
                        break
                    else:
                        print("Please enter a valid input.")
            else:
                print("Insufficient Stock!!!")
                continue
        elif option == "c" or option == "C":
            break
        else:
            print("Please enter a valid input.")








def display_menu():
    while True:
        display_table(products)
        choice = int(input("Enter the number to view the detail of product (0 to exit): "))
        if choice == 0:
            print("Thank you for shopping with us!")
            return
        elif 1 <= choice <= 10:
            product_detail(choice)
            break
        else:
            print("Please enter a valid option.")



display_menu()