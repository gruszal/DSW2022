# Zadanie 1 - plecak harcerza

## Etap 1:

- Napisz klasę `Plecak`, która zamodeluje plecak harcerza.
- Napisz inicjalizator klasy `Plecak`, który ustawi obiektowi poniższe atrybuty:
    - Atrybut `pojemnosc`, ma być ustawiany na wartość przekazaną do inicjalizatora w parametrze. Atrybut ten ma być typu `int`.
    - Atrybut `kolor`, ma być zawsze ustawiony na wartość 'zielony' (jak to u harcerzy ;).
- Napisz metodę `__str__`, która spowoduje, że obiekty klasy `Plecak` będą opisywane/reprezentowane poniższym komunikatem:
> 'Plecak koloru (tutaj kolor) ma pojemność (tutaj pojemność)l'

## Etap 2:

- Stwórz obiekt `p1` klasy `Plecak` o pojemności 30l.
- Wydrukuj na ekranie reprezentację słowną obiektu `p1`.
- Stwórz obiekt `p2` klasy `Plecak o pojemności 45l.
- Harcerz, który jest właścicielem tego plecaka, przemalował go w barwy imitujące kamuflaż. Zmień wartość atrybutu `kolor` stworzonego już plecaka `p2` na wartość `kamuflaż`.
- Wydrukuj obiekt `p2`.
