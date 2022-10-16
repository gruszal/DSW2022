# Zadanie - książka numerów telefonicznych

### Etap 2:
Wewnątrz skryptu stwórz funkcję `wczytaj_nowy_wpis()`, która będzie wczytywać z klawiatury dane do nowego wpisu, a następnie doda go do już istniejącej listy wpisów. Funkcja ma:
- Przyjmować jeden argument: `lista`, w którym przekazywać będziemy listę, do której funkcja będzie dodawać wpis.
- Wczyta z klawiatury imię oraz numer.
- Stworzy słownik analogiczny do tego w etapie 1 i doda go na koniec przekazanej w argumencie listy.

Wykorzystaj tę funkcję w skrypcie i zserializuj dwuelementową listę numerów do JSONa.

#### Rozszerzenie:
- Jeśli Użytkownik nie wpisał poprawnej liczby całkowitej jako numer, program ma poinformować Użytkownika o tym fakcie i nie dodawać niczego do listy, ale nie przerywać pracy całego programu.
