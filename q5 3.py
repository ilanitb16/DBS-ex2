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
       SELECT m.meal_name
       FROM menu_meal m
       JOIN meal_item mi ON m.meal_id = mi.meal_id
       JOIN menu_item i ON mi.item_id = i.item_id
       GROUP BY m.meal_id, m.meal_name, m.price
       HAVING m.price >= SUM(i.price);
           """)


    print(', '.join(str(row) for row in cursor.fetchall()))
