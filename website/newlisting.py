from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user
from .models import User, Listing
from . import db

newlisting = Blueprint("newlisting", __name__) 

@newlisting.route("/newListing", methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        desc = request.form.get("author")

        if len(title) < 2:
            flash("Title is too short!", category="error")
        elif len(author) < 5:
            flash("Author name is too short!", category="error")
        elif len(desc) < 5:
            flash("Please provide a description!", category="error")
        else:
            new_listing = Listing(title=title, author=author, desc=desc)
            db.session.add(new_listing)
            db.session.commit()
            flash("New Listing added!")
            return redirect(url_for("views.home"))

    return render_template("newListing.html", user=current_user)
