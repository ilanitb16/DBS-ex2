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
    WITH 
-- Get the least sold meal and how many times it was ordered
LeastSoldMeal AS (
    SELECT m.meal_id, m.meal_name, COUNT(oi.order_id) AS meal_orders
    FROM menu_meal m
    LEFT JOIN order_item oi ON m.meal_id = oi.item_id AND oi.is_meal = TRUE
    GROUP BY m.meal_id, m.meal_name
    ORDER BY meal_orders ASC
    LIMIT 1
),

-- Get all items in that meal
MealItems AS (
    SELECT mi.item_id
    FROM meal_item mi
    JOIN LeastSoldMeal lsm ON mi.meal_id = lsm.meal_id
),

-- Orders that include all those items (only as separate items, no meal)
CompleteSetOrders AS (
    SELECT oi.order_id
    FROM order_item oi
    WHERE oi.is_meal = 0
      AND oi.item_id IN (SELECT item_id FROM MealItems)
      AND oi.order_id NOT IN (
          SELECT order_id FROM order_item
          WHERE is_meal = 1
            AND item_id = (SELECT meal_id FROM LeastSoldMeal)
      )
    GROUP BY oi.order_id
    HAVING COUNT(DISTINCT oi.item_id) = (SELECT COUNT(*) FROM MealItems)
)

-- Final subtraction
SELECT
    (SELECT meal_orders FROM LeastSoldMeal) -
    (SELECT COUNT(*) FROM CompleteSetOrders) AS difference;

    """)

    print(', '.join(str(row) for row in cursor.fetchall()))
