import random
WIELKOSC = 8
SASIADOW_ABY_CIAZA = 3
SASIADOW_ABY_NIE_UMRZEC = (2, 3)

def policz_sasiadow(plansza, x, y):
    liczba_sasiadow = 0 - plansza[x][y]  # żeby nie było +1 bo liczy siebie
    for i in range(x - 1, x + 1 + 1):
        for j in range(y - 1, y + 1 + 1):
            # python więc range końcowy +1
            try:
                assert i >= 0
                assert j >= 0
                if plansza[i][j]:
                    liczba_sasiadow += 1
            except:
                pass
    return liczba_sasiadow


def przelicz_plansze(plansza):
    plansza_nowa = [[False for _ in range(WIELKOSC)] for _ in range(WIELKOSC)]
    for rzad_num in range(WIELKOSC):
        for komorka_num in range(WIELKOSC):
            liczba_sasiadow = policz_sasiadow(plansza, rzad_num, komorka_num)
            wartosc_komorki = plansza[rzad_num][komorka_num]
            if not wartosc_komorki and liczba_sasiadow == SASIADOW_ABY_CIAZA:
                nowa_wartosc = True
            elif wartosc_komorki and liczba_sasiadow in SASIADOW_ABY_NIE_UMRZEC:
                nowa_wartosc = True
            else:
                nowa_wartosc = False
            plansza_nowa[rzad_num][komorka_num] = nowa_wartosc
    return plansza_nowa


def wyswietl_plansze(plansza):
    for linijka in plansza:
        for komorka in linijka:
            if komorka:
                print("🟩", end="")
            else:
                print("🟥", end="")
        print("")
    print("---")

