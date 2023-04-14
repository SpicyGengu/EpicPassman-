import sqlite3 as sql
import os
from de_en_crypt import *
import sign_in_up as siu

def setup():
    conn = sql.connect("myDB.db")

    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE if not exists users(id INTEGER PRIMARY KEY, name VARCHAR(255), masterpass VARCHAR(255));"
    )
    cursor.execute(
        "CREATE TABLE if not exists passwords(id INTEGER PRIMARY KEY, user_id INTEGER, service VARCHAR(255), username VARCHAR(255), password VARCHAR(255), FOREIGN KEY (user_id) REFERENCES users(id));"
    )
    conn.commit()
    conn.close()



def main():
    setup()
    os.system("cls")

    print("Hello!\n\nYou have two options now:")
    print("1: Sign in")
    print("2: Sign up\n")
    print("3: Exit\n")

    start_choice = input("1/2/3: ")

    if start_choice == "1":
        siu.sign_in()
    if start_choice == "2":
        siu.sign_up()


if __name__ == "__main__":
    main()
