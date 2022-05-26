# Podstawy programowania ćwiczenia nr 3

Tablice + losowanie

1.  Wylosuj liczbę z podanego zakresu i wyświetl ją (zakres min i max wpisuje użytkownik). (1 punkt).  

2. Napisz program, który losuje liczbę. Użytkownik ma za zadanie odgadnąć liczbę wylosowaną przez komputer z określonego zakresu. Program ma podpowiadać “za dużo”, “za mało” lub “odgadłeś za “+liczba_prób+”razem”.  

3. Napisz program, który losuje 6 liczb z zakresu 1..49 (używając tablic), liczby nie mogą się powtarzać.  

4. Napisz program, który pobiera od użytkownika 6 liczb z puli 49. Program ma wziąć pod uwagę zestaw unikalnych sześciu liczb. Następnie program dokonuje losowań do czasu gdy wylosuje wybrane przez użytkownika zestawienie liczb. Program podaje po ilu latach i ilu dniach użytkownik wylosowałby liczby (np. potrzeba x lat i x dni). Zakładamy że losowania odbywają się codziennie (jedno losowanie na jeden dzień). * (z zastosowanie tablic).  

5. Z ZASTOSOWANIEM KOLEKCJI: Napisz program, który pobiera od użytkownika 6 liczb z puli 49. Program ma wziąć pod uwagę zestaw unikalnych sześciu liczb. Następnie program dokonuje losowań do czasu gdy wylosuje wybrane przez użytkownika zestawienie liczb. Program podaje po ilu latach i ilu dniach użytkownik wylosowałby liczby (np. potrzeba x lat i x dni). Zakładamy że losowania odbywają się codziennie (jedno losowanie na jeden dzień). *  

6. W pliku NAPIS.TXT, w oddzielnych wierszach, znajduje się 1 000 napisów o długościach od 2 do 25 znaków. Każdy napis składa się z wielkich liter alfabetu łacińskiego. Wypisz napisy z pliku NAPIS.TXT, które występują w nim więcej niż jeden raz (każdy taki napis wypisz tylko raz).  

7. Napis rosnący to taki napis, w którym kod ASCII każdej kolejnej litery jest większy od kodu poprzedniej. Podaj wszystkie napisy rosnące występujące w pliku NAPIS.TXT  

Programowanie obiektowe:

1. Zaproponuj temat, który nadawałby się na utworzenie klasy (z wyjątkiem: Osoba, Pracownik, Auto). Utwórz klasę posiadającą przynajmniej 6 pól różnego typu.

2. Do klasy utwórz przynajmniej 3 konstruktory.

3. Skróć zapis przynajmniej jednego konstruktora by wywoływał inny konstruktor przez this

4. Utwórz metody dostępowe (getter, setter) dla pól klasy.

5. Utwórz 6 obiektów, wywołując różne konstruktory (nie zawsze znamy wartości pól obiektów w momencie ich tworzenia).

6. Ustaw za pomocą settera wartości pól, które nie były znane w momencie wywoływania konstruktora.

Podpowiedzi:

```java
String napis="To program do prezentacji char";

char[] tablicaChar;

tablicaChar = napis.toCharArray();

System.out.println(tablicaChar[0]); //wyświetli T

System.out.println((int)tablicaChar[0]); //wyświetli 84
```
