from flask import Flask, request, Response, render_template
import json
import random

app = Flask(__name__)


joke_db = {
    "1": { 'joke': 'My wife told me to stop acting like a flamingo.', 'punchline': 'I had to put my foot down.' },
    "2": { 'joke': 'Why did David Hasselhoff change his name to The Hoff?', 'punchline': 'Its less hassle!' },
    "3": { 'joke': 'Why did the chicken go to prison?', 'punchline': 'Crimes.'},
    "4": { 'joke': 'What do you do when your hot pants catch on fire?', 'punchline': 'Put them out with your pantyhose.' },
    "5": { 'joke': 'What do you call a sad cup of coffee?', 'punchline': 'Depresso.' },
    "6": { 'joke': 'What did one nut say when it was chasing the other nut?', 'punchline': 'Im a cashew' }
}

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/joke_link")
def joke_link():
    html_response = random.choice(list(joke_db.values()))
    print ('I got clicked!')
    return html_response, 'Click'

if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
     app.run(host='127.0.0.1')

### new movie
# { "movie" : { "name" : "The Matrix", "release_date" : "1999"} }






# READ      - GET
# UPDATE    - PUT
# DELETE    - GET