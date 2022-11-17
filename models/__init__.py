import os
from mysql import connector
from dotenv import load_dotenv

load_dotenv()
connection = connector.connect(
    host=os.getenv("host"), password=os.getenv("password"), user=os.getenv("user")
)
cursor = connection.cursor()

cursor.execute("SHOW DATABASES;")
if ("meetscheduler",) not in cursor.fetchall():
    cursor.execute("CREATE DATABASE meetscheduler;")
cursor.execute("USE meetscheduler")
cursor.execute("SHOW TABLES;")

SCHEDULE_TABLE_NAME = "schedule"
USER_TABLE_NAME = "user"
BOOKING_TABLE_NAME = "booking"

tables = cursor.fetchall()

if (USER_TABLE_NAME,) not in tables:
    cursor.execute(
        f"CREATE TABLE {USER_TABLE_NAME} (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(69) NOT NULL, password VARCHAR(69) NOT NULL);"
    )

if (SCHEDULE_TABLE_NAME,) not in tables:
    cursor.execute(
        f"CREATE TABLE {SCHEDULE_TABLE_NAME} ( id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, monday CHAR(11) NOT NULL, tuesday CHAR(11) NOT NULL, wednesday CHAR(11) NOT NULL, thursday CHAR(11) NOT NULL, friday CHAR(11) NOT NULL, saturday CHAR(11) NOT NULL, sunday CHAR(11) NOT NULL, userId INTEGER, FOREIGN KEY (userId) REFERENCES {USER_TABLE_NAME}(id));"
    )


if (BOOKING_TABLE_NAME,) not in tables:
    cursor.execute(
        f"CREATE TABLE {BOOKING_TABLE_NAME} (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, topic VARCHAR(255) NOT NULL, `day` VARCHAR(9) NOT NULL, bookingUserId INT NOT NULL, bookedUserId INT NOT NULL, FOREIGN KEY (bookingUserId) REFERENCES {USER_TABLE_NAME}(id), FOREIGN KEY (bookedUserId) REFERENCES {USER_TABLE_NAME}(id), timeRange VARCHAR(9) NOT NULL);"
    )
