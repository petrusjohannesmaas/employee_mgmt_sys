from flask import Flask, request, render_template, make_response, redirect
from database.insert import insert
from database.read import read
from database.delete import delete
from database.exceptions import NotAuthorized
from database.roles import *

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')

@app.route('/access', methods=['POST'])
def access():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        response = make_response(redirect('/'))
        response.set_cookie('username', username)
        response.set_cookie('password', password)
        return response
    else:
        return "Invalid username or password"

@app.route('/logout', methods=['GET'])
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('username', '')
    response.set_cookie('password', '')
    return response

@app.route('/', methods=['GET'])
def index():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    if username and password:
        return render_template('ems.html')
    else:
        return redirect('/login')

@app.route('/insert', methods=['POST'])
def insert_employee():
    if request.cookies.get('username') in MGMT:
        eID = request.form['eID']
        name = request.form['name']
        department = request.form['department']
        insert(eID, name, department)
        return "Employee inserted successfully"
    else:
        raise NotAuthorized()

@app.route('/read', methods=['GET'])
def read_employees():
    read()
    return "Read attempted."

@app.route('/delete', methods=['POST'])
def remove_employee():
    eID = request.form['eID']
    delete(eID)  # Pass the eID to the delete function
    return "Employee removed successfully"

if __name__ == '__main__':
    app.run(debug=True)