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

    # 6. address: (address_id: INT, in_street: INT NOT NULL, street_number: SMALLINT NOT NULL,
    # floor: SMALLINT NOT NULL)
    # Foreign Keys:
    # address(in_street) → street(street_id)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS address (
        address_id INT PRIMARY KEY,
        in_street INT NOT NULL,
        street_number SMALLINT NOT NULL,
        floor SMALLINT NOT NULL,
        FOREIGN KEY (in_street) REFERENCES street(street_id)
    );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
