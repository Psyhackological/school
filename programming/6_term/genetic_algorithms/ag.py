import numpy as np


def popinit(lg, lch):
    # lg - liczba genow, lch - liczba chromosomow
    stworzona_populacja = np.column_stack(
        (np.zeros(lch), np.random.randint(2, size=(lch, lg)))
    )
    return stworzona_populacja


def ocena(xp, wartosc, waga, waga_max):
    # Ocena populacji z uwzglednieniem ograniczenia na sume wag
    ocena_populacji = []
    waga_chromosomu = []

    for chromosom in xp:
        # Obliczanie sumy wag dla chromosomu pomijajac gen o indeksie 0
        suma_wag = np.sum(chromosom[1:] * waga)
        # Sprawdzanie czy suma wag genow nie przekracza maksymalnej dopuszczalnej wagi
        if suma_wag <= waga_max:
            # Obliczanie funkcji przystosowania jesli warunek wagi jest spelniony
            fp = np.sum(chromosom[1:] * wartosc)
        else:
            # Ustawienie funkcji przystosowania na 0  jesli suma wag przekracza maksymalna dopuszczalna wage
            fp = 0
        ocena_populacji.append(fp)
        waga_chromosomu.append(suma_wag)

    ocena_wynik = np.array(ocena_populacji), np.array(waga_chromosomu)
    return ocena_wynik


# Glowny program
if __name__ == "__main__":
    lch = int(input("Podaj liczbe chromosomow w populacji: "))
    lg = int(input("Podaj maksymalna dlugosc chromosomu: "))

    # Wczytywanie danych z plikow z ograniczeniem do dlugosci lg
    wartosc = np.loadtxt("wart1.txt")[:lg]
    # Wczytywanie wag z przesunieciem 1
    waga = np.loadtxt("wag1.txt")[1: lg + 1]
    # Pierwszy element to maksymalna dopuszczalna suma wag
    waga_max = np.loadtxt("wag1.txt")[0]
    print(f"Max waga: {waga_max}")

    # Inicjalizacja populacji
    chromosomy = popinit(lg, lch)

    # Ocena populacji z uwzglednieniem ograniczenia wagi
    ocena_populacji, wagi_chromosomow = ocena(
        chromosomy, wartosc, waga, waga_max)

    # Wyswietlanie stworzonej populacji chromosomow
    print("Populacja chromosomow:")
    for i, chromosom in enumerate(chromosomy, 1):
        print(f"ch {i:02}: {chromosom}")

    print("\nWartosci przystosowania i wagi chromosomow:")
    for i, (ocena_chromosomu, waga_chromosomu) in enumerate(
        zip(ocena_populacji, wagi_chromosomow), 1
    ):
        print(
            f"ch {i:02}: przystosowanie = {ocena_chromosomu}, waga = {waga_chromosomu}"
        )

    # Wydruk wynikow
    print("\nWyniki:")
    for i, (chromosom, wart_przyst, w_chr) in enumerate(
        zip(chromosomy, ocena_populacji, wagi_chromosomow), 1
    ):
        chr_str = " ".join(str(gen) for gen in chromosom)
        print(f"ch {i:02} - {chr_str} = {wart_przyst} (waga: {w_chr})")
