from flask import Flask, render_template,session,redirect
from functools import wraps
import pymongo
app = Flask(__name__)
app.secret_key=b'\xc3\x86gcE\xb3\n\n\x8b\x1e\xa7\xc6\xe3\x99;\xe2'

#database

client=pymongo.MongoClient('localhost',27017)
db=client.BLOGS

#decorator

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            return redirect('/')
        
    return wrap
#Routes 

from user import routes
from Blog import routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    blogs=db.blogs.find({})
    return render_template('dashboard.html',Blogs=blogs)