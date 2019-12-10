from flask import render_template, request, jsonify, redirect, url_for
from flask import Blueprint
from model.images_model import ImagesModel
from model.entity.images import Images
import urllib.request
import uuid


mod = Blueprint('home', __name__)


@mod.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@mod.route('/add_image', methods=['POST'])
def add_image():
    # TODO add image
    if request.method == 'POST':
        url = request.form['image_url']
        if url:
            unique_filename = str(uuid.uuid4())
            urllib.request.urlretrieve(url, UPLOAD_IMG + "\\" + unique_filename)
            entity = Images(0,UPLOAD_IMG + "\\" + unique_filename, 0,1)
            img_model = ImagesModel()
            img_model.insert_by_entity(entity)

        # img_file = request.files['img_file']
        # if img_file:
        #     filename = secure_filename(img_file.filename)
        #     img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     img_url = '/uploads/' + filename
    return redirect('/')