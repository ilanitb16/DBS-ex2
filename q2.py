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

    # 1. menu_item: (item_id : INT, item_name: VARCHAR NOT NULL, price : SMALLINT NOT NULL)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu_item (
        item_id INT PRIMARY KEY,
        item_name VARCHAR(255) NOT NULL,
        price SMALLINT NOT NULL
    );
    """)

    # 2. menu_meal: (meal_id : INT, meal_name: VARCHAR NOT NULL, price : SMALLINT NOT NULL, served_at: VARCHAR NOT NULL)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu_meal (
        meal_id INT PRIMARY KEY,
        meal_name VARCHAR(255) NOT NULL,
        price SMALLINT NOT NULL,
        served_at VARCHAR(255) NOT NULL
    );
    """)

    # 3. meal_item: (meal_id: INT, item_id: INNOT NULLT)
    # Foreign Keys:
    # meal_item(meal_id) → menu_meal(meal_id)
    # meal_item(item_id) → menu_item(item_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meal_item (
        meal_id INT NOT NULL,
        item_id INT NOT NULL,
        FOREIGN KEY (meal_id) REFERENCES menu_meal(meal_id),
        FOREIGN KEY (item_id) REFERENCES menu_item(item_id)
    );
    """)

    # 4. city: (city_id: INT, city_name: VARCHAR NOT NULL)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS city (
        city_id INT PRIMARY KEY,
        city_name VARCHAR(255) NOT NULL
    );
    """)

    # 5. street: (street_id: INT, street_name: VARCHAR NOT NULL, in_city: INT NOT NULL)
    # Foreign Keys:
    # street(in_city) → city(city_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS street (
        street_id INT PRIMARY KEY,
        street_name VARCHAR(255) NOT NULL,
        in_city INT NOT NULL,
        FOREIGN KEY (in_city) REFERENCES city(city_id)
    );
    """)

    # 6. address: (address_id: INT, in_street: INT NOT NULL, street_number: SMALLINT NOT NULL,
    # floor: SMALLINT NOT NULL)
    # Foreign Keys:
    # address(in_street) → street(street_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS address (
        address_id INT PRIMARY KEY,
        in_street INT NOT NULL,
        street_number SMALLINT NOT NULL,
        floor SMALLINT NOT NULL,
        FOREIGN KEY (in_street) REFERENCES street(street_id)
    );
    """)

    # 7. client: (client_id: INT, client_name: VARCHAR NOT NULL, client_address: INT NOT NULL )
    # Foreign Keys:
    # client(client_address) → address(address_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS client (
        client_id INT PRIMARY KEY,
        client_name VARCHAR(255) NOT NULL,
        client_address INT NOT NULL,
        FOREIGN KEY (client_address) REFERENCES address(address_id)
    );
    """)

    # 8. full_order: (order_id: INT, order_time: DATETIME NOT NULL, by_client: INT NOT NULL)
    # INSERT INTO "order" (order_id, order_time, by_client) VALUES
    # Foreign Keys:
    # full_order(by_client) → client(client_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS full_order (
        order_id INT PRIMARY KEY,
        order_time DATETIME NOT NULL,
        by_client INT NOT NULL,
        FOREIGN KEY (by_client) REFERENCES client(client_id)
    );
    """)

    # 9. order_item: (order_id: INT, item_id: INT, is_meal: BOOLEAN)
    # Foreign Keys:
    # order_item(order_id) → full_order(order_id)
    # order_item(item_id) → menu_item(item_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_item (
        order_id INT NOT NULL,
        item_id INT NOT NULL,
        is_meal BOOLEAN,
        FOREIGN KEY (order_id) REFERENCES full_order(order_id),
        FOREIGN KEY (item_id) REFERENCES menu_item(item_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
