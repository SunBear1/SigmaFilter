# SigmaFilter

### Opis
Projekt umożliwia zamianę wybranych niecenzuralnych słów języka polskiego na gwiazdki.

### Instalacja
W celu przygotowania środowiska do uruchomienia należy: 
- zainstalować interpreter [pythona](https://www.python.org/downloads/) w wersji co najmniej 3.9
- Będąc w folderze z projektem użyć komendy `pip install requirements.txt`

### Użycie
w celu uruchomienia programu należy wywołać komendę:

```
cd .\src
python main.py
```

Konsolowy interfejs pozwala na wybranie jednego z 2 źródeł wejścia programu:
- plik `wejscie.txt` znajdujący się w głównym folderze projektu
- Wejście użytkownika z konsoli

Program wypisuje na wyjściu konsoli tekst z przekleństwami zamienionymi na gwiazdki (*)
. 

Lista obsługiwanych przez nas wulgaryzmów dostępna jest w pliku `data/badwords.yaml`

### Testy
W celu przedstawienia możliwości filtra przygotowaliśmy testy. Aby je uruchomić należy wywołać komendę:

```
cd .\test 
pytest e2e -v
```

### Działanie 
Działanie filtra możemy podzielić na 2 etapy:
- przygotowanie słowa
- wykrycie wulgaryzmu i zamiana go na gwiazdki

w pierwszym etapie przeprowadzamy modyfikacje słów używając modularnych funkcji realizujących poniższe zadania:
- Usuwanie powtarzających się liter
- tworzenie kombinacji słowa na podstawie znaków bliskoznacznych 
  - np. (1,3,4,0,v) na kolejno: (i,e,a,o,u) 
- wykrywanie specjalnych znaków 
  - w tym spacji
- przetwarzanie słowa do pierwotnego znaczenia
  - kurwy -> kurwa

Następnie tak oczyszczone słowa są sprawdzane pod kątem występowania w naszej liście wulgaryzmów i w razie wykrycia ocenzurowane

Sprowadzając słowo do formy podstawowej, wykorzystujemy bibliotekę python Morfeusz2. Biblioteka potrafi również zklasyfikować słowo np. jako wulgaryzm.
