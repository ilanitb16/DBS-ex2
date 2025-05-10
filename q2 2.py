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

    # 2. menu_meal: (meal_id : INT, meal_name: VARCHAR NOT NULL, price : SMALLINT NOT NULL, served_at: VARCHAR NOT NULL)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu_meal (
        meal_id INT PRIMARY KEY,
        meal_name VARCHAR(255) NOT NULL,
        price SMALLINT NOT NULL,
        served_at VARCHAR(255) NOT NULL
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
