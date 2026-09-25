# RIN.271.1.4.2026 — KOMPLEKSOWE UBEZPIECZENIE GMINY RYMANÓW
## Analiza źródłowa do ASYSTENTA POSTĘPOWAŃ
Data analizy: 25.09.2026

## 1. Identyfikacja

Numer:
RIN.271.1.4.2026

Nazwa:
Kompleksowe ubezpieczenie Gminy Rymanów wraz z jednostkami organizacyjnymi

Rodzaj:
usługi.

Tryb:
tryb podstawowy, art. 275 pkt 1 Pzp.

Identyfikator:
ocds-148610-2d1cb2c7-c171-49f4-91ba-88e9bf106277

Ogłoszenie:
2026/BZP 00219390/01 z 28.04.2026.

Plan:
2026/BZP 00012341/05/P.

Pozycja:
1.3.4.

Postępowanie prowadzone z udziałem pełnomocnika/brokera:
MENTOR S.A.

Platforma:
mentor.logintrade.net.

---

# 2. Materiał źródłowy w ZIP

Pakiet zawiera głównie dokumentację przygotowawczą i publikacyjną:

- ogłoszenie o zamówieniu,
- SWZ,
- OPZ,
- formularz oferty,
- oświadczenie art. 125,
- osobny wzór umowy części I,
- osobny wzór umowy części II,
- grupę kapitałową,
- wniosek o udostępnienie części poufnej,
- wykaz mienia,
- pierwotne szacowanie,
- skorygowane szacowanie,
- skorygowany OPZ,
- pełnomocnictwo.

ZIP nie zawiera pełnego folderu po otwarciu ofert i podpisaniu umów. Dane wyniku i umów znane z bazy referencyjnej ASYSTENTA muszą więc pozostać oznaczone jako pochodzące z odrębnie zweryfikowanych ogłoszeń/publicznych źródeł, a nie z tego ZIP.

---

# 3. Części

Postępowanie podzielono na dwie części.

## Część I — ubezpieczenia majątkowe
Zakres obejmuje m.in.:
- ubezpieczenie mienia od wszystkich ryzyk,
- kradzież/rabunek i szkody szyb,
- odpowiedzialność cywilną, w tym OC zarządcy dróg,
- NNW,
- inne zakresy wyszczególnione w OPZ.

## Część II — ubezpieczenia komunikacyjne
Zakres:
- OC posiadaczy pojazdów,
- AC,
- NNW kierowcy i pasażerów,
- Assistance.

### Wniosek dla ASYSTENTA
Każda część ma:
- inny zakres,
- osobny wzór umowy,
- osobnego potencjalnego wykonawcę,
- osobną cenę,
- osobną realizację.

To potwierdza konieczność modelowania części jako pełnych podpostępowań.

---

# 4. Szacowanie — wersjonowanie danych

W repo znajdują się dwie wersje szacowania.

## Wersja wcześniejsza
Część I:
366 300,00 zł.

Część II:
234 000,00 zł.

Całość:
797 100,00 zł.

## Wersja skorygowana
Część I:
385 220,00 zł.

Część II:
234 000,00 zł.

Całość:
798 820,00 zł.

W skorygowanym dokumencie:
- część I zamówienie podstawowe 36 miesięcy: 350 200 zł,
- przewidywane powtórzenie usług 10%: 35 020 zł,
- wznowienie na 12 miesięcy: 119 600 zł,
- część II podstawowa: 180 000 zł,
- przewidywane powtórzenie 30%: 54 000 zł,
- wznowienie 12 miesięcy: 60 000 zł,
- całkowita wartość dokumentu: 798 820 zł.

### Ważna korekta
Dotychczasowa baza ASYSTENTA zawierała estimatedNet = 808 280 zł.

Ta wartość nie jest potwierdzona przez dwa znalezione dokumenty szacowania.

Najnowszy dokument w folderze „korekta” wskazuje:
798 820,00 zł.

### Zasada
Nie nadpisywać automatycznie bez śladu.
Zapisać:
- sourceVersion 1 = 797100,
- sourceVersion corrected = 798820,
- currentAcceptedEstimate = 798820,
- previous database value 808280 = do wyjaśnienia/wycofania.

---

# 5. Poufność dokumentacji

SWZ wyraźnie przewiduje dokumentację poufną.

Poufne:
- Załącznik nr 1 — OPZ,
- Załącznik nr 7 — wykaz mienia.

Wykonawca uzyskuje dostęp na wniosek:
Załącznik nr 6.

### Wniosek dla ASYSTENTA
Potrzebne pole:
attachmentConfidential = true.

Dla dokumentu poufnego:
- nazwa,
- numer,
- zasady udostępnienia,
- wniosek o dostęp,
- historia komu i kiedy udostępniono.

---

# 6. Termin realizacji

Podstawowy okres:
36 miesięcy od 01.06.2026.

Wznowienie:
12 miesięcy na dotychczasowych warunkach, jeżeli żadna ze stron nie złoży sprzeciwu najpóźniej 4 miesiące przed końcem okresu podstawowego.

Dla komunikacyjnych:
maksymalny okres wskazany w SWZ do 30.05.2030.

### Wniosek
ASYSTENT musi odróżniać:
- podstawowy okres umowy,
- wznowienie,
- opcję.

W tym postępowaniu:
wznowienie = TAK,
opcja = NIE.

---

# 7. Zamówienia podobne

Art. 214 ust. 1 pkt 7:
- część I — do 10% wartości zamówienia podstawowego,
- część II — do 30%.

To jest osobna cecha i nie powinna być utożsamiana z prawem opcji ani wznowieniem.

---

# 8. Kryteria

Dla obu części:

- Cena — 90 pkt,
- Klauzule fakultatywne — 10 pkt.

To jest ważny rzeczywisty przykład kryterium jakościowego specyficznego dla ubezpieczeń.

SWZ zawiera uzasadnienie zastosowania ceny z wagą powyżej 60%, wskazujące na ustandaryzowany jakościowo program ubezpieczenia.

### Biblioteka kryteriów
Do ASYSTENTA warto dodać:
„Klauzule fakultatywne” jako gotowe kryterium dla ubezpieczeń.

---

# 9. Wadium i zabezpieczenie

Wadium:
nie wymagano.

Zabezpieczenie należytego wykonania:
nie wymagano.

ASYSTENT nie powinien automatycznie narzucać zabezpieczenia dla usług.

---

# 10. Terminy publikacyjne

Pierwotne ogłoszenie:
28.04.2026.

Pierwotny termin składania:
14.05.2026 godz. 11:30.

Pierwotne otwarcie:
14.05.2026 godz. 12:00.

Termin związania:
30 dni.

Z wcześniejszej zweryfikowanej bazy wiadomo, że opublikowano później dwie zmiany:
- 2026/BZP 00238222/01 z 11.05.2026,
- 2026/BZP 00243168/01 z 14.05.2026,

a finalny termin ofert został przesunięty do 18.05.2026 godz. 11:30, otwarcie 12:00.

Te zmiany nie znajdują się w obecnym ZIP, więc w finalnej rekonstrukcji należy je powiązać z zewnętrzną historią ogłoszeń.

---

# 11. Wynik — dane referencyjne do zestawienia ze źródłami

Z wcześniej zweryfikowanych publicznych danych:

Ogłoszenie o wyniku:
2026/BZP 00269647/01 z 01.06.2026.

## Część I
Wykonawca:
COMPENSA TU S.A. Vienna Insurance Group.

Umowa:
29.05.2026.

Wartość:
300 555 zł.

## Część II
Wykonawca:
Generali T.U. S.A.

Umowa:
28.05.2026.

Wartość:
153 342 zł.

Razem:
453 897 zł.

### Uwaga źródłowa
Te dane nie pochodzą z analizowanego ZIP; są utrwalonymi, wcześniej zweryfikowanymi danymi publicznymi. Należy je zachować, ale w modelu provenance wskazać inne źródło.

---

# 12. Realizacja

Obie umowy są długoterminowe.

Część I:
od 29.05/01.06.2026, okres około 36 miesięcy.

Część II:
analogicznie, zgodnie z harmonogramem polis.

Na 25.09.2026:
umowy trwają.

Ogłoszenie o wykonaniu umowy:
jeszcze niewymagalne na podstawie samego bieżącego okresu realizacji.

---

# 13. Wzory umów

Pakiet zawiera:
- Załącznik 4a — umowa dla części I,
- Załącznik 4b — umowa dla części II.

### Bardzo ważny wniosek
Nie może istnieć założenie:
„jeden projekt umowy na całe postępowanie”.

ASYSTENT musi pozwalać:
część 1 → umowa A,
część 2 → umowa B.

Mechanizm powinien działać także, gdy części mają różne rodzaje zamówienia lub zupełnie odmienne wzory.

---

# 14. Specyficzny model pełnomocnika

Postępowanie jest prowadzone z brokerem jako pełnomocnikiem.

ASYSTENT powinien obsługiwać opcjonalnie:
- Zamawiającego,
- pełnomocnika prowadzącego postępowanie,
- platformę pełnomocnika,
- dane kontaktowe pełnomocnika,
- rolę w komunikacji.

Nie należy wpisywać brokera jako Zamawiającego.

---

# 15. Co poprawić w bazie ASYSTENTA

1. Zrewidować estimatedNet:
   - obecne 808280 jest niezgodne z dokumentami w paczce,
   - przyjąć po kontroli 798820 jako skorygowane szacowanie.
2. Zapisać wersjonowanie szacunku 797100 → 798820.
3. Dodać proceedingId.
4. Dodać plan 1.3.4 / 2026/BZP 00012341/05/P.
5. Dodać:
   - confidentialAttachments,
   - renewal = 12 miesięcy,
   - similarServicesPercent per part.
6. Kryteria dla każdej części: 90/10.
7. Zapisać brak wadium i brak zabezpieczenia.
8. Zachować osobne wzory umów dla części.
9. Zachować dwie zmiany ogłoszenia w noticeHistory.
10. W dalszej analizie zewnętrznych źródeł odtworzyć oferty i ranking, których ten ZIP nie zawiera.

---

# 16. Wniosek projektowy

To postępowanie jest wzorcem dla:
- pełnomocnika/brokera,
- alternatywnej platformy,
- dokumentacji poufnej,
- dwóch części,
- osobnych umów,
- wznowień,
- zamówień podobnych art. 214 ust. 1 pkt 7,
- kryterium „klauzule fakultatywne”,
- wersjonowania szacowania.

Szczególnie ważne:
ASYSTENT musi przechowywać wersje danych źródłowych. W tym jednym postępowaniu samo szacowanie zmieniło się z 797 100 do 798 820 zł. Historia nie może zniknąć po korekcie.
