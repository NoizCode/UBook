from flask import Blueprint, render_template, flash, request, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['POST', 'GET'])
def login():
    pass

@auth.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already registered!", category="error")
        elif len(email) < 9:
            flash("Email too short!", category="error")
        elif len(firstName) < 3:
            flash("First name must be greater than 2 characters!", category="error")
        elif password1 != password2:
            flash("Passwords do not match!", category="error")
        elif len(password1) < 7:
            flash("Password must be greater than 6 characters!", category="error")
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)
