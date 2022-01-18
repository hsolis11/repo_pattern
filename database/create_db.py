import sqlite3

DATABASE = "test.db"


def connect(database):
    return sqlite3.connect(database)


def create_user_table(database):
    conn = connect(database)
    conn.execute("""CREATE TABLE users (id integer PRIMARY KEY,
                                        f_name text NOT NULL,
                                        l_name text NOT NULL,
                                        username text NOT NULL,
                                        password text NOT NULL)""")
    conn.commit()


def create_email_table(database):
    conn = connect(database)
    conn.execute("""CREATE TABLE emails (user_id integer,
                    primary_email text NOT NULL,
                    secondary_email text NOT NULL,
                    primary_validated integer DEFAULT 0,
                    secondary_validated integer DEFAULT 0,
                    FOREIGN KEY(user_id) REFERENCES users (id))""")
    conn.commit()


def main(database):
    create_user_table(database)
    create_email_table(database)


if __name__ == '__main__':
    main(DATABASE)
