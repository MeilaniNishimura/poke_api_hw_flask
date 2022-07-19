from flask import render_template, request, redirect, url_for, flash
from . import bp as app
from app.blueprints.main.models import User
from flask_login import login_user, logout_user
from app import db


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form['inputEmail']).first()

        if user is None:
            flash(f'User with email { request.form["emailInput"] } does not exist.', 'danger')
        elif not user.check_my_password(request.form['inputPassword']):
            flash('Password is incorrect', 'danger')
        else:
            login_user(user)
            flash("User logged in successfully", 'success')
            return redirect(url_for('main.home'))

        return render_template('login.html')
    else:
        return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        check_user = User.query.filter_by(email=request.form['emailInput']).first()

        if check_user is not None:
            flash('Error, user already exists', 'danger')
        else:
            if request.form['passwordInput'] == request.form['inputPasswordConfirm']:
                new_user = User(
                    email=request.form['emailInput'],
                    password='',
                    username=request.form['usernameInput'],
                    first_name=request.form['first_nameInput'],
                    last_name = request.form['last_nameInput']
                )
                new_user.hash_my_password(request.form['passwordInput'])
                db.session.add(new_user)
                db.session.commit()
                flash('User created successfully, please login', 'success')
                return redirect(url_for('auth.login'))
            else:
                flash('Error, passwords do not match', 'danger')

        return render_template('register.html')
    else:
        return render_template('register.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))