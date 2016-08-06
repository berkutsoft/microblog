import re
from app import app, db

class User(db.Model):
    #...
    @staticmethod
    def make_valid_nickname(nickname):
        return re.sub('[^a-zA-Z0-9_\.]', '', nickname)