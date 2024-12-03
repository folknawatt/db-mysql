import mysql.connector


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="mysql",  # Service name from docker-compose.yml
            user="testuser",
            password="testpassword",
            database="testdb",
        )
        print("Connection to MySQL successful!")
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES;")
        for db in cursor:
            print(db)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    connect_to_database()
