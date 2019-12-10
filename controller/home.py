from flask import render_template, request, jsonify, redirect, url_for
from flask import Blueprint
from model.images_model import ImagesModel
from model.entity.images import Images
from model.db_helper.mysql_connection import *
import urllib.request
import uuid


mod = Blueprint('home', __name__)


@mod.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

UPLOAD_IMG_FOLDER = "/static/images/"
@mod.route('/add_image', methods=['POST'])
def add_image():
    # TODO add image
    if request.method == 'POST':
        url = request.form['image_url']
        if url:
            unique_filename = str(uuid.uuid4())
            urllib.request.urlretrieve(url, unique_filename+".jpg")
            entity = Images(0,unique_filename+".jpg", 0,1)
            with MySQLConnection as mysql_con:
                img_model = ImagesModel(mysql_con)
                img_model.insert_by_entity(entity)

        # img_file = request.files['img_file']
        # if img_file:
        #     filename = secure_filename(img_file.filename)
        #     img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     img_url = '/uploads/' + filename
    return redirect('/')