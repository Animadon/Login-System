from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from models import UserManager

app = Flask(__name__)
app.secret_key = 'test_environment'
user_manager = UserManager()

@app.route('/')
def index():
    # Error occurs here when Jinja tries to build the 'logout' URL:
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
    username = data['username']
    password = data['password']
    
    if user_manager.authenticate_user(username, password):
        session['username'] = username
        return Gjsonify({'status': 'Login Successfully'})
    return jsonify({'status': 'Invalid Username or Password'}), 401

# FIX: Added the missing /logout route to resolve the BuildError
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)