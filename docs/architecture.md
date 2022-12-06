# Główne założenia
- Słownik z podstawowym zbiorem wulgaryzmów
- Jedno słowo na raz do młynu walidacyjnego
- Wszytkie walidatory muszą przejść pomyślnie, aby słowo nie było wulgrazymem
- Dużo prostych walidatorów, narazie unikamy rozległych walidatorów.
 
# Test driven development
Tworzymy na początku ale i na bieżąco zbiór słów testowych, który będzie odzwierciedlał skuteczność naszego walidatora.

# Mikrofiltry
- zamiana znaków (i,e,a,o,u) na kolejno: (1,3,4,0,v) - Frydziu
- zamianę małego L na duże i (“l” -> “I”), a litery “w” na “vv” - Frydziu
- powtarzanie niektórych liter w danym wyrazie, np. “ssłoowo” - Jeremi
- słowa mogą występować z różnymi końcówkami fleksyjnymi - Greg
- próby obejścia filtra poprzez dostawienie do wyrazu losowego znaku (na przykład
spacji), lub zamiana kolejności dwóch liter (dla większej ilości zamian, można
przyjąć, że słowo staje się nieczytelne). - Łukasz
- Więcej pomysłowych filtrów, co dusza zapragnie

# PODZIAŁ ZADAŃ
1. GREG
permutacje z danego słowa bazowego
2. Jeremi

4. Fryderyuk

6. Łukasz
proces sprawdzania słowa mikrofiltrami
wczytywanie wejścia
pokazywanie wyjścia
