import os
from mysql import connector

connection = connector.connect(
    host=os.getenv("host"), password=os.getenv("password"), user=os.getenv("user")
)
cursor = connection.cursor()

cursor.execute("SHOW DATABASES;")
cursor.execute("SHOW TABLES;")

SCHEDULE_TABLE_NAME = "schedule"
USER_TABLE_NAME = "user"
BOOKING_TABLE_NAME = "booking"

dbs = cursor.fetchall()

if (SCHEDULE_TABLE_NAME,) not in dbs:
    cursor.execute(
        f"CREATE TABLE {SCHEDULE_TABLE_NAME} ( id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, monday VARCHAR(9) NOT NULL, tuesday VARCHAR(9) NOT NULL, wednesday VARCHAR(9) NOT NULL, thursday VARCHAR(9) NOT NULL, friday VARCHAR(9) NOT NULL, saturday VARCHAR(9) NOT NULL, sunday VARCHAR(9) NOT NULL, userId INTEGER, FOREIGN KEY (userId) REFERENCES {USER_TABLE_NAME}(id));"
    )

if (USER_TABLE_NAME,) not in dbs:
    cursor.execute(
        f"CREATE TABLE {USER_TABLE_NAME} VALUES (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(69) NOT NULL, password VARCHAR(69) NOT NULL);"
    )

if (BOOKING_TABLE_NAME,) not in dbs:
    cursor.execute(
        f"CREATE TABLE {BOOKING_TABLE_NAME} VALUES (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, topic VARCHAR(255), day VARCHAR(9) NOT NULL, bookingUserId FOREIGN KEY REFERENCES {USER_TABLE_NAME} (id) NOT NULL, bookedUserId FOREIGN KEY REFERENCES {USER_TABLE_NAME} (id) NOT NULL, timeRange VARCHAR(9) NOT NULL);"
    )
