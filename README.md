# Database Builder

This script allows you to create a database by scanning a directory containing files and storing the data in the selected database system. The script supports three types of databases: SQLite, MySQL, and MongoDB.

## Requirements

Before running the script, make sure you have the following requirements fulfilled:

1. **SQLite**: SQLite is a self-contained, serverless, file-based database engine. You need to have the SQLite library installed on your system. If you don't have it, you can download it from the official SQLite website: [SQLite Downloads](https://www.sqlite.org/download.html).

2. **MySQL**: MySQL is an open-source relational database management system. You need to have the MySQL server installed and running. If you don't have it, you can download the MySQL Community Server from the official MySQL website: [MySQL Downloads](https://dev.mysql.com/downloads/mysql/). Follow the installation instructions for your operating system.

3. **MongoDB**: MongoDB is a NoSQL document database. You need to have the MongoDB server installed and running. If you don't have it, you can download the MongoDB Community Server from the official MongoDB website: [MongoDB Downloads](https://www.mongodb.com/try/download/community). Follow the installation instructions for your operating system.

## Usage

1. Clone or download the repository to your local machine.
2. Install the necessary dependencies if required (`pymongo`, `mysql-connector-python`, etc.).
3. Ensure that the corresponding database software is installed and running on your system.
4. Open the `database_builder.py` file in a text editor.
5. Modify the connection settings in the code based on your database configuration. Update the following lines:

```python
# Modify the connection settings accordingly for each database type
# SQLite connection settings
sqlite_connection = sqlite3.connect('your_database_name.db')

# MySQL connection settings
mysql_connection = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database'
)

# MongoDB connection settings
mongodb_client = MongoClient('your_mongodb_connection_url')
Save the database_builder.py file.
```

6.Open a terminal or command prompt and navigate to the directory where the database_builder.py file is located.

7.Run the script using the following command:

```code
python database_builder.py
```

8.Follow the prompts in the graphical user interface (GUI) to select the directory, database type, and folder name for the database files.

9.Click the "Create Database" button to start the database creation process.

10.Wait for the script to finish creating the database. Progress will be displayed in the progress bar.

11.Once the process is complete, the database will be created and placed in the specified folder on your desktop.

If you encounter any issues or have specific database configurations, refer to the documentation provided by SQLite, MySQL, or MongoDB for further assistance.

Note: This script is written in Python. If you want to run it from a Kotlin program, you'll need to integrate the Python script with your Kotlin code using appropriate libraries or tools.
