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

    mydb.commit()
    cursor.close()
    mydb.close()
