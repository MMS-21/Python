from invms import *
from simple_colors import *

def main():
    # Initializing The Dictionary
    inventory = {}
    # initializing a while loop to control the 
    while True:
        print(green(""" Inventory Management System:
                    1 --> Add A New Item.
                    2 --> Update Stock.
                    3 --> Generate Sales Report.
                    4 --> Popular Items.
                    5 --> Exit."""))
        # Getting the user Selected option
        choice = input(blue("""\x1B[3mChoose An Action From The List Above (1 - 5): \x1B[0m""")).strip()
        
        if choice == "1":
            addnewitem(inventory)
        elif choice == '2':
            stock_quantity_update(inventory)
        elif choice == '3':
            sales_report(inventory)
        elif choice == '4':
            popular_items(inventory)
        # requirement 5:
        # Exit: Provide an option for the user to exit the program.
        elif choice == '5':    
            print(red("\x1B[1;30;47mExiting the program, GOODBYE!\x1B[0m"))
            break
        else:   
            print(red("Invalid Option. Please enter a number between 1 and 5."))



if  __name__ == "__main__":
    main()