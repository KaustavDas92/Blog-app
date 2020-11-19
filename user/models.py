from flask import Flask,jsonify,request,session,render_template,redirect
# from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class Users:

    def start_session(self,user):
        del user['password']
        session['logged_in']=True
        session['user']=user
        # return jsonify(session),200
    def signup(self):
        user={
            "_id":uuid.uuid4().hex,
            "name":request.form.get('name'),
            "role":request.form.get('role'),
            "email":request.form.get('email'),
            "password":request.form.get('password')
        }
        # user['password']=pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({'email':user['email']}):
            return jsonify({'error':' email address is already in use'}),400
        db.users.insert_one(user)
        self.start_session(user)
        return redirect('/dashboard/')
    def login(self):
        user=db.users.find_one({
            'email':request.form.get('email'),
            'password':request.form.get('password')
            })
        if user:
            
            self.start_session(user)
            return redirect('/dashboard')
        else :
            return redirect('/')
    def signout(self):
        session.clear()
        return redirect('/')