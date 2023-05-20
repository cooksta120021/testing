import os
import json
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar, Combobox
from pymongo import MongoClient
import mysql.connector
import sqlite3


def process_directory(directory, database):
    total_files = count_files(directory)
    progress_var.set(0)
    progress_bar["maximum"] = total_files

    # Iterate over the files and subdirectories in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                process_file(file_path)
                progress_var.set(progress_var.get() + 1)
                window.update_idletasks()

    # After processing the directory, create the database folder on the desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    db_folder_name = folder_name_entry.get()
    db_folder_path = os.path.join(desktop_path, db_folder_name)
    os.makedirs(db_folder_path, exist_ok=True)

    # Create the database based on the selected option
    if database == "SQLite":
        create_sqlite_database(db_folder_path)
    elif database == "MySQL":
        create_mysql_database(db_folder_path)
    elif database == "MongoDB":
        create_mongodb_database(db_folder_path)


def process_file(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as f:
        content = f.read()

        # Perform any necessary processing on the file content
        # For example, you can extract relevant data using regular expressions or parsing techniques

        # Once you have extracted the data, you can store it in the database
        # You can use a database library like SQLite, MySQL, or MongoDB to create tables and insert data


def count_files(directory):
    total_files = 0
    for root, dirs, files in os.walk(directory):
        total_files += len(files)
    return total_files


def browse_directory():
    selected_directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, selected_directory)


def create_sqlite_database(db_folder_path):
    # Create a new SQLite database
    db_name = os.path.basename(db_folder_path)
    db_path = os.path.join(db_folder_path, f"{db_name}.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Scan the directory and create tables for each file
    for root, dirs, files in os.walk(db_folder_path):
        for file in files:
            if file.endswith('.csv'):
                table_name = os.path.splitext(file)[0]
                table_path = os.path.join(root, file)

                # Create the table and insert data
                with open(table_path, 'r') as f:
                    # Perform any necessary processing on the file content
                    # For example, you can extract column names and data types
                    column_names = ...
                    column_types = ...

                    # Create the table
                    create_table_query = f"CREATE TABLE {table_name} ({', '.join(f'{name} {type}' for name, type in zip(column_names, column_types))});"
                    cursor.execute(create_table_query)

                    # Insert data into the table
                    insert_data_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(column_names))});"
                    data = [tuple(row) for row in csv.reader(f)]
                    cursor.executemany(insert_data_query, data)

    # Commit and close the connection
    conn.commit()
    conn.close()


def create_mysql_database(db_folder_path):
    # Get MySQL connection settings from the user
    host = input("Enter MySQL host: ")
    user = input("Enter MySQL user: ")
    password = input("Enter MySQL password: ")
    database = input("Enter MySQL database name: ")

    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()

    # Scan the directory and create tables for each file
    for root, dirs, files in os.walk(db_folder_path):
        for file in files:
            if file.endswith('.csv'):
                table_name = os.path.splitext(file)[0]
                table_path = os.path.join(root, file)

                # Create the table and insert data
                with open(table_path, 'r') as f:
                    # Perform any necessary processing on the file content
                    # For example, you can extract column names and data types
                    column_names = ...
                    column_types = ...

                    # Create the table
                    create_table_query = f"CREATE TABLE {table_name} ({', '.join(f'{name} {type}' for name, type in zip(column_names, column_types))});"
                    cursor.execute(create_table_query)

                    # Insert data into the table
                    insert_data_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(column_names))});"
                    data = [tuple(row) for row in csv.reader(f)]
                    cursor.executemany(insert_data_query, data)

    # Commit and close the connection
    conn.commit()
    conn.close()


def create_mongodb_database(db_folder_path):
    # Get MongoDB connection settings from the user
    host = input("Enter MongoDB host: ")
    port = int(input("Enter MongoDB port: "))
    username = input("Enter MongoDB username: ")
    password = input("Enter MongoDB password: ")
    auth_source = input("Enter MongoDB authentication source: ")

    # Connect to the MongoDB server
    client = MongoClient(host=host, port=port, username=username,
                         password=password, authSource=auth_source)

    # Create a new database
    db_name = os.path.basename(db_folder_path)
    db = client[db_name]

    # Scan the directory and create collections for each file
    for root, dirs, files in os.walk(db_folder_path):
        for file in files:
            if file.endswith('.json'):
                collection_name = os.path.splitext(file)[0]
                collection = db[collection_name]

                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)

                # Insert the data into the collection
                collection.insert_many(data)

    # Disconnect from the MongoDB server
    client.close()


def create_database():
    directory = directory_entry.get()
    database = database_combo.get()
    process_directory(directory, database)
    status_label["text"] = "Database created and placed in the specified folder on the desktop."


# Create the main window
window = tk.Tk()
window.title("Database Builder")
window.geometry("400x350")

# Create the directory label and entry field
directory_label = tk.Label(window, text="Directory:")
directory_label.pack()
directory_entry = tk.Entry(window, width=30)
directory_entry.pack()
browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.pack()

# Create the database label and combo box
database_label = tk.Label(window, text="Database:")
database_label.pack()
database_combo = Combobox(window, values=["SQLite", "MySQL", "MongoDB"])
database_combo.pack()

# Create the folder name label and entry field
folder_name_label = tk.Label(window, text="Folder Name:")
folder_name_label.pack()
folder_name_entry = tk.Entry(window, width=30)
folder_name_entry.pack()

# Create the create database button
create_button = tk.Button(
    window, text="Create Database", command=create_database)
create_button.pack()

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Create the progress bar
progress_var = tk.DoubleVar()
progress_bar = Progressbar(window, variable=progress_var, maximum=100)
progress_bar.pack()

# Start the main event loop
window.mainloop()
