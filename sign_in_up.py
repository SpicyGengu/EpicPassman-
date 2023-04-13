import sqlite3 as sql
from de_en_crypt import *

def sign_up():
    username = input("Username: ")
    if user_exists(username):
        print("User already exists")
        sign_up()
    master_pass = input("Master pass: ")
    conn = sql.connect("myDB.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name,masterpass) VALUES (?,?);",(username.lower(), encrypt(master_pass,master_pass)))
    conn.commit()
    conn.close()

def sign_in():
    username = input("Username: ")
    if user_exists(username):
        master_pass = input("Enter master password: ")

        if password_matches(username,master_pass):
            print("In main frame")


def password_matches(username: str,master_pass):
    conn = sql.connect("myDB.db")
    cursor = conn.cursor()
    qur = cursor.execute(f"SELECT masterpass FROM users WHERE name = '{username.lower()}'")
    encrypted_pass = qur.fetchone()[0]
    conn.close()
    decrypted_pass = decrypt(master_pass,encrypted_pass)
    if decrypted_pass == master_pass:
        return True
    return False

def user_exists(name: str) -> bool:
    conn = sql.connect("myDB.db")
    cursor = conn.cursor()
    qur = cursor.execute(f"SELECT * FROM users WHERE name = '{name.lower()}'")
    fetch = qur.fetchone()
    conn.close()
    print(fetch)
    if (fetch != None):
        return True
    else:
        return False
