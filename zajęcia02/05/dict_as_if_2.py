dzien = input('Wpisz dzień tygodnia: ')

dni_tygodnia = {'poniedziałek': 'Monday',
                'wtorek': 'Tuesday',
                'środa': 'Wednesday',
                'czwartek': 'Thursday',
                'piątek': 'Friday',
                'sobota': 'Saturday',
                'niedziela': 'Sunday'}

print('{} po angielsku to: {}'.format(dzien, dni_tygodnia[dzien]))
