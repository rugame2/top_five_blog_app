#Import the app variable from the init
from top_five_blog_app import app

#import specific packages from flask
from flask import render_template

#Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def testRoute():
    names = ['Adele','HER','Luther','Prince','Whitney']
    return render_template('test.html',list_names = names)