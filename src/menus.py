import os
import main
from simple_password_generator import *
import sqlite3 as sql
from de_en_crypt import *


def logged_in(user_id:int, master_password:str):
    os.system("cls")

    print("Hello!\n\nYou have two options now:")
    print("1: Create a new password for X service")
    print("2: View service credentials\n")
    print("3: View password of service\n")
    print("4: Log out\n")

    start_choice = input("1/2/3: ")

    if start_choice == "1":
        new_password_for_service(user_id,master_password)
    if start_choice == "2":
        view_users_creds(user_id,master_password)
    if start_choice == "3":
        view_pass_serv(user_id,master_password)
    if start_choice == "4":
        main.main()
    logged_in(user_id, master_password)


def new_password_for_service(user_id:int, master_password:str):
    service = input("Enter service: ")
    username = input("Enter Username: ")
    password_choice = input(
        "(1) Generate new password or (2)insert new password: ")
    if password_choice == "1":
        password_length = input("Enter password length: ")
        password = generate_password(password_length)
    if password_choice == "2":
        password = input("Enter password: ")
    
    conn = sql.connect("myDB.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords(user_id,service,username,password) VALUES (?,?,?,?);",
                   (user_id, service, username, encrypt(master_password, password)))
    conn.commit()
    conn.close()

def view_users_creds(user_id:int, master_password:str):
    conn = sql.connect("myDB.db")
    cursor = conn.cursor()
    qur = cursor.execute(f"SELECT * FROM passwords WHERE user_id = '{user_id}'")
    fetch = qur.fetchall()
    conn.commit()
    conn.close()
    print(fetch)
    if input("Press key to go back"):
        logged_in(user_id, master_password)

def view_pass_serv(user_id:int, master_password:str):
    service = input("Show password for: ")
    conn = sql.connect("myDB.db")
    cursor = conn.cursor()
    qur = cursor.execute(f"SELECT password FROM passwords WHERE user_id = '{user_id}' AND LOWER(service) = '{service.lower()}'")
    fetch = qur.fetchall()
    conn.commit()
    conn.close()
    print(fetch)
    if(fetch != None):
        print(decrypt(master_password,fetch[-1][0]))
    if input("Press key to go back"):
        logged_in(user_id, master_password)
    