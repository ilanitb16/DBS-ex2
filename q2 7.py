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

    mydb.commit()
    cursor.close()
    mydb.close()
