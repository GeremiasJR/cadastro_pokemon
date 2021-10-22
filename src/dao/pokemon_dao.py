class PokemonDAO():
    def __init__(self, instancia_pokemon):
        self._pokemon_json = {}
        self.preenche_valores_json(instancia_pokemon)
    
    def preenche_valores_json(self, instancia):
        self._pokemon_json['id']   = instancia.id
        self._pokemon_json['tipo'] = instancia.tipo
        self._pokemon_json['nome'] = instancia.nome


    def __str__(self):
        return str(self._pokemon_json)
        