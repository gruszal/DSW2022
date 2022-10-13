szablon = 'ZAPROSZENIE\n' \
          'Serdecznie zapraszam\n' \
          '{gosc1} wraz z {gosc2}\n' \
          'na uroczystość, która odbędzie się w\n' \
          '{miejsce}'

zaproszenie = szablon.format(gosc1="Zenona",
                             gosc2="Osobą Towarzyszącą",
                             miejsce="Gdańsku")

print(zaproszenie)
