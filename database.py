from db_connection import DatabaseConnection


def create_inventory_table():
    with DatabaseConnection('inventory.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS inventory(product_name text,product_number integer, category text, '
            'price float8, discount float8, quantity smallint)')


def add_ims_item(name, number, category, price, discount, quantity):
    with DatabaseConnection('inventory.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO inventory VALUES(?, ?, ?, ?, ?, ?)',
                       (name, number, category, price, discount, quantity))


def list_ims_items():
    with DatabaseConnection('inventory.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM inventory')
        items_list = [{'product_name': row[0], 'product_number': row[1], 'category': row[2],
                       'price': row[3], 'discount': row[4], 'quantity': row[5]} for row in cursor.fetchall()]
    return items_list


def search_ims_category_items(category):
    with DatabaseConnection('inventory.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM inventory WHERE category = ?', (category,))


def update_item_quantity():
    pass


def sell_ims_item(product_number, amount):
    with DatabaseConnection('inventory.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE inventory SET quantity = quantity - ? WHERE product_number = ?', (product_number, amount))


def delete_ims_item(product_number):
    with DatabaseConnection('inventory.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM inventory WHERE product_number=?', (product_number,))
