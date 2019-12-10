from flask import Flask
import os
from controller import home

template_dir = os.path.dirname(os.path.abspath(__file__));
template_dir = os.path.join(template_dir, 'views')
template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)

app.register_blueprint(home.mod)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
