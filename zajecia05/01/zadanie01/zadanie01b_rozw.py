from datetime import datetime

data_z_klawiatury = input("Podaj datę urodzin (w formacie RRRR-MM-DD): ")

data_urodzin = ''
try:
    data_urodzin = datetime.strptime(data_z_klawiatury, '%Y-%m-%d')
except ValueError:
    print('Podana data nie była w formacie RRRR-MM-DD.')
    exit()

obecna_data = datetime.now()

roznica = obecna_data - data_urodzin

lata = roznica.days // 365
dni = roznica.days % 365
print('Osoba ma obecnie: {} lat i {} dni'.format(lata, dni))
