from flask.globals import request
from flask.templating import render_template
from main import app, render_template




@app.route('/')
def homepage():
    return render_template('/website/homepage.html')

@app.route('/about')
def about():
    return render_template('/website/about-us.html')

@app.route('/service')
def service():
    return render_template('/website/service-detail.html')

@app.route('/project')
def project():
    return render_template('/website/project-detail.html')

@app.route('/team')
def team():
    return render_template('/website/our-team.html')

@app.route('/blog')
def blog():
    return render_template('/website/blog.html')



# Admin Panel Routes
@app.route('/admin')
def admin():
    return render_template('/admin/index.html')

@app.route('/admin/change')
def admin_about():
    return render_template('/admin/page/change.html')

@app.route('/admin/form')
def admin_chage():
    return render_template('/admin/page/message.html')
