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

    cursor.execute("""
       SELECT menu_meal.meal_name
       FROM menu_meal 
       JOIN meal_item ON menu_meal.meal_id = meal_item.meal_id
       JOIN menu_item i ON meal_item.item_id = i.item_id
       GROUP BY menu_meal.meal_id, menu_meal.meal_name, menu_meal.price
       HAVING menu_meal.price >= SUM(i.price);
           """)


    print(', '.join(str(row) for row in cursor.fetchall()))
