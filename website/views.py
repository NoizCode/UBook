from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Listing
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def home():
    all_listings = Listing.query.all()
    return render_template("home.html", listings=all_listings)

@views.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template("profile.html", user=current_user)
