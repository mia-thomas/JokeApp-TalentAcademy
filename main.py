#!/Users/mia.thomas/.pyenv/shims/python

from flask import Flask, request, Response
import json

app = Flask(__name__)
import requests
# DATABASE

movie_db = {
    "1": { 'name': 'stargate', 'release_date': '1994' },
    "2": { 'name': 'Sunshine', 'release_date': '2007' },
    "3": { 'name': 'The Holiday', 'release_date': '2006' }
}

@app.route("/")
def hello():
    return 'Hello World'

@app.route("/movies")
def get_all_movies():
    return json.dumps(movie_db)

## READ
@app.route('/movie/<id>', methods=['GET'])
def get_movie(id):
    return json.dumps(movie_db[id])

if __name__ == "__main__":
    app.run(host='127.0.0.1')

@app.route(".movie/add", methods=['POST'])
def add_movie():
    req_data = requests.get_json()
    movie = req_data['movie']

    new_movie = { "4" : movie}
    movie_db.update(new_movie)
    return "Movie was added successfully"





