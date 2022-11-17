from . import cursor, connection, USER_TABLE_NAME


class User:
    def insert(self, name: str, password: str):

        cursor.execute(
            f'INSERT INTO {USER_TABLE_NAME}(name, password) VALUES("{name}", "{password}");'
        )

        connection.commit()
        print(f"Inserted Successfully\nRow Id: {cursor.lastrowid}")
        return cursor.lastrowid

    def getByCondition(self, whereCondition: str):
        print(f"SELECT * FROM {USER_TABLE_NAME} WHERE {whereCondition}")
        cursor.execute(f"SELECT * FROM {USER_TABLE_NAME} WHERE {whereCondition}")
        return cursor.fetchall()
