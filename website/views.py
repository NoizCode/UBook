from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Listing
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def home():
    return render_template("home.html", user=current_user)
