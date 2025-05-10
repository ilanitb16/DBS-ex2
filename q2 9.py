import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgers",
        port=3306
    )
    cursor = mydb.cursor()

    # 9. order_item: (order_id: INT, item_id: INT, is_meal: BOOLEAN)
    # Foreign Keys:
    # order_item(order_id) → full_order(order_id)
    # order_item(item_id) → menu_item(item_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_item (
        order_id INT NOT NULL,
        item_id INT NOT NULL,
        is_meal BOOLEAN,
        FOREIGN KEY (order_id) REFERENCES full_order(order_id),
        FOREIGN KEY (item_id) REFERENCES menu_item(item_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
