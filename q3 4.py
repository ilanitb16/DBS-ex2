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

    # 4. city table:
    cursor.execute("""
    INSERT INTO city (city_id, city_name) VALUES
    (1, 'MIA'), (2, 'NYC'), (3, 'SF');
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
