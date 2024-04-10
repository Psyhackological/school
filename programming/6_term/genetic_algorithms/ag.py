import numpy as np


def popinit(lg, lch):
    """
    Inicjalizuje populację chromosomów z losowymi genami.

    lg - liczba genów w chromosomie,
    lch - liczba chromosomów w populacji.
    """
    # Tworzenie odpowiedniego matrixa skladajacych sie z odpowiedniego rozmiaru w size z 0 i 1
    xp = np.column_stack(
        (np.zeros(lch), np.random.randint(2, size=(lch, lg)))
    )
    return xp


def ocena(xp, wartosc, waga, waga_max):
    """
    Ocenia populację, uwzględniając ograniczenie na sumę wag.

    xp - populacja,
    wartosc - wartości poszczególnych genów,
    waga - waga poszczególnych genów,
    waga_max - maksymalna dozwolona suma wag.
    """
    ocena_populacji = []
    waga_chromosomu = []

    for chromosom in xp:
        suma_wag = np.sum(chromosom[1:] * waga)
        if suma_wag <= waga_max:
            fp = np.sum(chromosom[1:] * wartosc)
        else:
            fp = 0
        ocena_populacji.append(fp)
        waga_chromosomu.append(suma_wag)

    return (np.array(ocena_populacji), np.array(waga_chromosomu))


def wczytaj_z_plikow(lg, plik_waga="wag1.txt", plik_wartosci="wart1.txt"):
    wartosci = np.loadtxt("wart1.txt")[:lg]
    # Dodajemy 1 bo musi sie shape zgadzac po waga_max
    wagi = np.loadtxt("wag1.txt")[:lg + 1]
    return wartosci, wagi


def wczytaj_z_klawiatury():
    # Liczba chromosomów w populacji
    lch = int(input("Podaj liczbe chromosomow w populacji (max. 50): "))
    lch = min(lch, 50)  # (max. 50)
    # Liczba genów w chromosomie
    lg = int(input("Podaj maksymalna dlugosc chromosomu (max. 10): "))
    lg = min(lg, 10)  # (max. 10)

    # Liczba pokoleń
    lpop = int(input("Podaj liczbe pokolen (max. 500): "))
    lpop = min(lpop, 500)  # (max. 500)

    # pm - prawdopodobieństwo zajścia mutacji (0. – 0.1)
    pm = float(input("Podaj prawdopodobieństwo zajscia mutacji (0. – 0.1): "))
    pm = min(pm, 0.1)  # Gdy bedzie za duzo wezmiemy 0.1

    # prawdopodobieństwo zajścia krzyżowania (0.6 – 1.0)
    pk = float(input("Podaj prawdopodobieństwo zajscia krzyzowania (0.6 – 1.0): "))
    pk = min(pk, 0.8)  # Gdy bedzie za duzo wezmiemy cos po srodku

    return (lch, lg, lpop, pm, pk)


def wyswietl_parametry(lch, lg, lpop, pm, pk):
    print()
    print("Wybrane parametry:")
    print(f"{lch = }")
    print(f"{lg = }")
    print(f"{lpop = }")
    print(f"{pm = }")
    print(f"{pk = }")
    print()


# Glowne wykonywanie sie skryptu
if __name__ == "__main__":
    # Wczytywanie wartosci z klawiatury
    (lch, lg, lpop, pm, pk) = wczytaj_z_klawiatury()
    wyswietl_parametry(lch, lg, lpop, pm, pk)

    # Wczytywanie wartosci i wagi z plikow
    wartosci, wagi = wczytaj_z_plikow(lg)

    # Maksymalna waga to 1 element z pliku wag1.txt
    waga_max = wagi[0]
    print(f"max waga: {waga_max}")

    xp = popinit(lg, lch)
    (ocena_populacji, wagi_chromosomow) = ocena(
        xp, wartosci, wagi[1:], waga_max)  # Wykluczamy element 0 bo to waga_max

    print("Populacja chromosomow:")
    for i, chromosom in enumerate(xp, 1):
        print(f"ch {i:02}: {chromosom}")

    print("\nWartosci przystosowania i wagi chromosomow:")
    for i, (ocena_chromosomu, waga_chromosomu) in enumerate(
        zip(ocena_populacji, wagi_chromosomow), 1
    ):
        print(
            f"ch {i:02}: przystosowanie = {ocena_chromosomu}, waga = {waga_chromosomu}"
        )

    print("\nWyniki:")
    for i, (chromosom, wart_przyst, w_chr) in enumerate(
        zip(xp, ocena_populacji, wagi_chromosomow), 1
    ):
        chr_str = " ".join(str(gen) for gen in chromosom)
        print(f"ch {i:02} - {chr_str} = {wart_przyst} (waga: {w_chr})")
