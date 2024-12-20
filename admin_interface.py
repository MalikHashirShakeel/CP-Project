from ADMIN_MENU_FUNCTION import *

def admin_interface():
    while True:
        print("ADMIN MENU:")
        print("(1) CHANGE MENU")
        print("(2) VIEW ACCOUNTS")
        print("(3) LOGOUT")

        admin_choice = get_valid_input("Enter your choice (1-3): ")

        if admin_choice == 1:
            # Call the function for changing the menu
            display_admin_menu_result = display_admin_menu()
            if display_admin_menu_result == "checkout":
                print("Admin checkout successful.")
                return
            elif display_admin_menu_result == "back":
                continue
        elif admin_choice == 2:
            # Call the function for viewing accounts
            print("Functionality under development: VIEW ACCOUNTS")
            # Add your code here for viewing accounts
        elif admin_choice == 3:
            # Admin logout
            print("Admin logout successful.")
            return
        else:
            print('Please enter a valid input!!!')

admin_interface()
