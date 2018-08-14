from flask import Flask,render_template
import os
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,create_engine
from pymongo import MongoClient
mongo = MongoClient('127.0.0.1',27017).challenge
app = Flask(__name__)

engine = create_engine('mysql://root:@localhost/challenge')



from datetime import datetime

app =Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/challenge'
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content =db.Column(db.Text)
    category = db.relationship('Category',backref=db.backref('files',lazy='dynamic'))
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
    
    def add_tag(self,tag_name):
        file_item = mongo.files.find_one({'file_id':self.id})
        if file_item:
            tags =file_item['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            mongo.files.update_one({'file_id':self.id},{'$set':{'tags':tags}})
        else:
            tags = [tag_name]
            mongo.files.insert_one({'file_id':self.id,'tags':tags})
        return tags

    

        
    def remove_tag(self,tag_name):
        file_item = mongo.files.find_one({'file_id':self.id})
        if file_item:
            tags = file_item['tags']
            try:
                new_tags = tags.remove(tag_name)
            except ValueError:
                return tags
            mongo.files.update_one({'file_id':self.id},{'$set':{'tags':new_tags}})
            return new_tags
        return []

    @property
    def tags(self):
        file_item = mongo.files.find_one({'file_id':self.id})
        if file_item:
            print(file_item)
            return file_item['tags']
        else:
            return []

    def __repr__(self):
        return '<File %r>' %self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<Category %r>'% self.name

@app.route('/')
def index():
    files = File.query.all()
    return render_template('index.html',files=files)



@app.errorhandler(404)
@app.route('/files/<file_id>')
def file(file_id):
    sql = 'select * from file where id = {}'.format(file_id)
        
    file_content = engine.execute(sql).fetchall()
    if file_content==[]:
        return render_template('404.html'),404
    else:
        return render_template("file.html", file_item = file_content) 

if __name__=='__main__':
    app.run()
