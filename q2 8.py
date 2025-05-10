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

    mydb.commit()
    cursor.close()
    mydb.close()
