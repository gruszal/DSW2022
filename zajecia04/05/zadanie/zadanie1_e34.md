# Zadanie 1 - plecak harcerza

Rozbudowanie klasy `Plecak`.

## Etap 3:
- Klasa `Plecak` ma posiadać jeszcze jeden atrybut `zawartosc`. Zmodyfikuj inicjalizator tak, aby przy tworzeniu nowego obiektu klasy `Plecak`, obiekt rozpoczynał życie z atrybutem `zawartosc` ustawionym na pustą listę.
- Napisz metodę `dodaj_przedmiot`, która będzie przyjmować jeden parametr: string `przedmiot`. Wywołanie tej metody będzie powodować dodanie tego stringa do listy `zawartosc`.
- Przetestuj działanie tej metody w następujący sposób:
    - Stwórz obiekt `p1` klasy `Plecak`
    - Podejrzyj zawartość plecaka odwołując się bezpośrednio do atrybutu: `p1.zawartosc`
    - Użyj metody `dodaj_przedmiot` aby wrzucić przedmiot `'konserwa'` do plecaka.
    - Ponownie sprawdź zawartość plecaka

## Etap 4:
- Napisz metodę `ile_przedmiotow`, która zwracać będzie liczbę przedmiotów w plecaku.
- Przetestuj działanie tej metody:
    - Tak jak powyżej, dodaj jeszcze kilka przedmiotów do plecaka.
    - Wywołaj metodę `ile_przedmiotow` i zapisz jej wynik do zmiennej.
    - Wypisz na ekranie komunikat: "W plecaku znajduje się (ilość) przedmiotów."
