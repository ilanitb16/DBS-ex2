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
    WITH least_sold_meal AS (
        SELECT item_id AS meal_id
        FROM order_item
        WHERE is_meal = 1
        GROUP BY item_id
        ORDER BY COUNT(*) ASC
        LIMIT 1
    ),
    meal_orders AS (
        SELECT COUNT(*) AS meal_count
        FROM order_item
        WHERE is_meal = 1
          AND item_id = (SELECT meal_id FROM least_sold_meal)
    ),
    separate_orders AS (
        SELECT COUNT(*) AS separate_count
        FROM (
            SELECT oi.order_id
            FROM order_item oi
            WHERE oi.is_meal = 0
              AND oi.item_id IN (
                  SELECT item_id
                  FROM meal_item
                  WHERE meal_id = (SELECT meal_id FROM least_sold_meal)
              )
            GROUP BY oi.order_id
            HAVING 
              COUNT(DISTINCT oi.item_id) = (
                  SELECT COUNT(*)
                  FROM meal_item
                  WHERE meal_id = (SELECT meal_id FROM least_sold_meal)
              )
              AND
              MAX(CASE WHEN oi.item_id = (SELECT meal_id FROM least_sold_meal) THEN 1 ELSE 0 END) = 0
        ) AS sub
    )
    SELECT
        (SELECT meal_count FROM meal_orders) -
        (SELECT separate_count FROM separate_orders) AS difference;
    """)

    print(', '.join(str(row) for row in cursor.fetchall()))
