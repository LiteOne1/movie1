
from flask import render_template, url_for
from app import app
from app.movie import get_synopsis, url, get_actors, get_name, url_imdb, imdb_rating, rotten_rating



@app.route('/')
@app.route('/index')
def index():
    synopsis = get_synopsis(url)
    movie_name = get_name(url)
    actors = get_actors(url)
    imdb_score = imdb_rating(url_imdb)
    rotten_score = rotten_rating(url)
    return render_template('index.html', synopsis = synopsis, name = movie_name, actors = actors, score = imdb_score, rotten_score = rotten_score)