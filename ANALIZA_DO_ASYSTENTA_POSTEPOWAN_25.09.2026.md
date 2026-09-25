# ANALIZA POSTĘPOWAŃ 2026 POD KĄTEM ASYSTENTA POSTĘPOWAŃ
Data opracowania: 25.09.2026
Repo źródłowe: chmielzbig/POST_2026
Repo docelowe programu: chmielzbig/ASYSTENT-POSTEPOWAN

## 0. Cel analizy

Celem nie jest wyłącznie przepisanie podstawowych danych z ogłoszeń. Każde rzeczywiste postępowanie ma zostać odtworzone w ASYSTENCIE tak, jak gdyby użytkownik prowadził je w programie od pierwszego wniosku aż do wykonania umowy.

Docelowo po wejściu w historyczne lub bieżące postępowanie użytkownik powinien móc:
- zobaczyć komplet danych przygotowawczych,
- wygenerować SWZ / zapytanie i załączniki,
- zobaczyć historię publikacji i zmian,
- zobaczyć wszystkie oferty w numeracji rzeczywistej,
- odtworzyć przebieg badania ofert,
- wygenerować wezwania i zawiadomienia odpowiadające rzeczywistemu przebiegowi,
- zobaczyć wybór albo unieważnienie,
- zobaczyć dane umowy dla całości lub części,
- śledzić wykonanie, zabezpieczenie, gwarancję/rękojmię,
- widzieć status obowiązku ogłoszenia o wykonaniu umowy.

Podstawowa zasada danych:
FAKT POTWIERDZONY ≠ WNIOSEK ≠ BRAK DANYCH ≠ HIPOTEZA.
Nie uzupełniać pól domysłem.

---

# 1. Źródła w repozytorium POST_2026

W katalogu głównym znajduje się 13 pakietów rzeczywistych postępowań:
1. RIN.271.1.1.2026 Kogutek.zip
2. RIN.271.1.2.2026 Woda Bzianka.zip
3. RIN.271.1.3.2026 dach gminy.zip
4. RIN.271.1.4.2026 ubezpieczenia.zip
5. RIN.271.1.5.2026 Cyber serwery.zip
6. RIN.271.1.6.2026 Cyber Serw 2.zip
7. RIN.271.1.7.2026 Drogi gminy.zip
8. RIN.271.1.8.2026 woda Bzianka 2.zip
9. RIN.271.1.9.2026 oświetlenie.zip
10. RIN.271.1.10.2026 Drogi moder 2.zip
11. RIN.271.1.11.2026 Elewacja BG.zip
12. RIN.271.1.12.2026 LekOfinansach.zip
13. RIN.271.1.13.2026 transp Odpad.zip

Dodatkowo:
- Zestawienie postepowan do 2021 do 2024 roku.xlsx

W repo ASYSTENTA istnieje już robocza baza:
- DANE_2026_DO_IMPORTU.json

oraz notatki rekonstruujące część danych z BIP, e-Zamówień i wcześniejszych archiwów.

---

# 2. Model przebiegu, który ASYSTENT powinien odtwarzać

Każde postępowanie należy analizować i zapisywać w poniższych etapach.

## ETAP A — PRZYGOTOWANIE / WNIOSEK

Z dokumentów typu:
- wniosek o wszczęcie,
- kalkulacja/szacowanie,
- kosztorys,
- notatka z ustalenia wartości,
- plan postępowań,
- zarządzenie / komisja,

należy wydobywać:

### A1. Identyfikacja
- numer postępowania,
- pełna nazwa,
- typ: robota / dostawa / usługa,
- tryb,
- podstawa prawna,
- tryb krajowy / unijny / poza Pzp,
- numer pozycji planu,
- identyfikator OCDS,
- jednostka / komórka merytoryczna,
- osoby przygotowujące.

### A2. Wartości
Rozdzielić bezwzględnie:
- wartość szacunkową netto,
- VAT,
- wartość szacunkową brutto, jeśli występuje,
- kwotę przeznaczoną na sfinansowanie zamówienia,
- źródła finansowania,
- dofinansowanie,
- udział własny,
- wartości części.

### A3. Przedmiot
- opis główny,
- CPV główny,
- CPV dodatkowe,
- zakresy branżowe,
- lokalizacja,
- działki / obiekty, jeśli występują,
- części i ich nazwy,
- zakres każdej części.

### A4. Terminy
- planowany termin realizacji,
- sposób liczenia terminu: dni / miesiące / data końcowa,
- terminy dla poszczególnych części,
- gwarancja,
- rękojmia,
- ewentualna wizja lokalna.

### A5. Warunki i zabezpieczenia
- warunki 8.1–8.4,
- dokumenty potwierdzające warunki,
- podstawy wykluczenia,
- wadium — całość / każda część,
- zabezpieczenie należytego wykonania umowy,
- wysokość zabezpieczenia,
- procent pozostawiany na rękojmię/gwarancję.

W ASYSTENCIE etap A powinien kończyć się statusem:
PRZYGOTOWANIE KOMPLETNE / BRAKUJE DANYCH.

---

# 3. ETAP B — SWZ / ZAPROSZENIE / ZAŁĄCZNIKI

Dla każdego postępowania należy zachować nie tylko wartości pól, ale również treści powtarzalnych zapisów.

Z pakietu źródłowego należy odnaleźć:
- SWZ,
- OPZ,
- PFU,
- przedmiar,
- STWiORB,
- formularz oferty,
- oświadczenie art. 125,
- oświadczenie grupa kapitałowa,
- wykaz robót/usług/dostaw,
- wykaz osób,
- zobowiązanie podmiotu trzeciego,
- projekt umowy,
- dokumenty branżowe,
- załączniki specjalne.

Dla każdego dokumentu należy zapisać:
- nazwę rzeczywistą,
- numer załącznika,
- wersję,
- datę,
- treść lub szablon,
- zależność od typu postępowania,
- zależność od części.

## Wniosek dla programu

ASYSTENT powinien budować załączniki z jednego modelu danych, ale umożliwiać:
- osobne zestawy dla każdej części,
- osobny projekt umowy dla części,
- załączniki branżowe zależne od zakresu,
- zachowanie numeracji zgodnej z konkretnym postępowaniem.

---

# 4. ETAP C — PUBLIKACJA

Należy odtwarzać pełną historię publikacji, a nie tylko numer pierwszego ogłoszenia.

Dla każdego wpisu publikacyjnego:
- typ dokumentu,
- numer,
- data,
- godzina,
- źródło,
- powód publikacji,
- dokument zastępowany / zmieniany.

Typy:
- ogłoszenie o zamówieniu,
- ogłoszenie o zamiarze zawarcia umowy,
- zmiana ogłoszenia,
- SWZ,
- zmiana SWZ,
- odpowiedzi na pytania,
- informacja o kwocie z art. 222 ust. 4,
- informacja z otwarcia,
- zawiadomienie o wyborze,
- ogłoszenie o wyniku,
- ogłoszenie o wykonaniu umowy.

## Ważna reguła
Przy kilku zmianach terminów ASYSTENT musi przechowywać historię:
stary termin → zmiana → termin końcowy.

Nie wolno nadpisywać starego terminu bez zachowania śladu.

---

# 5. ETAP D — PYTANIA I ODPOWIEDZI / MODYFIKACJE SWZ

Dla każdego pisma należy zapisać:
- data pytania,
- wykonawca, jeśli jawny,
- numer pytania,
- treść pytania,
- odpowiedź,
- czy odpowiedź zmienia SWZ,
- jakie pola/rozdziały zmienia,
- czy powoduje zmianę terminu ofert,
- czy wymaga ogłoszenia o zmianie.

Docelowy automat:
jeżeli odpowiedź zmienia termin lub element ogłoszenia → program podpowiada konieczność odpowiedniej publikacji.

---

# 6. ETAP E — OTWARCIE OFERT

To jeden z najważniejszych etapów do odtworzenia z rzeczywistych dokumentów.

Należy wydobyć:
- datę i godzinę otwarcia,
- kwotę przeznaczoną,
- liczbę ofert,
- numer każdej oferty,
- wykonawcę,
- adres,
- NIP / REGON, jeżeli występuje,
- cenę,
- wartości wszystkich kryteriów,
- część, której dotyczy oferta,
- czy wykonawca złożył ofertę na kilka części.

## Zasada numeracji
Numer oferty jest numerem nadanym przy otwarciu.
Nie wolno zastępować go późniejszą pozycją w rankingu.

ASYSTENT powinien pokazywać:
Oferta nr 1, nr 2, nr 3...
a osobno:
miejsce w rankingu.

---

# 7. ETAP F — BADANIE OFERT

Dla każdej oferty powinien powstać dziennik czynności.

Minimalny model:
- poprawność podpisu,
- pełnomocnictwo,
- formularz,
- oświadczenie wstępne,
- dokumenty wymagane z ofertą,
- przedmiotowe środki dowodowe,
- błędy rachunkowe,
- oczywiste omyłki,
- RNC,
- podstawy odrzucenia,
- wykluczenie,
- wezwania,
- odpowiedzi na wezwania,
- dokumenty podmiotowe,
- wynik badania.

Każda czynność:
- data,
- typ,
- podstawa prawna,
- treść pisma,
- termin odpowiedzi,
- data wpływu,
- rezultat,
- dokument wynikowy.

---

# 8. ETAP G — RAŻĄCO NISKA CENA

Jeżeli występowała analiza RNC, należy wydobyć:
- ceny wszystkich ofert,
- średnią,
- wartość szacunkową lub kwotę odniesienia właściwą dla analizy,
- progi,
- które oferty uruchomiły alert,
- treść wezwania,
- data wysłania,
- termin,
- odpowiedź wykonawcy,
- ocena wyjaśnień,
- finalna decyzja.

ASYSTENT nie powinien automatycznie stwierdzać RNC tylko na podstawie procentu.
Ma generować alert i dokument roboczy.

---

# 9. ETAP H — WEZWANIA DO DOKUMENTÓW / UZUPEŁNIEŃ

Należy wyróżnić różne rodzaje pism:
- art. 126 — dokumenty podmiotowe od najwyżej ocenionego,
- art. 128 — uzupełnienie/poprawienie dokumentów/oświadczeń,
- art. 223 — wyjaśnienie treści oferty / omyłki,
- art. 224 — RNC,
- inne pisma proceduralne.

Dla każdego wezwania:
- adresat,
- oferta,
- część,
- podstawa prawna,
- dokładna lista dokumentów,
- data wysłania,
- termin,
- data wpływu,
- ocena.

## Wniosek dla ASYSTENTA
Lista dokumentów w wezwaniu ma wynikać automatycznie z SWZ danego postępowania.
Użytkownik nie powinien ponownie zastanawiać się, które dokumenty zaznaczyć.

---

# 10. ETAP I — KLASYFIKACJA I WYBÓR

Należy zachować:
- punktację w każdym kryterium,
- łączną punktację,
- ranking,
- oferty odrzucone,
- wykonawców wykluczonych,
- ofertę wybraną,
- wybór osobno dla części,
- datę wyboru,
- podstawę wyboru,
- treść zawiadomienia.

Jeżeli postępowanie wieloczęściowe:
każda część musi mieć osobny:
- ranking,
- wynik,
- wybranego wykonawcę,
- datę,
- umowę,
- wykonanie.

---

# 11. ETAP J — UNIEWAŻNIENIE

Dla postępowania lub części:
- data,
- podstawa prawna,
- przyczyna,
- treść zawiadomienia,
- czy postępowanie ponowiono,
- numer postępowania następnego.

Przykład relacji:
RIN.271.1.5.2026 Cyber I → unieważnione
RIN.271.1.6.2026 Cyber II → ponowione.

Program powinien umożliwiać wskazanie takiego powiązania.

---

# 12. ETAP K — OKRES STANDSTILL I PODPISANIE UMOWY

Po wyborze program powinien wyliczać:
- datę zawiadomienia o wyborze,
- wymagany okres oczekiwania,
- pierwszy bezpieczny dzień podpisania,
- wyjątki, jeśli mają zastosowanie.

Następnie:
- numer umowy,
- data,
- wykonawca,
- zakres,
- część,
- wartość,
- termin,
- gwarancja,
- zabezpieczenie,
- data wniesienia zabezpieczenia,
- podwykonawstwo,
- dane zobowiązań z oferty.

---

# 13. ETAP L — WYKONANIE UMOWY

To musi być osobny moduł, nie tylko status „zakończone”.

Należy wydobywać:
- data rozpoczęcia,
- termin umowny,
- aneksy,
- przesunięcia terminu,
- zmiany wynagrodzenia,
- odbiory częściowe,
- odbiór końcowy,
- faktyczna data wykonania,
- wartość końcowa,
- kary,
- roszczenia,
- rozliczenie finansowe,
- status zabezpieczenia,
- data zwrotu części zabezpieczenia,
- kwota pozostawiona,
- koniec rękojmi/gwarancji.

---

# 14. OGŁOSZENIE O WYKONANIU UMOWY — LICZNIK / ALERT

To powinien być widoczny wskaźnik na kaflu postępowania.

Proponowany model statusów:

1. UMOWA JESZCZE TRWA
   - data umowy
   - planowany koniec
   - liczba dni do planowanego końca

2. TERMIN UMOWNY MINĄŁ — SPRAWDŹ WYKONANIE
   - brak potwierdzonego odbioru/aneksu

3. WYKONANO — OGŁOSZENIE DO PUBLIKACJI
   - faktyczna data wykonania znana
   - ogłoszenie nieopublikowane

4. OGŁOSZENIE O WYKONANIU OPUBLIKOWANE
   - numer
   - data publikacji

5. NIE DOTYCZY
   - np. postępowanie poza Pzp, jeśli brak takiego obowiązku.

Na panelu:
UMOWA: 22.09.2026
PLANOWANY KONIEC: 06.11.2026
WYKONANIE: w realizacji
OGŁOSZENIE WYKONANIA: jeszcze niewymagalne

lub:

UMOWA: 29.05.2026
PLANOWANY KONIEC: 13.07.2026
WYKONANIE: do potwierdzenia
OGŁOSZENIE WYKONANIA: ALERT — sprawdź odbiór / aneks

Nie należy utożsamiać końca gwarancji z momentem publikacji ogłoszenia o wykonaniu umowy. Moduł powinien przechowywać osobno wykonanie umowy oraz gwarancję/rękojmię.

---

# 15. STAN ROBOCZY POSZCZEGÓLNYCH POSTĘPOWAŃ

Poniższe dane są stanem już odtworzonym w ASYSTENCIE i stanowią punkt startowy do porównania z zawartością ZIP.

## RIN.271.1.1.2026 — KOGUTEK
- zamówienie z wolnej ręki,
- art. 305 pkt 1 w zw. z art. 214 ust. 1 pkt 13,
- wartość szacunkowa netto: 399 187 zł,
- kwota przeznaczona: 491 000 zł,
- umowa: 30.01.2026,
- wykonawca: Spółdzielnia Socjalna KOGUTEK,
- wartość umowy: 491 200 zł,
- realizacja: 01.02–31.12.2026,
- ogłoszenie o wyniku: 2026/BZP 00088308/01,
- na 25.09.2026 umowa trwa.

Do pełnej rekonstrukcji z ZIP:
- zaproszenie/negocjacje,
- protokół,
- dokumenty kwalifikacyjne,
- uzasadnienie in-house,
- treść umowy.

## RIN.271.1.2.2026 — Bzianka cz.1
- wartość szacunkowa: 3 404 807,87 zł netto,
- kwota przeznaczona: 2 200 000 zł,
- umowa: 15.05.2026,
- wykonawca: ROLWOD,
- wartość: 2 323 929,50 zł,
- planowany okres: 180 dni.

Do wydobycia:
- pełna lista ofert,
- ranking,
- badanie,
- wezwania,
- dokumenty wykonawcy,
- podpisana umowa i dokładne liczenie terminu.

## RIN.271.1.3.2026 — Dach UG
- wartość szacunkowa: 69 147,09 zł netto,
- kwota przeznaczona we wniosku niepotwierdzona,
- 9 ofert,
- 2 oferty odrzucone,
- umowa 29.05.2026,
- wykonawca ABE Budownictwo EMIL BAIDA,
- wartość 115 620 zł,
- termin 45 dni minął.

Priorytet:
odtworzyć wszystkie 9 ofert i 2 rzeczywiste odrzucenia oraz sprawdzić wykonanie/odbiór.

## RIN.271.1.4.2026 — Ubezpieczenie
- postępowanie na 2 części,
- wartość szacunkowa 808 280 zł,
- kwota przeznaczona 538 800 zł,
- 2 zmiany ogłoszenia,
- wynik 01.06.2026,
- część 1: Compensa, 300 555 zł,
- część 2: Generali, 153 342 zł,
- okres 36 miesięcy.

Postępowanie jest bardzo dobrym wzorcem dla:
- części,
- osobnych umów,
- różnych wykonawców,
- wieloletniej realizacji,
- zmian ogłoszenia.

## RIN.271.1.5.2026 — Cyber I
- postępowanie unieważnione,
- brak umowy,
- powinno być wzorcem ścieżki UNIEWAŻNIENIE → NOWE POSTĘPOWANIE.

Do wydobycia:
- oferty / brak ofert,
- dokładna podstawa,
- treść zawiadomienia,
- powiązanie z Cyber II.

## RIN.271.1.6.2026 — Cyber II
- 2 oferty,
- wybrano JT-SYSTEMS,
- umowa 10.06.2026,
- wartość 573 878,64 zł,
- zmiana terminu ofert na 03.06.2026,
- rozbieżność terminu wykonania: 27.06 vs 90 dni.

Najważniejsze:
podpisana umowa musi rozstrzygnąć rzeczywisty termin i status ogłoszenia o wykonaniu.

## RIN.271.1.7.2026 — Drogi
- wartość szacunkowa 1 748 755,60 zł,
- kwota przeznaczona 2 100 000 zł,
- umowa 21.07.2026,
- DROGBUD,
- wartość 1 617 479,77 zł,
- planowany okres 90 dni.

Do wydobycia:
pełna lista ofert, gwarancje, badanie, dokumenty etapu II.

## RIN.271.1.8.2026 — Bzianka cz.2
- 11 ofert,
- wybrano Zakład Budowlano-Instalacyjny Grzegorz Falger,
- umowa 22.09.2026,
- wartość 845 625 zł,
- realizacja do 15.12.2026.

Priorytet:
odtworzyć wszystkie 11 ofert wraz z punktacją i przebiegiem badania.

## RIN.271.1.9.2026 — Oświetlenie
- wartość szacunkowa 1 210 302,59 zł netto,
- kwota przeznaczona 1 150 000 zł,
- wadium 12 000 zł,
- na zapisany stan brak potwierdzonego wyniku.

ZIP należy potraktować jako źródło nadrzędne dla:
- otwarcia,
- wykonawców,
- badania,
- aktualnego statusu.

## RIN.271.1.10.2026 — Drogi etap 2
Postępowanie referencyjne dla części.

- 2 części,
- wartość szacunkowa razem 380 000 zł netto,
- kwota przeznaczona 460 000 zł,
- 6 ofert w bazie,
- wybór 15.09.2026,
- część 1: LUKATRANS, umowa 22.09, 192 267,45 zł, gwarancja 60 miesięcy,
- część 2: Karol Wesołowski, umowa 23.09, 163 633,67 zł, gwarancja 60 miesięcy.

To postępowanie powinno być głównym wzorcem dla:
- ofert składanych na różne części,
- osobnego rankingu,
- osobnych wezwań,
- osobnych wyborów,
- dwóch umów,
- dwóch terminów wykonania.

## RIN.271.1.11.2026 — Elewacja
- wadium 2 000 zł,
- termin ofert 15.09.2026,
- realizacja 60 dni,
- cena 70 / gwarancja 30,
- stan zapisany: brak wyniku.

ZIP ma pierwszeństwo w ustaleniu:
- kwoty z art. 222 ust. 4,
- ofert,
- wezwań,
- aktualnego wyniku.

## RIN.271.1.12.2026 — Lekcje o finansach / wycieczki
- 22 wycieczki,
- kwota przeznaczona 421 413 zł,
- wadium 4 000 zł,
- cena 60 / standard zakwaterowania 40,
- termin ofert 18.09.2026,
- stan zapisany: brak wyniku.

To postępowanie powinno posłużyć do rozbudowy kryteriów jakościowych innych niż cena/gwarancja.

## RIN.271.1.13.2026 — PSZOK
- wartość szacunkowa 312 350 zł netto,
- kwota przeznaczona 384 190,50 zł,
- wadium 4 000 zł,
- cena 80 / termin płatności 20,
- termin ofert 30.09.2026,
- warunek BDO,
- potencjał techniczny,
- branżowe załączniki odpadowe.

To postępowanie jest wzorcem dla:
- usług odpadowych,
- warunku uprawnień,
- warunku sprzętowego,
- dokumentów branżowych,
- kryterium terminu płatności.

---

# 16. ZESTAWIENIE HISTORYCZNE — JAK WYKORZYSTAĆ

Arkusz historyczny powinien zostać wykorzystany do dwóch celów.

## 16.1. Kontrola obowiązku publikacji
Dla każdej pozycji:
- numer,
- data umowy,
- planowany/faktyczny koniec,
- czy jest ogłoszenie o wykonaniu,
- numer i data ogłoszenia.

## 16.2. Moduł „do zrobienia”
ASYSTENT powinien automatycznie filtrować:
- umowy po terminie,
- brak ogłoszenia,
- brak formalnej daty wykonania,
- brak zwrotu zabezpieczenia,
- zbliżający się koniec gwarancji/rękojmi.

---

# 17. POWTARZALNE TREŚCI, KTÓRE NALEŻY WYDOBYĆ JAKO SZABLONY

Z całego korpusu należy zbudować bibliotekę rzeczywistych pism:

1. informacja o kwocie przeznaczonej,
2. informacja z otwarcia,
3. wezwanie art. 126,
4. wezwanie art. 128,
5. wezwanie art. 223,
6. wezwanie art. 224,
7. poprawienie omyłki,
8. informacja o odrzuceniu,
9. wybór oferty,
10. unieważnienie,
11. zwrot wadium,
12. wezwanie przed umową,
13. zwrot zabezpieczenia,
14. ogłoszenie wyniku,
15. ogłoszenie wykonania.

Przy każdym szablonie rozdzielić:
- tekst stały,
- pola dynamiczne,
- listę dokumentów wynikającą z SWZ,
- wariant dla części.

---

# 18. ULEPSZENIA ASYSTENTA WYNIKAJĄCE Z RZECZYWISTYCH POSTĘPOWAŃ

## 18.1. Jedna oś czasu
Każde postępowanie powinno mieć chronologiczną oś:
Wniosek → publikacja → zmiana → pytania → kwota → otwarcie → wezwania → wybór → umowa → wykonanie.

## 18.2. Dokumenty generowane „w miejscu zdarzenia”
Przy czynności powinien być przycisk:
„Pokaż / wygeneruj dokument”.

Np. przy wezwaniu:
- pismo,
- data,
- termin,
- odpowiedź,
- wynik.

## 18.3. Automatyczne przechodzenie danych
Dane wpisane wcześniej nie mogą być ponownie przepisywane:
- wykonawca z oferty → wezwanie → wybór → umowa,
- lista dokumentów SWZ → wezwanie art. 126,
- data wyboru → termin bezpiecznego podpisania,
- umowa → harmonogram wykonania,
- gwarancja z oferty → umowa → koniec gwarancji.

## 18.4. Części jako pełne podpostępowania
Każda część powinna mieć własny przebieg od ofert do wykonania.

## 18.5. Stan dokumentu
Każdy dokument:
- planowany,
- przygotowany,
- wysłany/opublikowany,
- odpowiedź otrzymana,
- zamknięty.

---

# 19. PLAN DALSZEJ PRACY NA PLIKACH POST_2026

Dla każdego ZIP należy przeprowadzić identyczny audyt:

### KROK 1 — indeks plików
Lista wszystkich plików i folderów.

### KROK 2 — klasyfikacja dokumentów
Przypisać dokument do etapu A–L.

### KROK 3 — ekstrakcja danych
Wartości, daty, wykonawcy, oferty, pisma.

### KROK 4 — chronologia
Ułożyć wydarzenia po dacie.

### KROK 5 — porównanie z DANE_2026_DO_IMPORTU.json
- potwierdzone,
- brakujące,
- rozbieżne,
- wymagające korekty.

### KROK 6 — biblioteka pism
Wyciągnąć treści rzeczywistych pism do wzorców.

### KROK 7 — uzupełnienie bazy ASYSTENTA
Dopiero po potwierdzeniu źródłowym.

### KROK 8 — test w programie
Wejść w postępowanie i sprawdzić:
czy można przejść cały historyczny przebieg bez ręcznego dopisywania brakujących danych.

---

# 20. TECHNICZNA UWAGA DOTYCZĄCA ZIP

GitHub API udostępnia same pliki ZIP, ale nie indeksuje ich wewnętrznej zawartości jako kodu.
W repo POST_2026 dodano:
- scripts/extract_post2026.py
- .github/workflows/extract-post2026.yml

Ich przeznaczenie:
rozpakować archiwa i utworzyć tekstowy katalog ANALIZA_WYDOBYTA, tak aby każdy dokument był możliwy do dalszego wyszukiwania i porównywania.

Na moment utworzenia tej analizy repo nie wykazuje uruchomionych GitHub Actions, więc szczegółowa analiza wnętrza każdego ZIP będzie kontynuowana po uzyskaniu indeksu lub inną drogą dostępu do plików binarnych.

Nie wpływa to na model danych i plan migracji opisany powyżej; obecne dane referencyjne pochodzą z DANE_2026_DO_IMPORTU.json, wcześniejszych notatek projektowych i już potwierdzonych źródeł.

---

# 21. PRIORYTETY DLA NASTĘPNEGO ETAPU

1. Odtworzyć komplet ofert i badanie dla:
   - RIN.271.1.3.2026,
   - RIN.271.1.8.2026,
   - RIN.271.1.10.2026.

2. Sprawdzić aktualny rzeczywisty stan:
   - RIN.271.1.9.2026,
   - RIN.271.1.11.2026,
   - RIN.271.1.12.2026.

3. Z umów ustalić:
   - Cyber II — rzeczywisty termin wykonania,
   - Dach — faktyczne wykonanie,
   - wszystkie zakończone — obowiązek ogłoszenia o wykonaniu.

4. Zbudować wspólną bibliotekę rzeczywistych pism.

5. Dodać do głównego panelu ASYSTENTA wskaźnik:
UMOWA → KONIEC → WYKONANIE → OGŁOSZENIE O WYKONANIU.

6. Następnie zasilić każde postępowanie pełnym historycznym workflow.

---

# 22. ZASADA KOŃCOWA

Historyczne postępowanie w ASYSTENCIE ma zachowywać się jak postępowanie prowadzone na żywo.

Użytkownik ma móc otworzyć np. RIN.271.1.10.2026 i przejść:
SWZ → otwarcie → oferta nr 1...6 → badanie → wezwanie → klasyfikacja → wybór części 1 i 2 → umowa części 1 i 2 → wykonanie,
a przy każdym kroku zobaczyć lub wygenerować właściwy dokument.

To jest docelowy standard kompletności dla wszystkich rekordów 2026 i później dla archiwum historycznego.
