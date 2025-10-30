from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from models import UserManager

app = Flask(__name__)
app.secret_key = 'test_environment'
user_manager = UserManager()

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', logged_in=True, username=session['username'])
    
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
        data= request.json
        username = data['username']
        password = data['password']
        if user_manager.add_user(username, password):
            return jsonify({'status': 'User Registered Successfully'})
        return jsonify({'status': 'User already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
        data = request.json
        usernmae = data['username']
        password = data['password']
        if user_manager.authenticate_user(username, password):
            session['username'] = username
            return jsonify({'status': 'Login Successfully'})
        return jsonify({'status': ' Invalid Username or Password}), 401'})

    
if __name__ == '__main__':
    app.run (debug=True)