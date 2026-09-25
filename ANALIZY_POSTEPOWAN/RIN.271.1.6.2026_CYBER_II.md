# RIN.271.1.6.2026 — CYBERBEZPIECZNY SAMORZĄD II
## Analiza źródłowa do ASYSTENTA POSTĘPOWAŃ
Data: 25.09.2026

## Dane główne
Rodzaj: dostawy.
Tryb: art. 275 pkt 1 Pzp.
Identyfikator: ocds-148610-b722a5bf-13a3-4057-b5f0-a57288b56ba1.
Ogłoszenie: 2026/BZP 00256236/01.
Zmiana ogłoszenia: 2026/BZP 00267195/01 z 29.05.2026.
Wynik: 2026/BZP 00286923/01 z 12.06.2026.
Plan: 2026/BZP 00012341/07/P, poz. 1.2.3.
Projekt: Cyberbezpieczny samorząd.

## Wartości
Protokół:
wartość szacunkowa netto = 470 000,00 zł,
równowartość ok. 109 048,72 euro,
ustalona 01.04.2026 na podstawie planowanych kosztów.

Kwota przeznaczona:
588 461,35 zł brutto.

## Zmiana terminów
Postępowanie miało zmianę ogłoszenia/SWZ.
Końcowo:
składanie ofert 03.06.2026 godz. 10:00,
otwarcie 03.06.2026 godz. 10:15.

ASYSTENT musi przechowywać historię terminów, a nie tylko finalny termin.

## Otwarcie
2 oferty:
1. JT-SYSTEMS sp. z o.o. — 573 878,64 zł.
2. STIMO sp. z o.o. — 680 190,00 zł.

Odrzucone: 0.
RNC: 0.

Kryterium: cena 100%.

Ranking:
1. JT-SYSTEMS — 100,00 pkt.
2. STIMO — 89,06 pkt.

## Udostępnianie dokumentów
Pakiet zawiera wniosek o wgląd/udostępnienie ofert i korespondencję dotyczącą udostępnienia dokumentów.

To jest gotowy wzorzec dla modułu:
„Wniosek wykonawcy o udostępnienie dokumentacji postępowania”.
Należy przechowywać:
- wnioskodawcę,
- datę,
- zakres żądania,
- dokumenty udostępnione,
- datę odpowiedzi.

## Etap II
03.06.2026 godz. 12:16:06:
wezwanie art. 274 ust. 1 do JT-SYSTEMS.

Żądano:
oświadczenia z art. 108 ust. 1 pkt 5 — grupa kapitałowa — Załącznik nr 3.

Termin:
09.06.2026 godz. 14:00.

JT-SYSTEMS odpowiedział tego samego dnia:
03.06.2026 godz. 12:46:24,
przesyłając wymagany Załącznik nr 3.

## Wybór
Informacja o wyborze wysłana:
03.06.2026 godz. 14:37:39.

Wybrano ofertę nr 1 JT-SYSTEMS.

To pokazuje poprawną automatyzację:
wezwanie → odpowiedź → zatwierdzenie → wybór w tym samym dniu.

## Umowa — konflikt dat źródłowych
Plik umowy ma w treści:
„zawarta w dniu 9 czerwca 2026”.

Jednak raport weryfikacji podpisów potwierdza:
- podpis Burmistrza: 10.06.2026 12:48:58,
- podpis Skarbnika: 10.06.2026 12:49:18,
- podpis wykonawcy: 10.06.2026 19:41:36.

Ogłoszenie o wyniku BZP również podaje:
data zawarcia umowy 10.06.2026.

### Przyjęta data końcowa
10.06.2026.

Nagłówek 09.06 należy zachować jako rozbieżność źródłową / datę dokumentu roboczego.

## Umowa
Numer:
RIN.272.1.6.2026.

Wykonawca:
JT-SYSTEMS sp. z o.o.

Wartość brutto:
573 878,64 zł.

Wartość netto:
466 568,00 zł.

Termin:
90 dni od podpisania,
w treści umowy wskazano datę 07.09.2026.

Płatność:
30 dni od prawidłowej faktury i protokołu odbioru.

Odbiór:
protokołem podpisanym przez Zamawiającego i Wykonawcę.

## Korekta wcześniejszej niepewności
Wcześniejszy rekord miał rozbieżność:
ogłoszenie pierwotne „do 27.06.2026” vs wynik „90 dni”.

Podpisana umowa rozstrzyga:
90 dni, do 07.09.2026.

Zatem contractExecution.endDate powinno wynikać z umowy, a nie ze starego ogłoszenia.

## Wadium
Pakiet zawiera wadia JT-SYSTEMS i STIMO oraz dyspozycję zwrotu.

Po wyborze program powinien wyświetlać operacje wadialne dla obu wykonawców.

## Oś czasu
22.05.2026 — ogłoszenie.
29.05.2026 — zmiana ogłoszenia/SWZ.
03.06.2026 10:00 — termin ofert.
03.06.2026 10:15 — otwarcie.
03.06.2026 12:16 — wezwanie JT-SYSTEMS.
03.06.2026 12:46 — odpowiedź.
03.06.2026 14:37 — wybór.
10.06.2026 — podpisanie umowy przez strony.
12.06.2026 — ogłoszenie o wyniku.
07.09.2026 — termin umowny.

## Co poprawić w bazie
- estimatedNet = 470000,
- financingAmount = 588461.35,
- 2 pełne oferty,
- ranking 100 / 89.06,
- art. 274 action + odpowiedź,
- dokument udostępnienia ofert,
- finalContractDate = 2026-06-10,
- contractExecution.endDate = 2026-09-07,
- usunąć status niepewności 27.06 vs 90 dni,
- zachować sourceConflict: nagłówek umowy 09.06 vs faktyczne podpisy i BZP 10.06.

## Powiązanie z Cyber I
predecessor = RIN.271.1.5.2026.
Powód ponowienia:
pierwsze postępowanie unieważniono art. 255 pkt 3 po jedynej ofercie przewyższającej środki.

Cyber I + Cyber II powinny być wspólnym testem funkcji „ponów postępowanie”.
