from flask import render_template, request, jsonify, redirect, url_for
from flask import Blueprint

mod = Blueprint('home', __name__)


@mod.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")
