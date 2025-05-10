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

    # 1. menu_item table
    cursor.execute("""
    INSERT INTO menu_item (item_id, item_name, price) VALUES
    (1, 'small fries', 2), (2, 'Osalad', 2), (3, 'large fries', 5),
    (4, 'Oburger', 6), (5, 'double Oburger', 10), (6, 'chicken Oburger', 3),
    (7, 'Onuggets', 3), (8, 'double Onuggets', 5), (9, 'Omlette', 3),
    (10, 'Opancake', 3), (11, 'Owaffle', 3), (12, 'light Obeverage', 2),
    (13, 'hot Obeverage', 2);
    """)

    # 2. menu_meal table:
    cursor.execute("""
    INSERT INTO menu_meal (meal_id, meal_name, price, served_at) VALUES
    (1, 'small Oburger Meal', 8, 'all day'),
    (2, 'large Oburger Meal', 14, 'all day'),
    (3, 'chicken Oburger meal', 8, 'all day'),
    (4, 'small Onuggets meal', 7, 'all day'),
    (5, 'large Onuggets meal', 11, 'all day'),
    (6, 'Omfast', 4, 'morning'),
    (7, 'Opanfast', 4, 'morning'),
    (8, 'Owaffast', 4, 'morning');
    """)

    # 3. meal_item table:
    cursor.execute("""
    INSERT INTO meal_item (meal_id, item_id) VALUES
    (1, 1), (1, 4), (1, 12),
    (2, 3), (2, 5), (2, 12),
    (3, 1), (3, 6), (3, 12),
    (4, 1), (4, 7), (4, 12),
    (5, 3), (5, 8), (5, 12),
    (6, 9), (6, 13),
    (7, 10), (7, 13),
    (8, 11), (8, 13);
    """)

    # 4. city table:
    cursor.execute("""
    INSERT INTO city (city_id, city_name) VALUES
    (1, 'MIA'), (2, 'NYC'), (3, 'SF');
    """)

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

    # 6. address table:
    cursor.execute("""
    INSERT INTO address (address_id, in_street, street_number, floor) VALUES
    (1, 2, 10, 2),
    (2, 1, 1, 10),
    (3, 3, 23, 101),
    (4, 4, 52, 304),
    (5, 5, 5, 2),
    (6, 6, 34, 1);
    """)

    # 7. client table:
    cursor.execute("""
    INSERT INTO client (client_id, client_name, client_address) VALUES
    (1, 'Lee Kang', 5),
    (2, 'Wang Fu', 6),
    (3, 'Sandro Moretti', 3),
    (4, 'Giuseppe Angelo', 4),
    (5, 'Favian Adames Alonso', 1),
    (6, 'Edward Pagan Henriquez', 2);
    """)

    # 8. full_order table:
    cursor.execute("""
    INSERT INTO full_order (order_id, order_time, by_client) VALUES
    (1, '2025-04-20 08:15:00', 1),
    (2, '2025-04-20 09:00:00', 1),
    (3, '2025-04-20 10:00:00', 2),
    (4, '2025-04-20 11:00:00', 2),
    (5, '2025-04-20 13:00:00', 1),
    (6, '2025-04-20 08:30:00', 3),
    (7, '2025-04-20 14:00:00', 3),
    (8, '2025-04-20 14:30:00', 4),
    (9, '2025-04-20 12:00:00', 5),
    (10, '2025-04-20 12:15:00', 6),
    (11, '2025-04-20 08:15:00', 5);
    """)

    # 9. order_item table:
    cursor.execute("""
    INSERT INTO order_item (order_id, item_id, is_meal) VALUES
    (1, 6, 1),
    (2, 7, 1),
    (3, 8, 1),
    (4, 6, 1),
    (5, 1, 1),
    (6, 6, 0),
    (6, 12, 0),
    (6, 1, 0),
    (6, 6, 1),
    (7, 1, 0),
    (7, 1, 1),
    (8, 3, 0),
    (8, 2, 1),
    (9, 6, 1),
    (9, 4, 1),
    (9, 5, 1),
    (10, 2, 0),
    (10, 2, 1),
    (11, 1, 1);
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
