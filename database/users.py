from database.connect import BaseRepo, StoreException
from dataclasses import dataclass


@dataclass
class User:
    id: int
    f_name: str
    l_name: str
    username: str
    password: str


class Users(BaseRepo):

    @staticmethod
    def _extract(data, user_obj):
        users = []
        for user in data:
            users.append(user_obj(*user))
        return users

    def add_user(self, user: User):
        try:
            c = self.conn.cursor()
            sql = """INSERT INTO users(f_name, l_name, username, password) VALUES(?,?,?,?)"""
            values = (user.f_name, user.l_name, user.username, user.password)
            c.execute(sql, values)
        except Exception as e:
            raise StoreException('error storing user')

    def get_user(self, user_id=None, username=None):
        try:
            sql = None
            values = None
            c = self.conn.cursor()
            if user_id:
                sql = """SELECT * FROM users WHERE id = ?"""
                values = (user_id,)
            elif username:
                sql = """SELECT * FROM users WHERE username = ?"""
                values = (username,)
            c.execute(sql, values)
            data = c.fetchall()
            return User(*data[0])

        except Exception as e:
            raise StoreException('error getting user')

    def get_list(self):
        try:
            c = self.conn.cursor()
            sql = """SELECT * FROM users"""
            c.execute(sql)
            data = c.fetchall()
            if data:
                return self._extract(data, User)
            else:
                return None
        except Exception as e:
            print(e)
            return None


