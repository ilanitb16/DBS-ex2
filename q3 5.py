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

    # 5. street table:
    cursor.execute("""
    INSERT INTO street (street_id, street_name, in_city) VALUES
    (1, 'Ocean Drive st.', 1),
    (2, 'Brickell ave.', 1),
    (3, 'Park ave.', 2),
    (4, 'Wall st.', 2),
    (5, 'Lombard ave.', 3),
    (6, 'Market st.', 3);
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
