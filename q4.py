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
        SELECT
            city.city_name,
            SUM(CASE WHEN menu_meal.served_at = 'morning' THEN 1 ELSE 0 END) AS breakfast_count,
            SUM(CASE WHEN menu_meal.served_at = 'all day' THEN 1 ELSE 0 END) AS regular_count
        FROM
            order_item
        JOIN full_order ON order_item.order_id = full_order.order_id
        JOIN client ON full_order.by_client = client.client_id
        JOIN address ON client.client_address = address.address_id
        JOIN street ON address.in_street = street.street_id
        JOIN city ON street.in_city = city.city_id
        JOIN menu_meal ON order_item.item_id = menu_meal.meal_id
        WHERE order_item.is_meal = 1
        GROUP BY city.city_name
        ORDER BY city.city_name;
        """)
    print(', '.join(str(row) for row in cursor.fetchall()))
