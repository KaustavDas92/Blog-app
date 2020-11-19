from flask import Flask
from app import app
from user.models import Users

@app.route('/user/signup', methods=['POST'])
def signup():
    return Users().signup()
@app.route('/user/login', methods=['POST'])
def login():
    return Users().login()
@app.route('/user/signout')
def signout():
    return Users().signout()