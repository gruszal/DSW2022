# Zadanie 02

Używając jako szablonu rozwiązanego zadania `zadanie01.py` napisz skrypt, który:
- w przypadku wprowadzenia przez użytkownika wartości, której nie da się przerobić na typ `int`, poinformuje o tym użytkownika i zakończy działanie.
- w przypadku wprowadzenia przez użytkownika wartości, która nie jest poprawnym indeksem, również poinformuje o tym fakcie i zakończy działanie.
- w przypadku podania prawidłowego indeksu program wypisze na ekran nazwę wybranego producenta.

## Podpowiedź:
Najprostszym sposobem na sprawdzenie jaki wyjątek należy obsłużyć, jest uruchomienie programu i wywołanie nieporządanej sytuacji, i odczytanie nazwy wyjątku z komunikatu wypisanego przez interpreter.

## Rozszerzenie 1:
- W przypadku wprowadzenia nieprawidłowej wartości komunikat powinien zawierać w sobie tę wpisaną wartość.

## Rozszerzenie 2:
- W przypadku wprowadzenia nieprawidłowej wartości program powinien ponawiać pytanie aż do otrzymania poprawnej wartości (lub do przerwania jego pracy z zewnątrz). 
