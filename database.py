import psycopg2

class Database:
    def __init__(self):
        self.connect = psycopg2.connect(
            database='name', # PostgreSql database name
            user='postgres', # PostgreSql username
            host='localhost', # does not touch
            password='password' # PostgreSql password
        )

    def manager(self, sql, *args, commit=False, fetchall=False, fetchone=False):
        with self.connect as connect:
            result = None
            with connect.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    connect.commit()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchone:
                    result = cursor.fetchone()
            return result

    def create_users(self):
        sql = """CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            login VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(50) NOT NULL
        );"""
        self.manager(sql, commit=True)

    def insert_users(self, first_name, last_name, login, password):
        sql = """INSERT INTO users (first_name, last_name, login, password) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING;"""
        self.manager(sql, first_name, last_name, login, password, commit=True)

    def select_table(self, table_name):
        allowed_table = ['users']

        if table_name not in allowed_table:
            raise ValueError(f"Kiritilgan jadval nomi noto'g'ri: {table_name}")

        sql = f"""SELECT * FROM {table_name}"""
        return self.manager(sql, fetchall=True)

    def find(self, table_name, column_name, value):
        allowed_table = ['users']

        if table_name not in allowed_table:
            raise ValueError(f"Kiritilgan jadval nomi noto'g'ri: {table_name}")

        sql = f"""SELECT * FROM {table_name} WHERE {column_name} = %s"""
        result = self.manager(sql, value, fetchall=True)

        if result:
            return True
        else:
            return False

    def counts(self, table_name):
        allowed_table = ['users']

        if table_name not in allowed_table:
            raise ValueError(f"Kiritilgan jadval nomi noto'g'ri: {table_name}")

        sql = f"""SELECT COUNT(*) FROM {table_name}"""
        return self.manager(sql, fetchone=True)

connect = Database()