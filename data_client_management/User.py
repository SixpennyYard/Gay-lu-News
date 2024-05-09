import csv
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, username, email=None, hashed_password=None):
        self._username = username
        self.__email = email
        self.__hashed_password = hashed_password
        if self.__email is None or self.__hashed_password is None:
            self._get_user_data(username)

    @property
    def get_email(self):
        return self.__email

    @property
    def get_hashed_password(self):
        return self.__hashed_password

    @staticmethod
    def save_data(username, email, hashed_password):
        with open('data/users.csv', mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, email, hashed_password])

    def _get_user_data(self, username):
        with open('data/users.csv', mode='r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if username == row[0]:
                    self.__email = row[1]
                    self.__hashed_password = row[2]
                    self.id = username

    @property
    def id(self):
        return self._username

    @id.setter
    def id(self, value):
        self._username = value
