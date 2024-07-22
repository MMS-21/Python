
from simple_colors import *
from datetime import datetime

# Requirement 1: Add New Item: 
# Prompt the user to enter details such as: 
#   item name, price, and quantity for a new item. 
#   Store this information in the inventory.
def addnewitem(inventory):
    """
    Adds a new item to the inventory or updates an existing item.

    Args:
        inventory (dict): A dictionary where keys are item names and values are dictionaries with 'Price', 
        'Quantity', 
        'Quantity Sold', and 
        'Remaining Quantity'.
    """
    while True:
        # Getting the Item name
        name = input(red("Item Name: "))
        # Validating the user's input
        if name and not name.startswith(tuple('0123456789')):
            try:
                # Getting details of the item {Price, Quantity, and quantity sales}
                price = float(input("Enter price: "))
                quantity = int(input("Enter Quantity: "))
                sales = int(input("Enter Quantity Sold: "))
                # Calculating the Remaining Quantity
                remaining_quantity = quantity - sales
                # Getting back to the main menu
                break
            # Handeling input error
            except ValueError:
                print("Invalid Price or Quantity")
        # Handeling the invaled names               
        else:
            print("Invalid name")
    # Verifing the details of the item           
    if name in inventory:
        # Just formatting a phrase using ANSI Console Formatting
        print(f"""This item '{name}' is already Exists
              \x1B[3mupdating Values.../\x1B[0m""")
        # Details embedding
        inventory[name]['Quantity'] += quantity
        inventory[name]['Quantity Sold'] = sales
        inventory[name]['Remaining Quantity'] = remaining_quantity
    # Verifing the details to item dictionary
    else:
        inventory[name] = {'Quantity': quantity,
                           'Quantity Sold': sales, 
                           'Price': price,
                           'Remaining Quantity': remaining_quantity}
    # printing reassuring message and returning to main menu
    print(magenta(f"Item '{name.capitalize()}' added/updated successfully."))
    print("\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
# Requirement 2: Update Stock: 
# Allow the user to update the quantity of existing items in the inventory.
# This Function adds on the Current Stock
def stock_quantity_update(inventory):
    """
    Updates the stock quantity of items in the inventory.
    
    Parameters:
    inventory (dict): A dictionary containing item details such as price, 
    quantity sold, and 
    remaining quantity.
    
    The function performs the following actions:
    1. Displays the available items in the inventory with their price, quantity sold, revenue, and remaining quantity.
    2. Prompts the user to enter the name of the item they wish to update.
    3. If the item exists, it prompts the user to enter the quantity to be added.
       - The function ensures that the entered quantity is a valid integer.
    4. Adds the input quantity to the current quantity and remaining quantity of the specified item.
    5. Displays a confirmation message with the updated quantity.
    6. Returns to the main menu if the inventory is empty or after updating an item.
    
    Returns:
    None
    """        
    while True:
        # Making Sure that the inventory is not empty befor using this function
        if inventory:
                # Showing all items in the inventory
                print("\nAvailable items:")

                print(cyan(f"{'Item':<20}{'Price':<10}{'Quantity Sold':<15}{'Revenue':<10}{'Remaining Quantity':<10}"))
                for i in inventory.keys():
                    # Calculating the revenue
                    revenue = inventory[i]["Price"]  * inventory[i]["Quantity Sold"]
                    print(f"{i:<20}{inventory[i]['Price']:<10}{inventory[i]['Quantity Sold']:<15}{revenue:<10}{inventory[i]['Remaining Quantity']:<10}" )
                
                name = input("Enter The Name Of Item To update: ")
                if name in inventory:
                    while True:
                        try:
                            # Accepting only Integers :)
                            addition_quantity = int(input("Enter the Quantity: "))
                            break
                        except ValueError:
                            print("Invalid Quantity")
                    # Adding the inputed quantity to the current Quantity 
                    inventory[name]["Quantity"] += addition_quantity
                    inventory[name]["Remaining Quantity"] += addition_quantity
                    # Printing Assuring message
                    print(yellow(f"Current {name.capitalize()} Quantity: "),inventory[name]["Remaining Quantity"])
                    print(magenta(f"{name.capitalize()} Quantity updated Successfully"))
                    print("\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
                    break
                # Handeling none existing Items
                else:
                    print(f"Invalid Name {name.upper()},This Item does not exist")
                    continue
        else:
            print(red("\nThere is nothing in the inventory!!, Make sure to add some Items :)\n",'bold'))
            print("\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
            break
# Requirement 3: Generate Sales Report: 
# Calculate the total revenue generated from sales. 
# This should include the total revenue for each item and the overall revenue for all items sold.
def sales_report(inventory):
    """
    Displays a sales report for the inventory based on user choice.

    Args:
        inventory (dict): A dictionary where keys are item names and values are dictionaries with 'Price', 
        'Quantity Sold', and 
        'Remaining Quantity'.
    """
    while True:
        # Making Sure that the inventory is not empty befor using this function
        if inventory:
            # Print menu options with colors and formatting
            print(green(""" \nInventory Management System: \x1B[1m"Sales Reports"\x1B[0m
                        1 --> Specfic Item.
                        2 --> All Stock.
                        3 --> Back To Menu."""))
            
            # Get user prompt
            c = input(blue("\nChoose an Action from the list above: ")).strip()
            
            # 1 --> Specfic Item Report
            if c == "1":
                # Handle specific item report
                revenue = 0
                print("\nAvailable items:")
                for i in inventory.keys():
                    print(f"\n{i} " ,end="")
                    print()
                item_name = input("\nEnter Item name From the list: ").lower().strip()
                
                if item_name in inventory:
                    # Designing the Report
                    print(cyan(f"The Details of {item_name.capitalize()}"))
                    print(cyan(f"{'Item':<20}{'Price':<10}{'Quantity Sold':<15}{'Revenue':<10}{'Remaining Quantity':<10}"))
                    print(cyan("="*75))
                    
                    details = inventory[item_name]
                    # Calculating Revenue
                    revenue = details['Quantity Sold'] * details['Price']
                    # printing the values
                    print(f"{item_name:<20}{details['Price']:<10}{details['Quantity Sold']:<15}{revenue:<10}{details['Remaining Quantity']:<10}")
                    print(cyan("="*75 ), "\n")

                    # Print the current date and time
                    current_datetime = datetime.now()
                    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    print("Current date and time:", formatted_datetime)
                    
                    #Return to main menu
                    print("\n\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m\n")
                    
                else:
                        #Handling the Invalid Items
                        print("Item not found in inventory.")

            # 2 --> All Stock Report
            elif c == "2":
                # Handling Stock All Items Report
                totalsales = 0
                # Designing the Report
                print(cyan(f"{'Item':<20}{'Price':<10}{'Quantity Sold':<15}{'Revenue':<10}{'Remaining Quantity':<10}"))
                print(cyan("="*75))
                
                # Pulling the details of the items from the dictionary 
                for name, details in inventory.items():
                    # Calculating the revenue 
                    revenue = details['Quantity Sold'] * details['Price']
                    # Incrementing the revenue to get the total revenue 
                    totalsales += revenue
                    # printing out the values
                    print(f"{name:<20}{details['Price']:<10}{details['Quantity Sold']:<15}{revenue:<10}{details['Remaining Quantity']:<10}")
                print(cyan("="*75))
                print(f"{'Total Revenue':<45}{totalsales:<10}\n")

                # Print the current date and time
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                print("Current date and time:", formatted_datetime)
                #Return to main menu
                print("\n\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m\n")
                break
            # 3 --> Back To Menu
            elif c == "3":
                # Getting Back To main Menu
                print("\x1b[1;37;46mThank you, Goodbye!\x1b[0m")  
                print("\n\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
                break
        else:
            print(red("\nThere is nothing in the inventory!!, Make sure to add some Items :)\n",'bold'))
            print("\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
            break
# Requirement 4:
# Popular Items: Identify the top three most popular items based on sales quantity.
def popular_items(inventory):
    """
    Displays the top 3 most popular items in the inventory based on sales quantity.

    Args:
        inventory (dict): A dictionary where keys are item names and values are dictionaries with 'Quantity Sold'.
    """
# lambda x: x[1]['Quantity Sold'] is an anonymous function (lambda function) used as the key for sorting.
# x is each item from inventory.items(), so x is a tuple like ('item1', {'Quantity Sold': 150}).
# x[1] accesses the second element of the tuple, which is the dictionary {'Quantity Sold': 150}.
# x[1]['Quantity Sold'] accesses the value of the 'Quantity Sold' key from that dictionary, which is 150 in this case.
    # Sort the items by sales quantity in descending order
    while True:
        # Making Sure that the inventory is not empty befor using this function
        if inventory:
            print("\nTop 3 Popular Items:")
            print(yellow(f"{'Item':<20}{'Price':<10}{'Quantity Sold':<15}{'Revenue':<15}"))
            print(yellow("="*50))
            sorted_items = sorted(inventory.items(), key=lambda x: x[1]['Quantity Sold'], reverse=True)
            for i, (name, details) in enumerate(sorted_items[:3]):
                revenue = details["Price"] * details["Quantity Sold"]
                print(f"{name.capitalize():<20}{details["Price"]:<10}{details['Quantity Sold']:<15}{revenue:<15}")
            print(yellow("="*50))
            print("\n\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
            break   
        else:
            print(red("\nThere is nothing in the inventory!!, Make sure to add some Items :)\n",'bold'))
            print("\x1b[3;31;43m RETURNING TO THE MAIN MENU\x1b[0m")
            break
