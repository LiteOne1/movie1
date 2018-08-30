
from flask import render_template, url_for
from app import app
from app.movie import get_synopsis, url, get_name



@app.route('/')
@app.route('/index')
def index():
    synopsis = get_synopsis(url)
    movie_name = get_name(url)
    return render_template('index.html', synopsis = synopsis, name = movie_name)