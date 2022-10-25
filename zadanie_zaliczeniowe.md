# Zadanie zaliczeniowe

## Opis
Napisz skrypt pythonowy, który zamodeluje grę w "wisielca"/"koło fortuny". Użytkownik będzie miał za zadanie odgadnięcie hasła, wpisując literę po literze. Gdy gracz wpisze literę znajdującą się w haśle, ta litera pokazuje się na ekranie w odpowiednim miejscu. Gdy wpisanej litery nie ma w haśle, gracz traci jedną próbę. Gra kończy się zwycięstwem, gdy całe hasło jest odgadnięte, a przegraną, gdy gracz wyczerpie wszystkie próby.

## Funkcjonalności wymagane
- Podstawowa gra może mieć jedno hasło wpisane "na stałe".
- Wyświetlanie na ekranie hasła, w którym zamiast liter pojawiają się znaki podkreślenia: "_" gdy litera nie została odgadnięta.
  - Gdy litera zostanie odgadnięta, wszystkie jej wystąpienia mają pojawić się w odpowiednim miejscu wyświetlonego hasła.
- Wyświetlanie po każdej próbie gracza hasła zaktualizowanego o odgadnięte litery i komunikat o ilości pozostałych prób.
- Podsumowanie gry na jej koniec: komunikat o rezultacie (zwycięstwo lub przegrana)

## Funkcjonalności dodatkowe (wybierz co najmniej dwa, każdy myślnik to jedna funkcjonalność)
- Jeśli użytkownik wpisze więcej niż jedną literę, uznaj to za próbę odgadnięcia hasła. Jeśli użytkownik zgadł hasło: wygrywa, w przeciwnym razie traci jedną próbę. 
- Wyświetlaj wszystkie litery wpisane przez gracza. Jeśli litera została już wcześniej wpisana, nie odejmuj próby graczowi, ale poinformuj go o tym fakcie.
- Wielkie i małe litery powinny być nierozróżniane. W przypadku wybrania polskich znaków ("ą", "ę") gra powinna traktować je ich odpowiedniki z alfabetu łacińskiego ("ą" = "a", "ż" = "z")
- Losowanie hasła do odgadnięcia z wielu znajdujących się w pliku tekstowym (format txt, json lub csv).
  - (rozszerzenie) Dodaj do każdego hasła jego "kategorię", która wyświetlona zostanie na początku gry.
- Wybieranie poziomu trudności gry przed jej rozpoczęciem. Będzie to wpływać na ilość prób.
  - (rozszerzenie) Nadaj poziomy trudności dla haseł i wybieraj odpowiednie dla wybranego poziomu trudności.
- Zmierz czas całej rozgrywki i średni czas każdej próby zgadnięcia litery.
- Wynik każdej rozgrywki zapisuj do pliku tekstowego. Każda linia to jedna rozgrywka. W zapisie musi się znaleźć: rezultat, ilość prób, data (może być więcej informacji).

### Uwagi
- Oddając zadanie, proszę o opisanie, które z dodatkowych funkcjonalności zostały wybrane.
- Jeśli użyte zostały zewnętrzne moduły, proszę tę informację dopisać (nie dotyczy wbudowanych modułów)
- W przypadku wczytywania haseł z pliku, do rozwiązania należy dołączyć również ten plik.
