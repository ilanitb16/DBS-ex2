import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgers",
        port=3306,
    )
    cursor = mydb.cursor()

    # 1. Meals, how many were sold
    cursor.execute("""
    SELECT menu_meal.meal_name, COUNT(order_item.order_id) AS sold_meals_count
    FROM menu_meal
    -- Joins each meal with orders where it was ordered as a meal (is_meal = 1)
    LEFT JOIN order_item ON menu_meal.meal_id = order_item.item_id AND order_item.is_meal = 1
    GROUP BY menu_meal.meal_id
    ORDER BY sold_meals_count DESC;
    """)

    # count how many times each meal was ordered, including meals that were never ordered (count = 0),
    # then sort them from most popular to least.
    # if a meal was never ordered, it still appears in the result with a count of 0


    print(', '.join(str(row) for row in cursor.fetchall()))
