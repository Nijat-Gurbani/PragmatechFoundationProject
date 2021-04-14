from flask.signals import request_finished
from main import db,app, render_template, request, redirect, desc, url_for
from werkzeug.utils import secure_filename
from main.models import *
import os

@app.route('/admin')
def admin():
    return render_template('/admin/index.html')

@app.route('/admin/change')
def change():
    return render_template('/admin/change.html')
    
@app.route('/admin/slider')
def slider():   
    from main.models import Slider
    slides=Slider.query.all()
    return render_template('/admin/slider.html', sliders=slides)

@app.route('/admin/service')
def services():
    return render_template('/admin/service.html')

@app.route('/admin/offer')
def offer():
    from main.models import Offer
    offers=Offer.query.all()
    return render_template('/admin/offer.html', all_offer=offers)

@app.route('/admin/tag')
def tag():
    from main.models import Tag
    tags=Tag.query.all()
    return render_template('/admin/tag.html', all_tag=tags)

@app.route('/admin/team')
def team():
    from main.models import Team
    teams=Team.query.all()
    return render_template('/admin/team.html', all_team_user=teams)

@app.route('/admin/blog')
def blog_post():
    tags=Tag.query.all()
    blogs=Blog.query.all()
    return render_template('/admin/blog.html', all_blog=blogs, all_tag=tags)

@app.route('/admin/message')
def message():
    data=Message.query.order_by(desc(Message.id))
    return render_template('/admin/message.html', data=data)
@app.route('/admin/message/<id>')
def post(id):
    data=Message.query.filter_by(id=id).first()
    return render_template('/admin/post.html', data=data)

@app.route('/website/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        data=Message(
            fullname=request.form['fullname'],
            email=request.form['email'],
            subject=request.form['subject'],
            message=request.form['message']
        )
        db.session.add(data)
        db.session.commit()
        return redirect('/')
    return render_template('contact.html')

@app.route('/admin/project_category')
def category():
    category=Project_Category.query.all()
    return render_template('/admin/project_category.html', all_category=category)

@app.route('/admin/project')
def projects():
    project=Project.query.all()
    return render_template('/admin/project.html',all_project=project)





# ADD

photo_index=0   
# ADD Slider
@app.route('/admin/slider/add_slider', methods=['GET', 'POST'])
def add_slider():
    from main.models import Slider
    if request.method == "POST":
        global photo_index
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{request.form['title'][0:3]}_{photo_index}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_PATH'], newName))
        photo_index+=1
        slide=Slider(
                title=request.form['title'],
                content=request.form['content'],
                image=newName
        )
        db.session.add(slide)
        db.session.commit()
        return redirect('/admin/slider')
    return render_template('/admin/add_slider.html')

# ADD SERVICE
@app.route('/admin/service/add_service')
def add_service():
    return render_template('/admin/add_service.html')

# ADD OFFER
@app.route('/admin/offer/add_offer', methods=['GET', 'POST'])
def add_offer():
    from main.models import Offer
    if request.method == "POST":
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        new_offer=Offer(
            title=request.form['title'],
            content=request.form['content'],
            image=filename
        )
        db.session.add(new_offer)
        db.session.commit()
        return redirect('/admin/offer')
    return render_template('/admin/add_offer.html')

# ADD Tag
@app.route('/admin/tag/add_tag', methods=['GET', 'POST'])
def add_tag():
    if request.method == 'POST':
        new_tag=Tag(
            name=request.form['name']
        )
        db.session.add(new_tag)
        db.session.commit()
        return redirect('/admin/tag')
    return render_template('/admin/add_tag.html')

# ADD Team
@app.route('/admin/team/add_team', methods=['GET', 'POST'])
def add_team():
    from main.models import Team
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        new_team_user=Team(
            fullname=request.form['fullname'],
            duty=request.form['duty'],
            image=filename
        )
        db.session.add(new_team_user)
        db.session.commit()
        return redirect('/admin/team')
    return render_template('/admin/add_team.html')

# ADD Blog
@app.route('/admin/blog/add_blog', methods=['GET', 'POST'])
def add_blog():
    tags=Tag.query.all()
    blogs=Blog.query.all()
    if request.method == "POST"  and request.form['title']!='' and request.form['content'] and request.files['image'] and request.form['tag']!='' and request.form['time'] !='':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        new_blog = Blog(
            title=request.form['title'],
            content=request.form['content'],
            image=filename,
            post_date=request.form['time'],
            tag_id=request.form['tag']
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('/admin/add_blog.html', all_tag=tags, all_blog=blogs)

# Add Project_Category
@app.route('/admin/project_category/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == "POST":
        new_category=Project_Category(
            name=request.form['name']
        )
        db.session.add(new_category)
        db.session.commit()
        return redirect('/admin/project_category')
    return render_template('/admin/add_category.html')
# Add Project
@app.route('/admin/project/add_project', methods=['GET', 'POST'])
def add_project():
    categorys=Project_Category.query.all()
    projects=Project.query.all()
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        new_project=Project(
            name=request.form['name'],
            company=request.form['company'],
            date=request.form['time'],
            image=filename,
            content=request.form['content'],
            url=request.form['url'],
            category_id=request.form['category']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect('/admin/project')
    return render_template('/admin/add_project.html', all_category=categorys, all_project=projects)


# DELETE

# Delete Slider
@app.route("/admin/slider/delete/<id>")
def delete_slider(id):
    from main.models import Slider
    SlideForDelete = Slider.query.get(id)
    db.session.delete(SlideForDelete)
    db.session.commit()
    return redirect('/admin/slider')

# Delete Offer
@app.route('/admin/offer/delete/<id>')
def delete_offer(id):
    from main.models import Offer
    OfferForDelete = Offer.query.get(id)
    db.session.delete(OfferForDelete)
    db.session.commit()
    return redirect('/admin/offer')

# Delete Tag
@app.route('/admin/tag/delete/<id>')
def delete_tag(id):
    from main.models import Tag
    TagForDelete = Tag.query.get(id)
    db.session.delete(TagForDelete)
    db.session.commit()
    return redirect('/admin/tag')

# Delete Team
@app.route('/admin/team/delete/<id>')
def delete_team(id):
    from main.models import Team
    TeamForDelete = Team.query.get(id)
    db.session.delete(TeamForDelete)
    db.session.commit()
    return redirect('/admin/team')

# Delete Blog
@app.route('/admin/blog/delete/<id>')
def delete_blog(id):
    from main.models import Blog
    BlogForDelete = Blog.query.get(id)
    db.session.delete(BlogForDelete)
    db.session.commit()
    return redirect('/admin/blog')

# Delete Message
@app.route('/admin/message/delete/<id>')
def delete_message(id):
    MessageForDelete=Message.query.get(id)
    db.session.delete(MessageForDelete)
    db.session.commit()
    return redirect('/admin/message')

# Delete Project
@app.route('/admin/project/delete/<id>')
def delete_project(id):
    ProjectForDelete=Project.query.get(id)
    db.session.delete(ProjectForDelete)
    db.session.commit()
    return redirect('/admin/project')

# Delete Project Category
@app.route('/admin/project_category/delete/<id>')
def delete_category(id):
    CategoryForDelete=Project_Category.query.get(id)
    db.session.delete(CategoryForDelete)
    db.session.commit()
    return redirect('/admin/project_category')

# UPDATE

# Update Slider
@app.route("/admin/slider/update/<id>", methods=['GET', 'POST'])
def update_slider(id):
    from main import db,app
    from main.models import Slider
    SlideForUpdate=Slider.query.get(id)
    if request.method == "POST":
        global photo_index
        file = request.files['image']
        filename = secure_filename(file.filename)
        newName = f"photo_{request.form['title'][0:3]}_{photo_index}.{filename.split('.')[-1]}"
        file.save(os.path.join(app.config['UPLOAD_PATH'], newName))
        photo_index+=1
        title = request.form['title']
        content = request.form['content']
        SlideForUpdate.title = title
        SlideForUpdate.content = content
        SlideForUpdate.image = newName
        db.session.commit()
        return redirect('/admin/slider')
    return render_template('/admin/update_slide.html',sliderss=SlideForUpdate)

# Update Offer
@app.route('/admin/offer/update/<id>', methods=['GET', 'POST'])
def update_offer(id):
    from main.models import Offer
    OfferForUpdate=Offer.query.get(id)
    if request.method == "POST":
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        title = request.form['title']
        content = request.form['content']
        OfferForUpdate.title = title
        OfferForUpdate.content = content
        OfferForUpdate.image = filename
        db.session.commit()
        return redirect('/admin/offer')
    return render_template('/admin/update_offer.html', offer=OfferForUpdate)

# Update Tag
@app.route('/admin/tag/update/<id>', methods=['GET', 'POST'])
def update_tag(id):
    from main.models import Tag
    TagForUpdate = Tag.query.get(id)
    if request.method == 'POST':
        name = request.form['name']
        TagForUpdate.name = name
        db.session.commit()
        return redirect('/admin/tag')
    return render_template('/admin/update_tag.html', tag=TagForUpdate)

# Update Team
@app.route('/admin/team/update/<id>', methods=['GET', 'POST'])
def update_team(id):
    from main.models import Team
    TeamForUpdate = Team.query.get(id)
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        fulname = request.form['fullname']
        duty = request.form['duty']
        TeamForUpdate.fullname = fulname
        TeamForUpdate.duty = duty
        TeamForUpdate.image = filename
        db.session.commit()
        return redirect('/admin/team')
    return render_template('/admin/update_team.html', user=TeamForUpdate)


# Update Blog
@app.route('/admin/blog/update/<id>', methods=['GET', 'POST'])
def update_blog(id):
    from main.models import Blog
    BlogForUpdate=Blog.query.get(id)
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        title=request.form['title']
        content=request.form['content']
        post_date=request.form['time']
        BlogForUpdate.title=title
        BlogForUpdate.content=content
        BlogForUpdate.image=filename
        BlogForUpdate.post_date=post_date
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('/admin/update_blog.html', blog=BlogForUpdate)

# Update Project
@app.route('/admin/project/update/<id>', methods=['GET', 'POST'])
def update_project(id):
    categorys=Project_Category.query.all()
    ProjectForUpdate=Project.query.filter_by(id=id).first()
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        ProjectForUpdate.name=request.form['name']
        ProjectForUpdate.company=request.form['company']
        ProjectForUpdate.date=request.form['time']
        ProjectForUpdate.image=filename
        ProjectForUpdate.url=request.form['url']
        ProjectForUpdate.content=request.form['content']
        ProjectForUpdate.category_id=request.form['category']
        db.session.commit()
        return redirect('/admin/project')
    return render_template('/admin/update_project.html', project=ProjectForUpdate, category=categorys)


# Update Project Category
@app.route('/admin/project_category/update/<id>', methods=['GET', 'POST'])
def update_project_category(id):
    CategoryForUpdate=Project_Category.query.get(id)
    if request.method == 'POST':
        name = request.form['name']
        CategoryForUpdate.name=name
        db.session.commit()
        return redirect('/admin/project_category')
    return render_template('/admin/update_category.html', category=CategoryForUpdate)







