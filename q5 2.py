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
    SELECT menu_meal.meal_id, menu_meal.meal_name, COUNT(order_item.order_id) AS meal_orders
    FROM menu_meal 
    LEFT JOIN order_item ON menu_meal.meal_id = order_item.item_id AND order_item.is_meal = TRUE
    GROUP BY menu_meal.meal_id, menu_meal.meal_name
    ORDER BY meal_orders ASC
    LIMIT 1
    ),

    -- Get all items in that meal
    MealItems AS (
    SELECT mi.item_id
    FROM meal_item mi
    JOIN LeastSoldMeal lsm ON mi.meal_id = lsm.meal_id
    ),

-- Orders that include only as separate items, (no meal)
CompleteSetOrders AS (
    SELECT order_item.order_id
    FROM order_item
    WHERE order_item.is_meal = 0
      AND order_item.item_id IN (SELECT item_id FROM MealItems)
      AND order_item.order_id NOT IN (
          SELECT order_id FROM order_item
          WHERE is_meal = 1
            AND item_id = (SELECT meal_id FROM LeastSoldMeal)
      )
    GROUP BY order_item.order_id
    HAVING COUNT(DISTINCT order_item.item_id) = (SELECT COUNT(*) FROM MealItems)
)

-- subtraction
SELECT
    (SELECT meal_orders FROM LeastSoldMeal) -
    (SELECT COUNT(*) FROM CompleteSetOrders) AS difference;

""")

    print(', '.join(str(row) for row in cursor.fetchall()))
