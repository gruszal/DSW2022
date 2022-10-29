# Wirtualne środowisko Pythona

```commandline
python3 -m venv venv
```

`python3` to interpreter, z którego korzystamy, będzie od "podstawą" wirtualnego środowiska
`-m venv` to polecenie, które uruchamia moduł tworzący wirtualne środowisko
drugie `venv` to katalog, w którym znajdują się pliki dla wirtualnego środowiska, w tym wszsytkie zewnętrzne moduły, które w nim zainstalujemy

## Aktywacja wirtualnego środowiska
https://docs.python.org/3/library/venv.html#how-venvs-work

Windows:
```commandline
venv\Scripts\activate
```

Linux/Mac
```commandline
source venv/bin/activate
```

## Package Installer for Python
```commandline
pip --version
pip freeze
pip install numpy
pip freeze
```

Instalacja zależności z pliku:
```commandline
pip install -r requirements.txt
```
