from src.classes.pokemon import Pokemon
from src.dao.pokemon_dao import PokemonDAO
from src.bd.bd_connection import bd
from flask import Flask





pokemon_1 = Pokemon(1, "planta", "Bulbasaur")
pokemon_1_dao = PokemonDAO(pokemon_1)
bd.insert_in_BD(pokemon_1_dao._pokemon_json)

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return ''' <html>'
        <center>Eu estou online! - Hello Worl<center/>
    </html>'''

if __name__== '__main__':
    app.run(debug=True, host="0.0.0.0.", port="3001")

app = Flask('flaskconftest')

app.run()

    
    
