from flask import Flask
import os
from flask import render_template, request,jsonify,redirect,url_for

template_dir = os.path.dirname(os.path.abspath(__file__));
print(template_dir)

template_dir = os.path.join(template_dir, 'views')
template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)


