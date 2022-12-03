import database
from art import logo

USER_CHOICE = """
Enter:
- 'a' to add a new item
- 'l' to list all items
- 'f' to search for specific item
- 'w' to mark an item sold
- 'd' to delete an item
- 'q' to quit

Your choice: """

print(logo)


def menu():
    database.create_inventory_table()  # running this to make sure file is created
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            add_new_item()
        elif user_input == 'l':
            list_all_items()
        elif user_input == 'f':
            search_item()
        elif user_input == 'w':
            item_sold()
        elif user_input == 'd':
            delete_item()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


def add_new_item():
    name = input("Enter product name: ")
    number = int(input("Enter product number (6 digits): "))
    category = input("Enter category name: ")
    price = float(input("Enter product price: $"))
    discount = float(input("Enter product discount: $"))
    quantity = int(input("Enter product quantity: "))

    category_formatted = category.title()
    database.add_ims_item(name, number, category_formatted, price, discount, quantity)


def list_all_items():
    items = database.list_ims_items()
    for item in items:
        print("product_name | product_number | category | price | discount | quantity")
        print(f"{item['product_name']} | {item['product_number']} | {item['category']} | {item['price']} | {item['discount']} | {item['quantity']}")


def search_item():
    pass


def item_sold():
    pass


def delete_item():
    pass


menu()
