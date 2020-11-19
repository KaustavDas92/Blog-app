from flask import Flask,render_template,session,redirect,request
from app import app
from Blog.models import Blogs
from functools import wraps

#decorator

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            return redirect('/')
        
    return wrap


@app.route('/blog/create')
@login_required
def createBlog():
    return render_template('addBlog.html')
@app.route('/blog/add', methods=['POST'])
def addBlog():
    return Blogs().createBlog()

@app.route('/blogs/<id>/update')
@login_required
def updateBlog(id):
     return Blogs().update(id)
@app.route('/blogs/<id>/edit', methods=['POST'])
def editBlog(id):
      return Blogs().editBlog(id)
@app.route('/blogs/<id>/delete')
def deleteBlog(id):
    return Blogs().deleteBlog(id)

@app.route('/blogs/view')
@login_required
def viewBlog():
    return Blogs().viewBlog(request.args['id'])    

@app.route('/blogs/comment/create', methods=['POST'])
def createComment():
    data=request.get_json()
    return Blogs().createComment(data)

@app.route('/blogs/comments', methods=['GET'])
def getComments():
    blogId=request.args['id']
    return Blogs().getComment(blogId)

@app.route('/blogs/comments/delete',methods=['DELETE'])
def deleteComment():
    commentId=request.args['id']
    return Blogs().deleteComment(commentId)

    
