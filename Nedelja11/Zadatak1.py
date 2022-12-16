menu = {
    "coffee": 3.50,
    "tea": 2.50,
    "soda": 2.00,
    "water": 1.50
}

def add_item(name, price):
    menu[name] = price
    print(menu)

def delete_item(name):
    del menu[name]
    print(menu)

def update_price(name, price):
    menu[name] = price
    print(menu)

while True:
    print("Welcome to our cafe! What would you like to do?")
    print("1. Add an item to the menu")
    print("2. Delete an item from the menu")
    print("3. Update the price of an item")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        name = input("Enter the name of the item: ")
        price = float(input("Enter the price of the item: "))
        add_item(name, price)
    elif choice == "2":
        name = input("Enter the name of the item: ")
        delete_item(name)
    elif choice == "3":
        name = input("Enter the name of the item: ")
        price = float(input("Enter the new price of the item: "))
        update_price(name, price)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
