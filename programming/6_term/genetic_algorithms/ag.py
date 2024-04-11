import numpy as np


def popinit(lg, lch):
    """
    Inicjalizuje populację chromosomów z losowymi genami.
    Argumenty:
        lg (int): Liczba genów w chromosomie.
        lch (int): Liczba chromosomów w populacji.
    Zwraca:
        np.array: Populacja chromosomów.
    """
    # Tworzenie odpowiedniego matrixa skladajacych sie z odpowiedniego rozmiaru w size z 0 i 1
    xp = np.column_stack((np.zeros(lch), np.random.randint(2, size=(lch, lg))))

    return xp


def ocena(xp, wartosc, waga, waga_max):
    """
    Ocenia populację, uwzględniając ograniczenie na sumę wag.
    Argumenty:
        xp (np.array): Populacja.
        wartosc (np.array): Wartości poszczególnych genów.
        waga (np.array): Waga poszczególnych genów.
        waga_max (float): Maksymalna dozwolona suma wag.
    Zwraca:
        tuple: Ocena populacji oraz waga chromosomów.
    """
    ocena_populacji = []
    waga_chromosomu = []

    for chromosom in xp:
        suma_wag = np.sum(chromosom[1:] * waga)
        fp = np.sum(chromosom[1:] * wartosc)
        ocena_populacji.append(fp)
        waga_chromosomu.append(suma_wag)

    return (np.array(ocena_populacji), np.array(waga_chromosomu))


def wczytaj_z_plikow(lg, plik_waga="wag1.txt", plik_wartosci="wart1.txt"):
    """
    Wczytuje wartości i wagi z plików.

    Argumenty:
        lg (int): Liczba genów w chromosomie.
        plik_waga (str, optional): Ścieżka do pliku z wagami. Domyślnie "wag1.txt".
        plik_wartosci (str, optional): Ścieżka do pliku z wartościami. Domyślnie "wart1.txt".

    Zwraca:
        tuple: Krotka zawierająca wartości i wagi.
    """
    wartosci = np.loadtxt("wart1.txt")[:lg]
    # Dodajemy 1 bo musi sie shape zgadzac po waga_max
    wagi = np.loadtxt("wag1.txt")[:lg+1]

    return wartosci, wagi


def wczytaj_z_klawiatury():
    """
    Wczytuje parametry algorytmu genetycznego od użytkownika.

    Zwraca:
        tuple: Krotka zawierająca wczytane parametry: liczba chromosomów (lch),
               liczba genów w chromosomie (lg), liczba pokoleń (lpop),
               prawdopodobieństwo mutacji (pm), prawdopodobieństwo krzyżowania (pk).
    """
    # Liczba chromosomów w populacji
    lch = int(input("Podaj liczbe chromosomow w populacji (max. 50): "))
    lch = min(lch, 50)  # (max. 50)

    # Liczba genów w chromosomie
    lg = int(input("Podaj maksymalna dlugosc chromosomu (max. 10): "))
    lg = min(lg, 10)  # (max. 10)

    # Liczba pokoleń
    # lpop = int(input("Podaj liczbe pokolen (max. 500): "))
    # lpop = min(lpop, 500)  # (max. 500)

    # pm - prawdopodobieństwo zajścia mutacji (0. – 0.1)
    # pm = float(input("Podaj prawdopodobieństwo zajscia mutacji (0. – 0.1): "))
    # pm = min(pm, 0.1)  # Gdy bedzie za duzo wezmiemy 0.1

    # prawdopodobieństwo zajścia krzyżowania (0.6 – 1.0)
    # pk = float(input("Podaj prawdopodobieństwo zajscia krzyzowania (0.6 – 1.0): "))
    # pk = min(pk, 0.8)  # Gdy bedzie za duzo wezmiemy cos po srodku

    return (lch, lg)


def wyswietl_parametry(lch, lg):
    """
    Wyświetla parametry algorytmu genetycznego.

    Argumenty:
        lch (int): Liczba chromosomów w populacji.
        lg (int): Liczba genów w chromosomie.
        lpop (int): Liczba pokoleń.
        pm (float): Prawdopodobieństwo mutacji.
        pk (float): Prawdopodobieństwo krzyżowania.
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
    min_fp = np.min(ocena_populacji)
    max_fp = np.max(ocena_populacji)
    srednia_fp = np.mean(ocena_populacji)

    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(
            f"{min_fp},{max_fp},{srednia_fp}, wartości zmiennych decyzyjnych.\n")


# WYKONYWANIA SKRYPTU GLOWNEGO
if __name__ == "__main__":
    # KLAWIATURA WCZYTYWANIE
    (lch, lg) = wczytaj_z_klawiatury()
    wyswietl_parametry(lch, lg)

    # PLIKI WCZYTANIE
    wartosci, wagi = wczytaj_z_plikow(lg)
    waga_max = wagi[0]  # Ustalone z gory
    print(f"{waga_max=}")

    # TWORZENIE POPULACJI
    xp = popinit(lg, lch)
    nrxp = range(1, len(xp) + 1)

    # OCENIANIE POPULACJI
    (ocena_populacji, suma_wag_chromosomow) = ocena(
        xp, wartosci, wagi[1:], waga_max  # Wykluczamy element 0 bo to waga_max
    )

    # POKAZYWANIE POPULACJI
    print("Populacja chromosomow:")
    for i, gen in zip(nrxp, xp):
        print(f"ch {i:02}: {gen}")
    print()

    # POKAZYWANIE WARTOSCI I WAGI
    print(f"Wartosci: {wartosci}")
    print(f"Wagi: {wagi[1:]}")  # Wykluczamy ograniczona wage

    # POKAZYWANIE WYNIKOW
    for (i, gen, ocena_ch, waga_ch) in zip(nrxp, xp, ocena_populacji, suma_wag_chromosomow):
        print(f"ch{i:02} -> {gen} = {ocena_ch} z waga: {waga_ch}")

    # TWORZENIE PLIKI HISTORII
    # zrob_hist(ocena_populacji)
