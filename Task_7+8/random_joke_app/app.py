from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch a random joke from API
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    setup = data['setup']
    punchline = data['punchline']

    return render_template("index.html", setup=setup, punchline=punchline)

if __name__ == "__main__":
    app.run(debug=True)
