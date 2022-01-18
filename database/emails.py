from database.connect import BaseRepo, StoreException
from dataclasses import dataclass


@dataclass
class Email:
    user_id: int
    primary_email: str
    secondary_email: str
    primary_validated: bool
    secondary_validated: bool


class Emails(BaseRepo):
    def get_email(self, user_id: bool):
        try:
            c = self.conn.cursor()
            sql = """SELECT * FROM emails WHERE user_id = ?"""
            values = (user_id,)
            c.execute(sql, values)
            data = c.fetchall()
            return Email(*data[0])

        except Exception as e:
            raise StoreException('error getting user')
