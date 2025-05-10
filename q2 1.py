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

    mydb.commit()
    cursor.close()
    mydb.close()
