import random

# Definicja klasy Pokémon
class Pokemon:
    def __init__(self, name, hp, attack, defense, type):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.type = type

    def __repr__(self):
        return f"{self.name} (HP: {self.hp}, Atk: {self.attack}, Def: {self.defense}, Type: {self.type})"

# Lista Pokémonów
pokemons = [
    Pokemon("Charizard", 78, 84, 78, "Fire"),
    Pokemon("Blastoise", 79, 83, 100, "Water"),
    Pokemon("Venusaur", 80, 82, 83, "Earth"),
    Pokemon("Pikachu", 35, 55, 40, "Air"),
    Pokemon("Arcanine", 90, 110, 80, "Fire"),
    Pokemon("Gyarados", 95, 125, 79, "Water"),
    Pokemon("Aerodactyl", 80, 105, 65, "Air"),
    Pokemon("Rhydon", 105, 130, 120, "Earth"),
    Pokemon("Vaporeon", 130, 65, 60, "Water"),
    Pokemon("Moltres", 90, 100, 90, "Fire")
]

# Typy i ich modyfikatory
type_effectiveness = {
    "Fire": {"Water": 0.8, "Earth": 1.2, "Air": 1.0, "Fire": 1.0},
    "Water": {"Fire": 1.2, "Earth": 1.0, "Air": 1.0, "Water": 1.0},
    "Earth": {"Fire": 0.8, "Water": 1.0, "Air": 1.2, "Earth": 1.0},
    "Air": {"Fire": 1.0, "Water": 1.0, "Earth": 0.8, "Air": 1.0}
}

# Funkcja do wybierania Pokémonów przez gracza
def choose_player_pokemons(pokemons, n=3):
    chosen_pokemons = []
    available_pokemons = pokemons.copy()
    for _ in range(n):
        print("Wybierz swojego Pokémona:")
        for i, pokemon in enumerate(available_pokemons):
            print(f"{i + 1}. {pokemon}")
        choice = int(input("Podaj numer Pokémona: ")) - 1
        chosen_pokemon = available_pokemons.pop(choice)
        chosen_pokemons.append(chosen_pokemon)
    return chosen_pokemons

# Funkcja do wyboru Pokémona przez gracza w czasie walki
def choose_pokemon(player_pokemons):
    print("Wybierz swojego Pokémona do walki:")
    for i, pokemon in enumerate(player_pokemons):
        print(f"{i + 1}. {pokemon}")
    choice = int(input("Podaj numer Pokémona: ")) - 1
    return player_pokemons[choice]

# Funkcja do obliczania obrażeń
def calculate_damage(attacker, defender):
    base_damage = attacker.attack - defender.defense
    type_modifier = type_effectiveness[attacker.type][defender.type]
    return max(0, base_damage * type_modifier)

# Funkcja walki
def battle(pokemon1, pokemon2):
    print(f"\n{pokemon1.name} walczy z {pokemon2.name}!")
    damage_to_2 = calculate_damage(pokemon1, pokemon2)
    damage_to_1 = calculate_damage(pokemon2, pokemon1)
    print(f"{pokemon1.name} zadaje {damage_to_2:.2f} obrażeń {pokemon2.name}!")
    print(f"{pokemon2.name} zadaje {damage_to_1:.2f} obrażeń {pokemon1.name}!")
    pokemon1.hp -= damage_to_1
    pokemon2.hp -= damage_to_2
    print(f"{pokemon1.name} HP: {pokemon1.hp}")
    print(f"{pokemon2.name} HP: {pokemon2.hp}")

# Funkcja do sprawdzania czy Pokémon jest żywy
def is_alive(pokemon):
    return pokemon.hp > 0

# Funkcja do wyświetlania aktualnego stanu Pokémonów przeciwnika
def display_opponent_pokemons(opponent_pokemons):
    print("\nPokemony przeciwnika:")
    for pokemon in opponent_pokemons:
        print(f"{pokemon.name} (HP: {pokemon.hp})")

# Pełna rozgrywka
def game(player_pokemons, opponent_pokemons):
    while player_pokemons and opponent_pokemons:
        player_pokemon = choose_pokemon(player_pokemons)
        opponent_pokemon = random.choice(opponent_pokemons)
        print(f"Przeciwnik wybrał {opponent_pokemon.name}!")
        battle(player_pokemon, opponent_pokemon)

        if not is_alive(player_pokemon):
            print(f"{player_pokemon.name} został pokonany!")
            player_pokemons.remove(player_pokemon)
        if not is_alive(opponent_pokemon):
            print(f"{opponent_pokemon.name} został pokonany!")
            opponent_pokemons.remove(opponent_pokemon)

        display_opponent_pokemons(opponent_pokemons)

    if player_pokemons:
        print("Gratulacje! Wygrałeś!")
    else:
        print("Przegrałeś! Spróbuj ponownie!")

# Gracz wybiera swoje Pokemony
player_pokemons = choose_player_pokemons(pokemons)

# Przeciwnikowi losują się Pokemony
opponent_pokemons = random.sample(pokemons, 3)

print("\nTwoje Pokemony:", player_pokemons)
print("Pokemony przeciwnika:")
for pokemon in opponent_pokemons:
    print(f"{pokemon.name} (HP: {pokemon.hp}) (Atk: {pokemon.attack}) (Type: {pokemon.type})")

# Uruchomienie gry
game(player_pokemons, opponent_pokemons)
