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

    # 4. city: (city_id: INT, city_name: VARCHAR NOT NULL)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS city (
        city_id INT PRIMARY KEY,
        city_name VARCHAR(255) NOT NULL
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
