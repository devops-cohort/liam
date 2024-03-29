from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.models import shen_user, shen_gong
from application.forms import UpdateForm, RegistrationForm, LoginForm, UpdateAccountForm, DeleteForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
        form=DeleteForm
        postData = shen_gong.query.all()
        return render_template('home.html', title='Home', shenposts=postData)

@app.route('/login', methods=(['GET', 'POST']))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=shen_user.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=(['GET', 'POST']))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = shen_user(
            username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)




@app.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        postData = shen_gong(
            shen_name=form.shen_name.data,
            power_rating=form.power_rating.data,
            description=form.description.data,
            shen_user=current_user,
        )
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        print(form.errors)
    return render_template('update.html', title='Update', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
# <int:id> converts str to an int
# queries the database for the id then the try method deletes the correspnding record with the id
# then commits it and returns the user home
@login_required
def delete(id):
    shendelete = shen_gong.query.get(id)
    try:
        db.session.delete(shendelete)
        db.session.commit()
        return redirect(url_for('home'))
    except:
        return redirect(url_for('home'))
