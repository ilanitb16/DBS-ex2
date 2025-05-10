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

    # small Onuggets meal: id = 4
    cursor.execute("""
    UPDATE menu_meal as m
    JOIN (
        SELECT mi.meal_id, SUM(i.price) AS total_price
        FROM meal_item mi
        JOIN menu_item i ON mi.item_id = i.item_id
        GROUP BY mi.meal_id
    ) AS price_table ON m.meal_id = price_table.meal_id
    SET m.raw_cost = price_table.total_price
    WHERE m.meal_id = 4;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
