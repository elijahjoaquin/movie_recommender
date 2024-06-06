from flask import Flask, render_template, request, jsonify
from scraper import get_movies_by_genre


app = Flask(__name__, template_folder='templates', static_folder='css')

# Home route to display the genre selection form
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    genre = request.form['genre']
    movie = get_movies_by_genre(genre)
    return jsonify(movie)

if __name__ == '__main__':
    app.run(debug=True)