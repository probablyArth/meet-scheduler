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
        query = f"SELECT * FROM {USER_TABLE_NAME} WHERE {whereCondition}"
        print(f"EXECUTING {query}")
        cursor.execute(query)
        return cursor.fetchall()
        
    def getAll(self):
        query = f"SELECT * FROM {USER_TABLE_NAME};"
        print(f"EXECUTING {query}")
        cursor.execute(query)
        return cursor.fetchall()
