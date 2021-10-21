from src.classes.pokemon import Pokemon
from src.dao.pokemon_dao import PokemonDAO
from src.bd.bd_connection import bd

pokemon_1 = Pokemon(1, "planta", "Bulbasaur")
pokemon_1_dao = PokemonDAO(pokemon_1)
bd.insert_in_BD(pokemon_1_dao._pokemon_json)