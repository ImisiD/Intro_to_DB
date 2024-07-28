import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")
        exit(1)

def connect_to_server():
    try:
        cnx = mysql.connector.connect(
            user='yourusername',    # replace with your MySQL username
            password='yourpassword' # replace with your MySQL password
        )
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else:
            print(f"Error: {err}")
        return None

def main():
    cnx = connect_to_server()
    if cnx:
        cursor = cnx.cursor()
        create_database(cursor)
        print("Database 'alx_book_store' created successfully!")
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    main()
