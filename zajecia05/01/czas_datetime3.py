from datetime import datetime

teraz = datetime.now()

print(teraz.timestamp())  # POSIX timestamp: ile sekund minęło od 1970-01-01, początek "epoki Unix'a"
# https://pl.wikipedia.org/wiki/Czas_uniksowy
