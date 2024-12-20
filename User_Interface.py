# user_interface.py
from MENU_FUNCTION import *

def main():
    while True:
        print("MENU OPTIONS:")
        print("(1) VIEW CART")
        print("(2) VIEW PRODUCT LIST")
        print("(3) VIEW HISTORY")
        print("(4) LOGOUT")

        choice = get_valid_input("Enter your choice (1-4): ")

        if choice == 1:
            # Read user's cart and history
            reading_data(cart, f"Database/{Username}_cart")
            reading_data(History, f"Database/{Username}_history")
            
            thela()
            
            # Write user's cart and history back to files
            writing_data(cart, f"Database/{Username}_cart")
            writing_data(History, f"Database/{Username}_history")
            
            exit_cart = checkout_or_back_2()
            if exit_cart == "back":
                # Clear lists after returning back
                History.clear()
                cart.clear()
            elif exit_cart == "checkout":
                return "Exit"
        elif choice == 2:
            display_menu_result = display_menu()
            if display_menu_result == "Exit":
                return "Exit"
            elif display_menu_result == "back":
                # Clear lists after returning back
                History.clear()
                products.clear()
                cart.clear()
        elif choice == 3:
            reading_data(History, f"Database/{Username}_history")
            print("                    >>>HISTORY<<<              ")
            display_table(History)
            while True:
                go_back = input("Press (b) to go back to the previous option: ")
                if go_back.lower() == "b":
                    break
                else:
                    print("Please enter a valid option!!!")
            # Clear lists after returning back
            History.clear()
            cart.clear()
        elif choice == 4:
            # Write data to files before logging out
            print("Thank you for shopping with us!")
            return "Exit"
        else:
            print("Please enter a valid option (1-4).")

# if __name__ == "__main__":
#     main()
main()
