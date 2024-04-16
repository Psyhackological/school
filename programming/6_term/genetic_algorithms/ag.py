"""
Ten modul zawiera funkcje pomocnicze do symulacji algorytmu genetycznego.
"""

import numpy as np


def popinit(lg, lch):
    """
    Inicjalizuje populacje chromosomow z losowymi genami.
    Argumenty:
        lg (int): Liczba genow w chromosomie.
        lch (int): Liczba chromosomow w populacji.
    Zwraca:
        np.array: Populacja chromosomow.
    """
    # Tworzenie macierzy o wymiarach (lch, lg+1), wypelnionej zerami i jedynkami
    xp = np.random.randint(2, size=(lch, lg))

    return xp


def ocena(xp, wartosc, waga):
    """
    Ocenia populacje, uwzgledniajac ograniczenie na sume wag.
    Argumenty:
        xp (np.array): Populacja.
        wartosc (np.array): Wartosci poszczegolnych genow.
        waga (np.array): Waga poszczegolnych genow.
    Zwraca:
        tuple: Ocena populacji oraz waga chromosomow.
    """
    ocena_populacji = []
    waga_chromosomu = []

    for chromosom in xp:
        suma_wag = np.sum(chromosom * waga)
        fp = np.sum(chromosom * wartosc)
        ocena_populacji.append(fp)
        waga_chromosomu.append(suma_wag)

    return (np.array(ocena_populacji), np.array(waga_chromosomu))


def wczytaj_z_plikow(lg, plik_waga="wag1.txt", plik_wartosci="wart1.txt"):
    """
    Wczytuje wartosci i wagi z plikow.

    Argumenty:
        lg (int): Liczba genow w chromosomie.
        plik_waga (str, optional): Sciezka do pliku z wagami. Domyslnie "wag1.txt".
        plik_wartosci (str, optional): Sciezka do pliku z wartosciami. Domyslnie "wart1.txt".

    Zwraca:
        tuple: Krotka zawierajaca wartosci i wagi.
    """
    wartosci = np.loadtxt(plik_wartosci)[:lg]
    # Dodajemy 1 bo musi sie shape zgadzac po waga_max
    wagi = np.loadtxt(plik_waga)[: lg + 1]

    return wartosci, wagi


def wczytaj_z_klawiatury():
    """
    Wczytuje parametry algorytmu genetycznego od uzytkownika.

    Zwraca:
        tuple: Krotka zawierajaca wczytane parametry: liczba chromosomow (lch),
               liczba genow w chromosomie (lg), liczba pokolen (lpop),
               prawdopodobienstwo mutacji (pm), prawdopodobienstwo krzyzowania (pk).
    """
    # Liczba chromosomow w populacji
    lch = int(input("Podaj liczbe chromosomow w populacji (max. 50): "))
    lch = min(lch, 50)  # (max. 50)

    # Liczba genow w chromosomie
    lg = int(input("Podaj liczbe genow chromosomu (max. 10): "))
    lg = min(lg, 10)  # (max. 10)

    # Liczba pokolen
    # lpop = int(input("Podaj liczbe pokolen (max. 500): "))
    # lpop = min(lpop, 500)  # (max. 500)

    # pm - prawdopodobienstwo zajscia mutacji (0. – 0.1)
    # pm = float(input("Podaj prawdopodobienstwo zajscia mutacji (0. – 0.1): "))
    # pm = min(pm, 0.1)  # Gdy bedzie za duzo wezmiemy 0.1

    # prawdopodobienstwo zajscia krzyzowania (0.6 – 1.0)
    # pk = float(input("Podaj prawdopodobienstwo zajscia krzyzowania (0.6 – 1.0): "))
    # pk = min(pk, 0.8)  # Gdy bedzie za duzo wezmiemy cos po srodku

    return (lch, lg)


def wyswietl_parametry(lch, lg):
    """
    Wyswietla parametry algorytmu genetycznego.

    Argumenty:
        lch (int): Liczba chromosomow w populacji.
        lg (int): Liczba genow w chromosomie.
        lpop (int): Liczba pokolen.
        pm (float): Prawdopodobienstwo mutacji.
        pk (float): Prawdopodobienstwo krzyzowania.
    """
    print()
    print("Wybrane parametry:")
    print(f"{lch = }")
    print(f"{lg = }")
    # print(f"{lpop = }")
    # print(f"{pm = }")
    # print(f"{pk = }")
    print()


def zrob_hist(ocena_populacji, nazwa_pliku="hist.txt"):
    """
    Zapisuje podstawowe statystyki oceny populacji do pliku.

    Argumenty:
        ocena_populacji (np.array): Oceny chromosomow w populacji.
        nazwa_pliku (str): Nazwa pliku, do ktorego zostana zapisane statystyki. Domyslnie 'hist.txt'.
    """
    min_fp = np.min(ocena_populacji)
    max_fp = np.max(ocena_populacji)
    srednia_fp = np.mean(ocena_populacji)

    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(
            f"{min_fp},{max_fp},{srednia_fp}, wartosci zmiennych decyzyjnych.\n")


def rodzice(xp, ocena_populacji, waga_populacji, waga_max):
    """
    Wykonuje selekcje turniejowa w populacji chromosomow.

    Argumenty:
        xp (np.array): Populacja chromosomow.
        ocena_populacji (np.array): Oceny chromosomow w populacji.
        waga_populacji (np.array): Wagi chromosomow w populacji.
        waga_max (float): Maksymalna dozwolona suma wag.

    Zwraca:
        list: Lista indeksow zwycieskich chromosomow.
    """
    nrxp = []
    for _ in range(len(xp)):
        ch1, ch2 = np.random.choice(len(xp), 2, replace=False)
        (waga_ch1, waga_ch2) = (waga_populacji[ch1], waga_populacji[ch2])

        # Przekroczone obie wagi, szukamy blizszej
        if waga_ch1 > waga_max and waga_ch2 > waga_max:
            wybrany = (
                ch1 if abs(waga_ch1 - waga_max) < abs(waga_ch2 -
                                                      waga_max) else ch2
            )
            print(
                f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{wybrany + 1:02} wygral: wagi {waga_ch1, waga_ch2} > {waga_max}, ch{wybrany + 1:02} blizej waga_max."
            )

        # ch1 jest ponizej wagi_max, a ch2 powyzej
        elif waga_ch1 <= waga_max < waga_ch2:
            print(
                f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{ch1 + 1:02} wygral: waga ch{ch1 + 1} = {waga_ch1} <= {waga_max}, waga ch{ch2 + 1:02} = {waga_ch2} > {waga_max}."
            )
            wybrany = ch1

        # ch2 jest ponizej wagi_max, a ch1 powyzej
        elif waga_ch2 <= waga_max < waga_ch1:
            print(
                f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{ch2 + 1:02} wygral: waga ch{ch2 + 1} = {waga_ch2} <= {waga_max}, waga ch{ch1 + 1:02} = {waga_ch1} > {waga_max}."
            )
            wybrany = ch2

        # pojedynek ocen
        else:
            wybrany = ch1 if ocena_populacji[ch1] > ocena_populacji[ch2] else ch2
            if wybrany == ch1:
                print(
                    f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{ch1 + 1} wygral: wagi ({waga_ch1}, {waga_ch2}) <= {waga_max}, oceny ch{ch1 + 1} = {ocena_populacji[ch1]} > {ocena_populacji[ch2]} (ocena ch{ch2 + 1})."
                )
            else:
                print(
                    f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{ch2 + 1} wygral: wagi ({waga_ch1}, {waga_ch2}) <= {waga_max}, oceny ch{ch2 + 1} = {ocena_populacji[ch2]} > {ocena_populacji[ch1]} (ocena ch{ch1 + 1})."
                )

        nrxp.append(wybrany)

    return nrxp


# WYKONYWANIA SKRYPTU GLOWNEGO
if __name__ == "__main__":
    # KLAWIATURA WCZYTYWANIE
    (lch, lg) = wczytaj_z_klawiatury()
    wyswietl_parametry(lch, lg)

    # PLIKI WCZYTANIE
    (wartosci, wagi) = wczytaj_z_plikow(lg)
    waga_max = wagi[0]  # Ustalone z gory

    # TWORZENIE POPULACJI
    xp = popinit(lg, lch)

    # OCENIANIE POPULACJI
    (ocena_populacji, suma_wag_chromosomow) = ocena(xp, wartosci, wagi[1:])

    # POKAZYWANIE POPULACJI
    print("Populacja chromosomow:")
    for i, gen in enumerate(xp, 1):
        print(f"ch {i:02}: {gen}")
    print()

    # POKAZYWANIE WARTOSCI I WAGI
    print(f"Wartosci: {wartosci}")
    print(f"Wagi: {wagi[1:]}")  # Wykluczamy ograniczona wage
    print(f"{waga_max=}")

    # POKAZYWANIE WYNIKOW
    for i, (gen, ocena_ch, waga_ch) in enumerate(
        zip(xp, ocena_populacji, suma_wag_chromosomow), 1
    ):
        print(f"ch{i:02} -> {gen} = {ocena_ch} z waga: {waga_ch}")

    # PRZEPROWADZANIE TURNIEJU
    print("\n--> TURNIEJ <--")
    nrxp = rodzice(xp, ocena_populacji, suma_wag_chromosomow, waga_max)
    print("Indeksy chromosomow zwyciezcow turnieju: ")
    print(nrxp)
    print("Numery chromosomow zwyciezcow turnieju: ")
    print([i + 1 for i in nrxp])

    for nr in nrxp:
        print(
            f"ch {nr + 1:02}: ocena = {ocena_populacji[nr]}, waga = {suma_wag_chromosomow[nr]}"
        )

    # TWORZENIE PLIKI HISTORII
    # zrob_hist(ocena_populacji)
