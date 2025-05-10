import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306
    )
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE DATABASE burgers;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
