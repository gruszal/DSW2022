# Zadanie 1

Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek. Jako przykład
może posłużyć Fiat 126p z 1973 roku.

- Program zacznie ze stworzonym słownikiem o trzech kluczach:
    - marka (str)
    - model (str)
    - rocznik (int)
- Wypisze ten słownik na ekran (bez żadnego formatowania)
- Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
  > Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.
- Jeśli nie spełnia powyższego warunku, wypisze komunikat:
  > Twój samochód (tutaj_marka) jest jeszcze zbyt młody.
- Gdy program będzie poprawnie działał, pozmieniaj wartości słownika, aby zobaczyć, czy progam również zmienia swoje
  zachowanie.

# Rozszerzenie 1:

Kolejnym warunkiem, aby dostać "żółte tablice", jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W
naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.

- Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
    - dopisz do słownika nowy klucz `czy_oryginalny` i ustaw jego wartość (typ: bool) wedle uznania.
    - ponownie wyświetl zmieniony słownik
- Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności.
  Dopisz odpowiednie komunikaty.
