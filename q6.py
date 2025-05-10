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

    # alter the menu_meal table such that it will include an integer raw_cost
    # column, which will store the accumulative cost of all items in the meal.

    cursor.execute("""
    ALTER TABLE menu_meal
    ADD COLUMN raw_cost INT;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
