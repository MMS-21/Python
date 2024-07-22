************************************
# Inventory Management System

## Project Overview
This Python project is an Inventory Management System that allows users to add new items, update existing items, view inventory, and track sales. The system provides a simple and efficient way to manage inventory data.

## Features
1. **Add New Item**: Allows the user to enter details such as item name, price, and quantity for a new item and store this information in the inventory.
2. **Update Item**: Enables updating the details of existing items in the inventory.
3. **View Inventory**: Displays the current inventory with item details including name, price, quantity, and quantity sold.
4. **Track Sales**: Records sales transactions and updates the inventory accordingly.

## Requirements
- Python 3.x
- `simple_colors` library (for colored terminal output):
    
    **Colorful output in terminal.**

    - Installation
    ``` bash
    pip install simple-colors
    ```
    - Usage
    ``` python
    from simple_colors import *
    print(green('hello'))

    print(green('hello', 'bold'))

    print(green('hello', ['bold', 'underlined']))
    ```
    - Inlucded colors
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan

    - Included styles:
        - bold
        - bright
        - dim
        - italic
        - underlined
        - blink
        - reverse



---------------------------------------
## program in pieces:

    ```
        Choice 1: Add New Item
            --> Prompt for Item:
                    Name, 
                    Price, 
                    and Quantity.
            --> Add or Update Item in Inventory
            --> Return to Menu

        Choice 2: Update Stock
            --> Prompt for Item:
                    Name,
                    and Quantity
            --> Update Item Quantity in Inventory
            --> Return to Menu

        Choice 3: Generate Sales Report
            --> Prompt for the Quantity Sold
            --> Calculate Sales 
            --> Display Sales Report
            --> Return to Menu

        Choice 4: Popular Items
            --> Calculate or count
            --> Display Top 3 Popular Items
            --> Return to Menu

        Choice 5: Exit Program
            --> Display an exit message
            --> Exit the program
    ```

##	 Flow Chart BLUEPRINT 

```
         Start
           |
  Initialize Inventory Dictionary
           |
       Display Menu
           |
     Get User Choice
       /   |    \    \     \
      /    |     \    \     \
Choice 1 Choice 2 Choice 3 Choice 4 Choice 5
(Add Item) (Update) (Report) (Popular) (Exit)
      |      |         |         |        |
Prompt for Prompt for   Calculate Calculate  End
Details   Details    and Display and Display
Add/Update Update    Sales Report Popular Items
Inventory  Inventory
     \       \         \         /         /
      \       \         \       /         /
       \       \         \     /         /
        \       \         \   /         /
         \       \         \ /         /
                Return to Menu
```

## Flow Chart Graph
```
       +--------------------------+
       |          Start           |
       +-----------+--------------+
                   |
                   v
       +--------------------------+
       | Initialize Inventory Dict|
       +-----------+--------------+
                   |
                   v
       +--------------------------+
       |      Display Menu        |
       +-----------+--------------+
                   |
                   v
       +--------------------------+
       |     Get User Choice      |
       +-----------+--------------+
                   |
        +----------+----------+----------+----------+
        |          |          |          |          |
        v          v          v          v          v
  +------------+ +------------+ +------------+ +------------+ +------------+
  | Choice 1   | | Choice 2   | | Choice 3   | | Choice 4   | | Choice 5   |
  | (Add Item) | | (Update)   | | (Report)   | | (Popular)  | | (Exit)     |
  +------+-----+ +------+-----+ +------+-----+ +------+-----+ +------+-----+
         |              |              |              |              |
         v              v              v              v              v
+---------------+ +------------+ +-------------+ +-------------+    End
| Prompt Details| | Prompt     | | Calculate   | | Calculate   |
| Add/Update    | | Details    | | Sales Report| | Popular Items|
| Inventory     | | Update     | | Display     | | Display     |
| Return to Menu| | Inventory  | | Return to   | | Return to   |
+---------------+ +------------+ | Menu        | | Menu        |
                      |          +-------------+ +-------------+
                      v                    |
           +------------------+	       	   |
           | Return to Menu   |  <---------| 
           +------------------+
```

## Functions:
1- Adding new item to the inventory
``` python
def addnewitem(inventory):
    """
    Adds a new item to the inventory or updates an existing item.

    Args:
        inventory (dict): A dictionary where keys are item names and values are dictionaries with 'Price', 
        'Quantity', 
        'Quantity Sold', and 
        'Remaining Quantity'.
    """
```
2- Updating Stock Quantity:
``` python
def stock_quantity_update(inventory):
    """
    Updates the quantity of a specified item in the inventory.
    
    Parameters:
    inventory (dict): The inventory dictionary where keys are item names and values are dictionaries
                      with item details, including 'Quantity' and 'Remaining Quantity'.

    Returns:
    None
    """
```
3- Generating the sales Reports
``` python
def sales_report(inventory):
    """
    Displays a sales report for the inventory based on user choice.

    Args:
        inventory (dict): A dictionary where keys are item names and values are dictionaries with 'Price', 
        'Quantity Sold', and 
        'Remaining Quantity'.
    """
```
4- Creating a list of popular items in inventory
``` python
def popular_items(inventory):
    """
    Displays the top 3 most popular items in the inventory based on sales quantity.

    Args:
        inventory (dict): A dictionary where keys are item names and values are dictionaries with 'Quantity Sold'.
    """
```

## Snipshots From the program running:
 ### First and Second Option:

**Adding the items and updating the Quantity**
-----
![First and Second Options](<first and second option.png>)

 ### Third option:
 **Generating The Sales Reports**
---
![alt text](<third option.png>)

 ### Trying to use the program win the INV is empty
![alt text](<Empty Inv.png>)

## Conclusion:
This project demonstrates a simple yet effective way to manage inventory using Python. It can be extended with additional features such as generating reports, integrating with a database, or adding a user interface.
