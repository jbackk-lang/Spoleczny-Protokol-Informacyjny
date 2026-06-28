## Dokumentacja online
https://jbackk-lang.github.io/
TIMDR + Λ–τ–ρ na danych 

# TIMDERA — Społeczny Protokół Informacyjny (v1.0)

## Cel modułu
TIMDERA jest społecznym protokołem informacyjnym, który umożliwia kodowanie i dekodowanie komunikatów w strukturach geometrycznych. System działa poza ograniczeniami platform, praw autorskich i cenzury.

## Elementy protokołu
- Skręt (Twist) — podstawowa jednostka informacji.
- Warstwy Λ–τ–ρ — struktura, transformacja, defekt.
- Klucz J — kompresja i dekodowanie komunikatu.
- Rytm — kodowanie czasowe.
- Modulacja — zmiana skrętu w czasie.

## Działanie protokołu
### Nadawca
1. Koduje treść w skręcie.
2. Nakłada warstwy Λ–τ–ρ.
3. Moduluje rytmem.
4. Kompresuje kluczem J.
5. Wysyła jako obraz/sygnał.

### Odbiorca
1. Dekompresuje kluczem.
2. Odtwarza warstwy.
3. Demoduluje rytm.
4. Odczytuje komunikat.

### Platforma
Widzi jedynie szum geometryczny — nie może analizować, blokować ani cenzurować komunikatu.

## Struktura modułu
/timdera_protocol/
    timdera_core.py
    timdera_key.py
    timdera_layers.py
    timdera_encoder.py
    timdera_decoder.py
    timdera_rhythm.py
