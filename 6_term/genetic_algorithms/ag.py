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

    ocena_populacji = np.sum(xp * wartosc, axis=1)
    waga_chromosomu = np.sum(xp * waga, axis=1)

    return (ocena_populacji, waga_chromosomu)


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
    lpop = int(input("Podaj liczbe pokolen (max. 500): "))
    lpop = min(lpop, 500)  # (max. 500)

    # Prawdopodobienstwo populacji
    pm = float(input("Podaj prawdopodobienstwo mutacji (0 - 0.1): "))
    pm = min(lpop, 0.1)  # (max. 0.1)

    # Prawdopodobienstwo populacji
    pk = float(input("Podaj prawdopodobienstwo krzyzowania (0.6 - 1.0): "))
    pk = min(lpop, 0.8)  # (max. 1.0 ale wzialem srodek)

    return (lch, lg, lpop, pm, pk)


def wyswietl_parametry(lch, lg, lpop, pm, pk):
    """
    Wyswietla parametry algorytmu genetycznego.

    Argumenty:
        lch (int): Liczba chromosomow w populacji.
        lg (int): Liczba genow w chromosomie.
        lpop (int): Liczba pokolen.
        pm (float): Prawdopodobienstwo mutacji.
        pk (float): Prawdopodobienstwo krzyzowania.
    """
    print("\nWybrane parametry:")
    print(f"{lch = }")
    print(f"{lg = }")
    print(f"{lpop = }")
    print(f"{pm = }")
    print(f"{pk = }\n")


def zapis(
    iteracja,
    ocena_populacji,
    najlepszy_chromosom,
    najlepsza_ocena,
    najlepsza_waga,
    znaleziono_nowy_najlepszy,
    nazwa_pliku="hist_45430.dat",
):
    """
    Zapisuje podstawowe statystyki oceny populacji do pliku.
    Argumenty:
        ocena_populacji (np.array): Oceny chromosomow w populacji.
        xp (np.array): Populacja chromosomow.
        iteracja (int): Numer iteracji.
        nazwa_pliku (str): Nazwa pliku do zapisu. Domyslnie 'hist_45430.dat'.
    """

    min_fp = round(np.min(ocena_populacji))
    max_fp = round(np.max(ocena_populacji))
    srednia_fp = round(np.mean(ocena_populacji), 2)

    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(
            f"i={iteracja:03d}; min_fp={min_fp:03d}; max_fp={max_fp:03d}; srednia_fp={srednia_fp:.2f}"
        )
        if najlepszy_chromosom is not None and znaleziono_nowy_najlepszy is True:
            f.write(
                f"; najlepszy_ch={najlepszy_chromosom.tolist()}; fp={najlepsza_ocena}; waga={najlepsza_waga:.2f}"
            )
        f.write("\n")


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
            # print(
            #     f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{wybrany + 1:02} wygral: wagi {waga_ch1, waga_ch2} > {waga_max}, ch{wybrany + 1:02} blizej waga_max."
            # )

        # ch1 jest ponizej wagi_max, a ch2 powyzej
        elif waga_ch1 <= waga_max < waga_ch2:
            wybrany = ch1
            # print(
            #     f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{ch1 + 1:02} wygral: waga ch{ch1 + 1} = {waga_ch1} <= {waga_max}, waga ch{ch2 + 1:02} = {waga_ch2} > {waga_max}."
            # )

        # ch2 jest ponizej wagi_max, a ch1 powyzej
        elif waga_ch2 <= waga_max < waga_ch1:
            wybrany = ch2
            # print(
            #     f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{ch2 + 1:02} wygral: waga ch{ch2 + 1} = {waga_ch2} <= {waga_max}, waga ch{ch1 + 1:02} = {waga_ch1} > {waga_max}."
            # )

        # pojedynek ocen
        else:
            wybrany = ch1 if ocena_populacji[ch1] > ocena_populacji[ch2] else ch2
            # if wybrany == ch1:
            #     print(
            #         f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{ch1 + 1} wygral: wagi ({waga_ch1}, {waga_ch2}) <= {waga_max}, oceny ch{ch1 + 1} = {ocena_populacji[ch1]} > {ocena_populacji[ch2]} (ocena ch{ch2 + 1})."
            #     )
            # else:
            #     print(
            #         f"ch{ch1 + 1:02} vs ch{ch2 + 1:02} -> ch{ch2 + 1} wygral: wagi ({waga_ch1}, {waga_ch2}) <= {waga_max}, oceny ch{ch2 + 1} = {ocena_populacji[ch2]} > {ocena_populacji[ch1]} (ocena ch{ch1 + 1})."
            #     )

        nrxp.append(wybrany)

    return nrxp


def mutuj(xp, pm):
    """
    Mutuje populacje chromosomow, informujac o prawdopodobienstwie mutacji kazdego genu
    oraz pokazujac stan chromosomu przed i po mutacji.

    Argumenty:
        xp (np.array): Populacja chromosomow.
        pm (float): Prawdopodobienstwo mutacji dla kazdego genu.

    Zwraca:
        np.array: Zmutowana populacja.
    """
    # Przechodzimy przez kazdy chromosom w populacji
    for i, chromosom in enumerate(xp, 1):
        # print(f"\nch{i:02} przed mutacja: {chromosom}")
        # Przechodzimy przez kazdy gen w chromosomie
        for j, gen in enumerate(chromosom):
            p = np.random.random()  # Generujemy losowe prawdopodobienstwo
            if p < pm:  # Sprawdzamy, czy mutacja ma zajsc
                # print(
                #     f"  g{j+1}: pm = {p:.2f} < {pm:.2f}, wiec {chromosom[j]} --> {chromosom[j] ^ 1}"
                # )
                # Uzycie operatora XOR do zmiany wartosci genu
                chromosom[j] ^= 1
            # else:
            #     print(f"  g{j+1}: pm = {p:.2f}")

        # print(f"ch{i:02} po mutacji: {chromosom}")

    return xp


def potomek(xp, pk):
    """
    Wykonuje krzyzowanie (crossover) pomiedzy chromosomami rodzicielskimi.

    Argumenty:
        xp (np.array): Populacja chromosomow.
        pk (float): Prawdopodobienstwo krzyzowania.

    Zwraca:
        np.array: Populacja po krzyzowaniu.
    """
    lg = xp.shape[1]
    xp_kopia = xp.copy()

    for i in range(0, lg - 1, 2):
        p = np.random.random()
        if p >= pk:
            punkt_ciecia = np.random.randint(1, xp.shape[0] - 1)
            print(
                f"\nPara rodzicow: {i+1} i {i+2}, punkt ciecia: {punkt_ciecia}")
            print(
                f"Rodzice przed krzyzowaniem: ch{i+1}: {xp[:, i]}, ch{i+2}: {xp[:, i+1]}"
            )
            # Krzyzowanie jednopunktowe
            xp_kopia[punkt_ciecia:, i], xp_kopia[punkt_ciecia:, i + 1] = (
                xp[punkt_ciecia:, i + 1],
                xp[punkt_ciecia:, i],
            )
            print(
                f"Rodzice po krzyzowaniu: ch{i+1}: {xp_kopia[:, i]}, ch{i+2}: {xp_kopia[:, i+1]}"
            )

    return xp_kopia


# Nie wywoluje, pozostalosc po starym debugu
def debug(xp, ocena_populacji, suma_wag_chromosomow, wartosci, wagi, waga_max):
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


# WYKONYWANIA SKRYPTU GLOWNEGO
if __name__ == "__main__":
    # Wczytanie parametrow algorytmu z klawiatury
    (lch, lg, lpop, pm, pk) = wczytaj_z_klawiatury()
    wyswietl_parametry(lch, lg, lpop, pm, pk)

    # Wczytanie danych z plikow
    (wartosci, wagi) = wczytaj_z_plikow(lg)
    waga_max = wagi[0]  # Maksymalna dozwolona waga chromosomu

    # Inicjalizacja populacji
    xp = popinit(lg, lch)
    ocena_populacji, suma_wag_chromosomow = ocena(xp, wartosci, wagi[1:])

    najlepszy_chromosom = None
    najlepsza_ocena = 0
    najlepsza_waga = 0
    najlepsza_iteracja = 0
    znaleziono_nowy_najlepszy = False

    with open("hist_45430.dat", "w", encoding="utf-8") as f:
        f.write(
            "iteracja;min_fp;max_fp;srednia_fp;najlepszy_chromosom;najlepsza_ocena;najlepsza_waga\n"
        )

    # Glowna petla algorytmu
    for i in range(1, lpop + 1):
        print(f"\nIteracja {i}")

        # Selekcja rodzicow
        indeksy_rodzicow = rodzice(
            xp, ocena_populacji, suma_wag_chromosomow, waga_max)
        xp = xp[indeksy_rodzicow]

        # Mutacja
        xp = mutuj(xp, pm)

        # Krzyzowanie
        xp = potomek(xp, pk)

        # Ocenianie populacji
        (ocena_populacji, suma_wag_chromosomow) = ocena(xp, wartosci, wagi[1:])

        # Aktualizacja najlepszego rozwiazania
        max_ocena_iteracji = np.max(ocena_populacji)
        max_index = np.argmax(ocena_populacji)
        if (
            max_ocena_iteracji > najlepsza_ocena
            and suma_wag_chromosomow[max_index] <= waga_max
        ):
            najlepsza_ocena = max_ocena_iteracji
            najlepszy_chromosom = xp[max_index]
            najlepsza_waga = suma_wag_chromosomow[max_index]
            najlepsza_iteracja = i
            znaleziono_nowy_najlepszy = True

        zapis(i, ocena_populacji, najlepszy_chromosom,
              najlepsza_ocena, najlepsza_waga, znaleziono_nowy_najlepszy)

        znaleziono_nowy_najlepszy = False

    # Wyswietlenie najlepszego rozwiazania
    print(f"Najlepszy chromosom: {najlepszy_chromosom}")
    print(
        f"Najlepsza wartosc funkcji przystosowania: {najlepsza_ocena} w iteracji {najlepsza_iteracja}"
    )
    print(f"Waga najlepszego chromosomu: {najlepsza_waga}")
