from sqlalchemy.orm import backref
from main import db

class Slider(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    content=db.Column(db.Text)
    image=db.Column(db.String(50))

class Services(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.column(db.String(50))
    content=db.Column(db.Text)
    icon=db.Column(db.String(50))

class Offer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    content=db.Column(db.Text)
    image=db.Column(db.String(100))
    read_more_url=db.Column(db.String(100))

class Team(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fullname=db.Column(db.String(50))
    duty=db.Column(db.String(50))
    image=db.Column(db.String(100))

class Tag(db.Model):
    __tablename__='Tag'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    blogs=db.relationship('Blog', backref='Tag')

class Blog(db.Model):
    __tablename__='Blog'
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50))
    image=db.Column(db.String(50))
    content=db.Column(db.Text)
    url=db.Column(db.String(50))
    post_date=db.column(db.String(50))
    tag_id=db.Column(db.Integer, db.ForeignKey('Tag.id'), nullable=False)

class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fullname=db.Column(db.String(50))
    email=db.Column(db.String(50))
    subject=db.Column(db.String(50))
    message=db.Column(db.Text)

class Project_Category(db.Model):
    __tablename__='Project_Category'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    projects=db.relationship('Project', backref='Project_Category')

class Project(db.Model):
    __tablename__='Project'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    company=db.Column(db.String(100))
    date=db.Column(db.String(50))
    image=db.Column(db.String(50))
    content=db.Column(db.String(200))
    url=db.Column(db.String(50))
    category_id=db.Column(db.Integer, db.ForeignKey('Project_Category.id'), nullable=False)

class About(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    content=db.Column(db.String(100))
    image=db.Column(db.String(50))

class Service_Detail(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50))
    content=db.Column(db.String(100))
    image=db.Column(db.String(50))

class Choose(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(100))
