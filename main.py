from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # quote = None
    # if request.method == 'POST':
    quote = get_qoute()
    return render_template('index.html', quote=quote)

def get_qoute():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    quote = response.json()
    return quote

if __name__ == '__main__':
    app.run()