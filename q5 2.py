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
    SELECT m.meal_name, COUNT(o.order_id) AS sold_count
    FROM menu_meal m
    LEFT JOIN order_item o ON m.meal_id = o.item_id AND o.is_meal = 1
    GROUP BY m.meal_id
    ORDER BY sold_count DESC;
    """)

    print(', '.join(str(row) for row in cursor.fetchall()))
