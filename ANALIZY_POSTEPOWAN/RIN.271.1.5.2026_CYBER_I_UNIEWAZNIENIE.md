# RIN.271.1.5.2026 — CYBERBEZPIECZNY SAMORZĄD I
## Analiza źródłowa do ASYSTENTA POSTĘPOWAŃ
Data: 25.09.2026

## Dane główne
Rodzaj: dostawy.
Tryb: art. 275 pkt 1 Pzp.
Identyfikator: ocds-148610-d3d80267-719c-4fe3-a6a8-22d2c41f562f.
Ogłoszenie o zamówieniu: 2026/BZP 00230611.
Ogłoszenie o wyniku/unieważnieniu: 2026/BZP 00248528/01 z 18.05.2026.
Plan: 2026/BZP 00012341/06/P, poz. 1.2.2.
Projekt: Cyberbezpieczny samorząd.

## Wniosek
Referat: Biuro ds. Obsługi Informatycznej i Rady Miejskiej.
Wartość szacunkowa netto: 535 000,00 zł.
Kwota przeznaczona brutto: 684 401,35 zł.
Data wniosku: 20.04.2026.
Termin realizacji wskazany we wniosku: 27.06.2026.
CPV: 48820000-2, 30233000-1, 72000000-5, 48000000-8, 30236000-2.
Warunki udziału 8.1–8.4: nie stawiano.

## Otwarcie
18.05.2026.
Kwota z art. 222 ust. 4: 684 401,35 zł.

Wpłynęła jedna oferta:
1. JT-SYSTEMS sp. z o.o. — 712 611,57 zł.

Cena przekraczała środki o 28 210,22 zł.

## Unieważnienie
Data: 18.05.2026.
Podstawa: art. 255 pkt 3 Pzp.
Zawiadomienie na podstawie art. 260 ust. 1.

Uzasadnienie faktyczne:
jedyna oferta JT-SYSTEMS 712 611,57 zł przekraczała kwotę 684 401,35 zł, a Zamawiający nie zwiększył środków do ceny oferty.

Nie było odrzucenia oferty — postępowanie zostało unieważnione z powodu relacji cena > finansowanie.

## Wadium
Pakiet zawiera wadium JT-SYSTEMS oraz dyspozycję zwrotu.
Po unieważnieniu program powinien automatycznie proponować obsługę zwrotu wadium.

## Relacja z kolejnym postępowaniem
To postępowanie jest bezpośrednim poprzednikiem:
RIN.271.1.6.2026 — Cyberbezpieczny samorząd II.

W ASYSTENCIE potrzebne pola:
- repeatedAsProceedingNumber,
- predecessorProceedingNumber,
- reasonForRepeat.

Przycisk „Ponów postępowanie” powinien kopiować dane bazowe SWZ/OPZ, ale pozwalać na zmianę zakresu, wartości, kwoty, terminów i publikacji.

## Oś czasu
20.04.2026 — wniosek.
06.05.2026 — ogłoszenie 00230611/01.
18.05.2026 — otwarcie.
18.05.2026 — jedna oferta 712 611,57 zł.
18.05.2026 — unieważnienie art. 255 pkt 3.
18.05.2026 — ogłoszenie wyniku/unieważnienia 00248528/01.
Następnie wszczęto RIN.271.1.6.2026.

## Do bazy
Dopisać:
- estimatedNet 535000,
- financingAmount 684401.35,
- jedyną ofertę JT-SYSTEMS 712611.57,
- resolutionPath = cancellation,
- cancelBasis = art. 255 pkt 3,
- cancelReason = cena jedynej oferty przekracza środki,
- resultNoticeNumber 2026/BZP 00248528/01,
- proceedingId,
- relationNext = RIN.271.1.6.2026.

## Wzorzec funkcjonalny
Cyber I jest modelowym przypadkiem:
PUBLIKACJA → 1 OFERTA → cena > środki → UNIEWAŻNIENIE → ZWROT WADIUM → PONOWIENIE POSTĘPOWANIA.

Program nie powinien oznaczać oferty jako „odrzuconej”, ponieważ przyczyna zakończenia dotyczy unieważnienia postępowania, nie wadliwości oferty.
