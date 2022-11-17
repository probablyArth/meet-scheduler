from . import cursor, connection, SCHEDULE_TABLE_NAME


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
        query = f"INSERT INTO {SCHEDULE_TABLE_NAME}(userId, monday, tuesday, wednesday, thursday, friday, saturday, sunday) VALUES({userId}, '{monday}', '{tuesday}', '{wednesday}', '{thursday}', '{friday}', '{saturday}', '{sunday}');"
        print(f"\nExecuting:\n{query}")
        cursor.execute(query)
        connection.commit()
        return cursor.lastrowid

    def update(
        self,
        monday: str,
        tuesday: str,
        wednesday: str,
        thursday: str,
        friday: str,
        saturday: str,
        sunday: str,
    ):
        query = f"UPDATE {SCHEDULE_TABLE_NAME} SET monday='{monday}', tuesday='{tuesday}', wednesday='{wednesday}', thursday='{thursday}', friday='{friday}', saturday='{saturday}', sunday='{sunday}'"
        cursor.execute(query)
        connection.commit()
        print(f"\nExecuted:\n{query}")

    def getByCondition(self, whereCondition: str):
        query = f"SELECT * FROM {SCHEDULE_TABLE_NAME} WHERE {whereCondition}"
        print(f"\nExecuting:\n{query}")
        cursor.execute(query)
        return cursor.fetchall()
