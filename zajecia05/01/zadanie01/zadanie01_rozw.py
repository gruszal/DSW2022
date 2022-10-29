from datetime import datetime

data_z_klawiatury = input("Podaj datę urodzin (w formacie RRRR-MM-DD): ")
data_urodzin = datetime.strptime(data_z_klawiatury, '%Y-%m-%d')

obecna_data = datetime.now()

roznica = obecna_data - data_urodzin

print('Osoba ma obecnie: {} lat'.format(roznica.days // 365))
