import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306
    )
    cursor = mydb.cursor()
    #  Used the first format but removed the line database="burgers" from connector
    #  because upon creating the DB we don't have a name for it yet because it does not exist.

    cursor.execute("""
    CREATE DATABASE burgers;
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
