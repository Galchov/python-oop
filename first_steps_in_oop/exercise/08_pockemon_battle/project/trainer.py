from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for el in self.pokemons:
            if el.name == pokemon_name:
                self.pokemons.remove(el)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        pokemon_details = []
        for el in self.pokemons:
            pokemon_details.append(f"- {el.pokemon_details()}")
        details = "\n".join(pokemon_details)
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{details}"
