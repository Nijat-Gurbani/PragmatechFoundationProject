from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_migrate import Migrate
import os

upload_folder = 'main/static/uploads'
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['UPLOAD_PATH']=upload_folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


@app.route('/')
def homepage():
    from main.models import Slider, Team, Project_Category, Project, Blog, Choose
    category=Project_Category.query.all()
    project=Project.query.all()
    team=Team.query.all()
    slider=Slider.query.all()
    blog=Blog.query.all()
    choose=Choose.query.all()
    return render_template('/website/homepage.html', sliders=slider, teams=team, categories=category, projects=project, blogs=blog, chooses=choose)

@app.route('/blog')
def blog():
    return render_template('/website/blog_single.html')

@app.route('/blog/detail/<id>')
def blog_detail(id):
    from main.models import Blog, Tag
    blog=Blog.query.get(id)
    tag=Tag.query.all()
    return render_template('/website/blog_single.html', blog=blog, tags=tag)

@app.route('/about')
def about():
    from main.models import About
    about=About.query.all()
    return render_template('/website/about-us.html', abouts=about)


@app.route('/service')
def service_details():
    from main.models import Service_Detail
    service=Service_Detail.query.all()
    return render_template('/website/service-detail.html', services=service)

@app.route('/project/detail/<id>')
def project(id):
    from main.models import Slider, Team, Project_Category, Project
    category=Project_Category.query.all()
    project=Project.query.get(id)
    return render_template('/website/project-detail.html', categories=category, project=project)

@app.route('/choose')
def choose():
    from main.models import Choose
    choose=Choose.query.all()
    return render_template('/website/choose.html', chooses=choose)


db=SQLAlchemy(app)
migrate=Migrate(app,db)


from admin import routes


