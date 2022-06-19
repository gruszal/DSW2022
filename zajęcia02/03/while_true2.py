while True:
    odpowiedz = input('Wpisz tekst lub "koniec" aby zakończyć wpisywanie: ')

    if odpowiedz == 'koniec':
        break  # 'break' powoduje wyjście z pętli

    print('Wpisano:', odpowiedz)

print('Koniec programu!')
