from flask import Flask,jsonify,request,session,render_template,redirect,make_response
from datetime import datetime
from app import db
import uuid

class Blogs:
    def createBlog(self):
        
        blog={
            '_id':uuid.uuid4().hex,
            'title': request.form.get('title'),
            'body': request.form.get('body'),
            'author': session['user']['name'],
            'authorId':session['user']['_id'],
            'created_at':datetime.now()
        }
        db.blogs.insert_one(blog)
        return redirect('/dashboard')
    
    def update(self,id):
        blog=db.blogs.find_one({'_id':id})
        return render_template('editBlog.html',Blog=blog)
   
    def editBlog(self,id):
        newBlog={
            '$set':{
                'title': request.form.get('title'),
                'body': request.form.get('body')
            }     
        }

        db.blogs.update_one({'_id':id},newBlog)
        return redirect('/dashboard')
    
    def deleteBlog(self,id):
        db.blogs.delete_one({'_id':id})
        return redirect('/dashboard')
    
    def viewBlog(self,id):
         blog=db.blogs.find_one({'_id':id})
         return render_template('viewBlog.html',Blog=blog)
    def createComment(self,data):
        record={
            '_id':uuid.uuid4().hex,
            'message':data['comment'],
            'userId':data['userId'],
            'blogId': data['blogId'],
            'created_at':datetime.now()
        }

        db.comments.insert_one(record)

        user=db.users.find_one({'_id':data['userId']})
        return make_response(jsonify({'user':user['name'],'blogId': data['blogId'],'message':data['comment']})) 
    
    def getComment(self,id):
       allComments= db.comments.find({'blogId':id})
       blog=db.blogs.find_one({'_id':id})
       commentList=[]
       for record in allComments:
           user=db.users.find_one({'_id':record['userId']})
           comm={
               'id':record['_id'],
               'message':record['message'],
               'commentedUsername':user['name'],
               'commentedUserId':user['_id'],
               'blogAuthorId':blog['authorId']

           }
           commentList.append(comm)
       return make_response(jsonify(commentList))
    
    def deleteComment(self,id):
        db.comments.delete_one({'_id':id})
        return make_response(jsonify({'response':'success'}))