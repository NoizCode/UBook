from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from .models import User, Listing
from . import db

newlisting = Blueprint("newlisting", __name__) 

@newlisting.route("/newListing", methods=['POST', 'GET'])
@login_required
def new():
    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        image_url = request.form.get("image")
        price = request.form.get("price")
        desc = request.form.get("desc")

        if len(title) < 2:
            flash("Title is too short!", category="error")
        elif len(author) < 5:
            flash("Author name is too short!", category="error")
        elif len(desc) < 5:
            flash("Please provide a description!", category="error")
        elif len(price) < 1:
            flash("Please provide a price!", category="error")
        elif len(image_url) < 3:
            flash("Please provide an image!", category="error")
        else:
            new_listing = Listing(title=title, author=author, image_url=image_url, price=price, desc=desc)
            db.session.add(new_listing)
            db.session.commit()
            flash("New Listing added!", category="success")
            return redirect(url_for("views.home"))

    return render_template("newListing.html", user=current_user)
