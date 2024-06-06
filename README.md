# Pokemon_PPY
# Imie, Nazwisko oraz album
Przemysław Karczmarczyk
s24639

# Opis Projektu
Projekt gry Pokémon w Pythonie, który symuluje walki Pokémonów z różnymi statystykami i typami. Gra pozwala graczowi wybrać swoje Pokemony, a następnie walczyć przeciwko losowo wybranym Pokémonom przeciwnika. Każdy Pokémon ma swoje statystyki: HP, atak, obrona oraz typ (ogień, woda, powietrze, ziemia), które wpływają na efektywność ataków.

# Pliki w Projekcie
main.py: Główny skrypt uruchamiający grę i obsługujący interakcje gracza.

#Instrukcja Obsługi

Uruchom main.py:
Po uruchomieniu, zobaczysz menu, które pozwoli Ci wybrać swoje Pokemony do walki oraz rozpocząć bitwę.

# Opcje Gry
Wybór Pokémonów: Gracz wybiera trzy Pokemony z dostępnej listy.
Walka: Gracz wybiera Pokémona do walki, a przeciwnikowi losuje się Pokémon do walki. Bitwa toczy się, aż wszystkie Pokemony jednej ze stron zostaną pokonane.

# Przykładowe Uruchomienie
Uruchom grę wybierając swoje Pokemony z listy.
Wybierz Pokémona do walki, gdy gra poprosi o wybór.
Śledź postęp bitwy, obserwując zaktualizowane HP Pokémonów po każdej rundzie.
Kontynuuj walkę, aż wszystkie Pokemony jednej ze stron zostaną pokonane.

# Wymagania
Python 3.x

# Struktura Kodu
main.py

# Opis Funkcjonalności
main.py
choose_player_pokemons(pokemons, n=3)

Pozwala graczowi wybrać trzy Pokemony z dostępnej listy.
Wyświetla listę dostępnych Pokémonów i pozwala graczowi wybrać numerycznie.
Zwraca listę wybranych Pokémonów.

choose_pokemon(player_pokemons)

Pozwala graczowi wybrać Pokémona do walki spośród wybranych Pokémonów.
Wyświetla listę wybranych Pokémonów i pozwala graczowi wybrać numerycznie.
Zwraca wybranego Pokémona.

calculate_damage(attacker, defender)

Oblicza obrażenia zadane przez atakującego Pokémona obrońcy.
Uwzględnia statystyki ataku i obrony oraz modyfikatory typów.
Zwraca obliczoną wartość obrażeń.

battle(pokemon1, pokemon2)

Symuluje walkę między dwoma Pokémonami.
Oblicza obrażenia zadane przez obie strony.
Aktualizuje HP obu Pokémonów po ataku.
Wyświetla wynik walki w konsoli.

is_alive(pokemon)

Sprawdza, czy dany Pokémon jest jeszcze żywy (ma więcej niż 0 HP).
Zwraca True, jeśli Pokémon jest żywy, w przeciwnym razie False.
display_opponent_pokemons(opponent_pokemons)

Wyświetla aktualny stan (HP) Pokémonów przeciwnika.
Pozwala graczowi zobaczyć, które Pokemony przeciwnika są nadal aktywne.

game(player_pokemons, opponent_pokemons)

Uruchamia pełną rozgrywkę między Pokémonami gracza a Pokémonami przeciwnika.
Powtarza rundy walki, dopóki jedna ze stron nie zostanie pokonana.
Wyświetla wynik walki i stan Pokémonów po każdej rundzie.
Ogłasza zwycięzcę po zakończeniu gry.

# Klasa reprezentująca Pokémona.
init(self, name, hp, attack, defense, type)
Inicjalizuje Pokémona z zadanymi statystykami (HP, atak, obrona) i typem.
repr(self)
Zwraca reprezentację tekstową Pokémona, zawierającą jego nazwę, HP, atak, obronę i typ.
