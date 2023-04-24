import requests
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)


@app.route('/')
def propiedades():
    url = f'https://witei.com/api/v1/houses/'
    headers = {'Authorization': 'Bearer 7a54f9633cf443d988c0c49e2b77989b'}
    response = requests.get(url, headers=headers)
    data = response.json()
    propiedades_disponibles = [prop for prop in data['results'] if prop['status'] == 'disponible']
    return render_template('propiedades.html', propiedades=propiedades_disponibles)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
