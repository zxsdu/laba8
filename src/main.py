import psycopg2
from datetime import datetime

conn = None
cur = None

try:
    # Підключення до бази даних «airport»
    conn = psycopg2.connect(
        host="localhost",
        database="airport",
        user="postgres",
        password="admin",  # Замініть на ваш пароль
        port="5432"
    )
    print("Database connected successfully")

    cur = conn.cursor()

    # Створення таблиці «flights» (Рейси)
    cur.execute("DROP TABLE IF EXISTS flights")
    create_table_query = """
    CREATE TABLE flights (
        flight_number VARCHAR(10) PRIMARY KEY,
        departure_point VARCHAR(100),
        destination VARCHAR(100),
        departure_time TIMESTAMP
    )
    """
    cur.execute(create_table_query)
    conn.commit()
    print("Table 'flights' created successfully")

    # Вставка даних
    insert_query = """
    INSERT INTO flights (flight_number, departure_point, destination, departure_time)
    VALUES (%s, %s, %s, %s)
    """
    flights_data = [
        ("PS101", "Kyiv", "London", datetime(2026, 11, 20, 8, 30)),
        ("PS202", "Kyiv", "Warsaw", datetime(2026, 11, 20, 6, 15)),
        ("FR303", "Lviv", "Berlin", datetime(2026, 11, 21, 14, 45)),
        ("LH404", "Kyiv", "Frankfurt", datetime(2026, 11, 22, 11, 0)),
        ("W6505", "Odesa", "Vienna", datetime(2026, 11, 19, 19, 20)),
        ("TK606", "Kharkiv", "Istanbul", datetime(2026, 11, 23, 9, 10))
    ]
    cur.executemany(insert_query, flights_data)
    conn.commit()
    print("Data inserted successfully")

    # Оновлення даних: перенесення рейсу PS101 на 10:00
    update_query = """
    UPDATE flights
    SET departure_time = %s
    WHERE flight_number = %s
    """
    cur.execute(update_query, (datetime(2026, 11, 20, 10, 0), "PS101"))
    conn.commit()
    print("Data updated successfully")

    # Видалення даних: спочатку знаходимо найранніший рейс
    cur.execute("SELECT MIN(departure_time) FROM flights")
    earliest_time = cur.fetchone()[0]

    # Потім видаляємо рейс з цим часом вильоту
    delete_query = """
    DELETE FROM flights
    WHERE departure_time = %s
    """
    cur.execute(delete_query, (earliest_time,))
    conn.commit()
    print("Data deleted successfully")

    # Вибірка даних: рейси з Києва, відсортовані за часом вильоту
    select_query = """
    SELECT * FROM flights
    WHERE departure_point = 'Kyiv'
    ORDER BY departure_time ASC
    """
    cur.execute(select_query)
    flights = cur.fetchall()
    print("Selected flights:")
    for flight in flights:
        print(f"Flight: {flight[0]}, From: {flight[1]}, To: {flight[2]}, "
              f"Departure: {flight[3]}")

except (Exception, psycopg2.Error) as error:
    print("Error while working with PostgreSQL", error)

finally:
    if conn:
        if cur:
            cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
