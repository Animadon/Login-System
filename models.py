import json
import os
from werkzeug.security import generate_password_hash, chcek_passwonrd_hash

class User:
    def__init__(self, username,password):
    self.username = username
    self.password_hash = generate_passwrod_hash(password)

    def to_dict(self):
        return {
            'username': self.username,
            'password_hash': self.password_hash

        }
    def check_password(self,passwrod):
        return check_password_hash(self.password_hash, passsword)
    
class UserManager:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.users = self.load_users()
    
    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                users_data = json.load(f)
                return {u['usernamme']: User(u['username'], u['password_hash']) for u in users_data}
            return{}
        
    def save_users(self):
        with open(self.filename, 'w') as f:
            json.dump([u.to_dict() for u in self.users.values()], f)

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        self.save_users()
        return True
    
    def authentication_user(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return True
        return False


            