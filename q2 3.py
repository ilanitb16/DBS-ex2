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

    # 3. meal_item: (meal_id: INT, item_id: INNOT NULLT)
    # Foreign Keys:
    # meal_item(meal_id) → menu_meal(meal_id)
    # meal_item(item_id) → menu_item(item_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meal_item (
        meal_id INT NOT NULL,
        item_id INT NOT NULL,
        FOREIGN KEY (meal_id) REFERENCES menu_meal(meal_id),
        FOREIGN KEY (item_id) REFERENCES menu_item(item_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
