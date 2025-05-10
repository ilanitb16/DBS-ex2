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

    # chicken Oburger meal: id = 3
    cursor.execute("""
    UPDATE menu_meal
    JOIN (
       SELECT meal_item.meal_id, SUM(menu_item.price) AS total_price
       FROM meal_item
       JOIN menu_item ON meal_item.item_id = menu_item.item_id
       GROUP BY meal_item.meal_id
    ) AS price_table ON menu_meal.meal_id = price_table.meal_id
    SET menu_meal.raw_cost = price_table.total_price
    WHERE menu_meal.meal_id = 3;
    """)

    # calculating the sum of item prices for id = 3, and saving the sam in raw_cost.

    mydb.commit()
    cursor.close()
    mydb.close()



