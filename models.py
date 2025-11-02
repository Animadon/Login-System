import json
import os
from werkzeug.security import generate_password_hash, check_password_hash # FIX 1: Corrected typo 'check_passwonrd_hash'

class User:
    # FIX 2: Added colon and fixed indentation for the method body
    def __init__(self, username, password): 
        self.username = username
        # FIX 3: Corrected typo 'generate_passwrod_hash'
        self.password_hash = generate_password_hash(password) 

    def to_dict(self):
        return {
            'username': self.username,
            # FIX 4: Removed extra newline/indentation error
            'password_hash': self.password_hash
        }
    
    # FIX 5: Corrected typo 'passwrod' in parameter, and fixed indentation
    def check_password(self, password): 
        # FIX 6: Corrected typo 'passsword' in function call
        return check_password_hash(self.password_hash, password) 
    
class UserManager:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.users = self.load_users()
    
    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                users_data = json.load(f)
                # FIX 7: Corrected typo 'usernamme' to 'username'
                # NOTE: The load function assumes the stored password_hash is the actual hash, 
                # so we pass it directly to User constructor, not expecting it to be hashed again.
                return {u['username']: User(u['username'], u['password_hash']) for u in users_data}
        
        # FIX 8: Corrected indentation for the final return statement
        return {}
        
    def save_users(self):
        with open(self.filename, 'w') as f:
            json.dump([u.to_dict() for u in self.users.values()], f)

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        self.save_users()
        return True
    
    # FIX 9: Corrected typo 'authentication_user' to 'authenticate_user'
    def authenticate_user(self, username, password): 
        user = self.users.get(username)
        if user and user.check_password(password):
            return True
        return False