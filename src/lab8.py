import psycopg2
import os

# --- DANGER ZONE ---
# PASSWORD stored in plain text. This is not secure.
# In a real-world application, use environment variables
# or a secret management service.
# For this lab, you can set an environment variable:
# export DB_PASSWORD='your_password'
# --- /DANGER ZONE ---

# --- STUDENT TODO: ---
# 1. Replace 'your_database' with the name of your database
# 2. Replace 'your_user' with your database username (often 'postgres')
# 3. Replace 'your_password' with your database password
# 4. Replace 'your_host' with your database host (usually 'localhost')
# 5. Replace 'your_port' with your database port (usually '5432' for PostgreSQL)

DB_NAME = "your_database"
DB_USER = "postgres"
DB_PASS = os.getenv("DB_PASSWORD", "your_password") # Fallback to insecure default
DB_HOST = "localhost"
DB_PORT = "5432"

def main():
    """
    Main function to connect to the database and perform operations.
    Students should modify this function to complete their lab assignments.
    """
    conn = None  # Initialize conn to None
    try:
        # Establish the connection
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Database connected successfully")
        cur = conn.cursor()

        # --- STUDENT TODO: Task 3 - Create Table ---
        # Write your SQL query to create a table.
        # Example for 'students' table:
        # create_table_query = """
        # CREATE TABLE IF NOT EXISTS students (
        #     id SERIAL PRIMARY KEY,
        #     name VARCHAR(100) NOT NULL,
        #     age INTEGER,
        #     admission_date DATE
        # );
        # """
        # cur.execute(create_table_query)
        # conn.commit()
        # print("Table 'students' created successfully.")

        # --- STUDENT TODO: Task 4 - Insert Data ---
        # Write your SQL query to insert data.
        # Use executemany for multiple inserts.
        # Example for 'students' table:
        # insert_query = "INSERT INTO students (name, age, admission_date) VALUES (%s, %s, %s);"
        # student_data = [
        #     ('John Doe', 20, '2023-09-01'),
        #     ('Jane Smith', 22, '2022-09-01'),
        #     ('Alice Johnson', 19, '2024-09-01'),
        #     ('Bob Williams', 21, '2023-09-01'),
        #     ('Anna Brown', 20, '2022-09-01')
        # ]
        # cur.executemany(insert_query, student_data)
        # conn.commit()
        # print(f"{cur.rowcount} records inserted successfully.")

        # --- STUDENT TODO: Task 5 - Update Data ---
        # Write your SQL query to update data.
        # Example for 'students' table:
        # update_query = "UPDATE students SET age = 21 WHERE name = 'John Doe';"
        # cur.execute(update_query)
        # conn.commit()
        # print(f"{cur.rowcount} record(s) updated successfully.")

        # --- STUDENT TODO: Task 6 - Delete Data ---
        # Write your SQL query to delete data.
        # Example for 'students' table:
        # delete_query = "DELETE FROM students WHERE name = 'Jane Smith';"
        # cur.execute(delete_query)
        # conn.commit()
        # print(f"{cur.rowcount} record(s) deleted successfully.")

        # --- STUDENT TODO: Task 7 - Select Data ---
        # Write your SQL query to select data.
        # Fetch and print the results.
        # Example for 'students' table:
        # select_query = "SELECT * FROM students ORDER BY age DESC;"
        # cur.execute(select_query)
        # records = cur.fetchall()
        # print("\n--- Student Records ---")
        # for record in records:
        #     print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Admission Date: {record[3]}")
        # print("-----------------------\n")

        # Remember to close the cursor
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while connecting to PostgreSQL: {error}")

    finally:
        # Ensure the connection is closed
        if conn is not None:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()