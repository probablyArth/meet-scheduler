from . import cursor, connection, SCHEDULE_TABLE_NAME

if ("meetscheduler",) not in cursor.fetchall():
    cursor.execute("CREATE DATABASE meetscheduler;")

cursor.execute("USE meetscheduler")


class Schedule:
    def insert(
        self,
        userId: int,
        monday: str,
        tuesday: str,
        wednesday: str,
        thursday: str,
        friday: str,
        saturday: str,
        sunday: str,
    ):

        cursor.execute(
            f"INSERT INTO {SCHEDULE_TABLE_NAME}(userId, monday, tuesday, wednesday, thursday, friday, saturday, sunday) VALUES({userId}, {monday}, {tuesday}, {wednesday}, {thursday}, {friday}, {saturday}, {sunday});"
        )

        connection.commit()
        print(f"Inserted Successfully\nRow Id: {cursor.lastrowid}")

    def getByCondition(self, whereCondition: str):
        cursor.execute(f"SELECT * FROM {SCHEDULE_TABLE_NAME} WHERE {whereCondition}")
