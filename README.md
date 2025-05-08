# Employee Management System (Web 2 & Web 3)

This repository contains a **bare-bones employee management system** designed for both traditional Web 2 applications and future Web 3 implementations. The current version is built using **Flask** for backend management, with **cookie-based authentication** and structured database operations. The next version will extend this functionality by implementing smart contracts in **Solidity**, allowing decentralized management on the Ethereum blockchain.

## Features

- **Database Configurations:** Centralized configurations are stored in `config.py` for ease of setup.
- **SQL Queries:** Defined separately in individual Python files located in the `database` folder to maintain modularity.
- **Cookie-Based Authentication:** A simple authentication system where user credentials are stored in cookies for session management.

## Code Overview

The Flask application provides essential employee management functionality, including user authentication and CRUD operations. Below is an explanation of key parts of the code:

### Authentication System
The system implements a basic authentication mechanism where an admin logs in using predefined credentials. Cookies store the user's session details to allow seamless navigation.

```python
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
```

### Employee Data Management
The system enables adding, reading, and deleting employees from the database while enforcing role-based authorization.

#### Insert Employee:
```python
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
```
Employees can only be added by users belonging to the **MGMT (management) role**, ensuring restricted access.

#### Read Employee Data:
```python
@app.route('/read', methods=['GET'])
def read_employees():
    read()
    return "Read attempted."
```
Retrieves and displays stored employee data.

#### Delete Employee:
```python
@app.route('/delete', methods=['POST'])
def remove_employee():
    eID = request.form['eID']
    delete(eID)
    return "Employee removed successfully"
```
Allows authorized deletion of employees from the database.

## Future Development (Web 3 Integration)
The next version of this system will transition from a centralized approach to a decentralized framework using **Solidity smart contracts** on the Ethereum blockchain. The aim is to provide:

- **Tamper-proof employee records** stored on-chain.
- **Decentralized authentication mechanisms** using wallets instead of cookies.
- **Permission-based role assignment** enforced through smart contracts.

The Web 3 upgrade will enhance security, transparency, and decentralization in employee management, ensuring that all transactions are **verifiable and immutable** within the Ethereum ecosystem.
