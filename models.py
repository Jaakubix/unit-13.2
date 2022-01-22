import sqlite3

class TodosSQLite:
    def create_connection(db_file):
        """ create a database connection to the SQLite database
         specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return conn

    def add_todo(conn, todo):
        """
        Create a new todo into the todos table
        :param conn:
        :param todo:
        :return: todo id
        """
        sql = '''INSERT INTO todos(tytul, opis, czy_wykonane)
             VALUES(?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, todo)
        conn.commit()
        return cur.lastrowid

    def select_all(conn, table):
        """
        Query all rows in the table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        conn.commit()
        return rows

    def select_where(conn, table, **query):
        """
        Query tasks from table with data from **query dict
        :param conn: the Connection object
        :param table: table name
        :param query: dict of attributes and values
        :return:
        """
        cur = conn.cursor()
        qs = []
        values = ()
        for k, v in query.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)
        cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
        rows = cur.fetchall()
        conn.commit()
        return rows

    def update(conn, table, id, **kwargs):
        """
        update tytul, opis, and czy_zrobione of a task
        :param conn:
        :param table: table name
        :param id: row id
        :return:
        """
        parameters = [f"{k} = ?" for k in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(v for v in kwargs.values())
        values += (id, )

        sql = f''' UPDATE {table}
                SET {parameters}
                WHERE id = ?'''
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            print("OK")
        except sqlite3.OperationalError as e:
            print(e)
        

    def delete_where(conn, table, **kwargs):
        """
        Delete from table where attributes from
        :param conn:  Connection to the SQLite database
        :param table: table name
        :param kwargs: dict of attributes and values
        :return:
        """
        qs = []
        values = tuple()
        for k, v in kwargs.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)

        sql = f'DELETE FROM {table} WHERE {q}'
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Deleted")

    def delete_all(conn, table):
        """
        Delete all rows from table
        :param conn: Connection to the SQLite database
        :param table: table name
        :return:
        """
        sql = f'DELETE FROM {table}'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Deleted")

    conn = create_connection("database.db")


todos = TodosSQLite()