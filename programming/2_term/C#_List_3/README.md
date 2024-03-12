

# 3. Wątki

##### ZADANIA

1. Napisz program do obsługi własnej kolejki:
   a) Utwórz klasę MyQueue, która przechowuje tablicę wartości całkowitych o zadanym rozmiarze oraz udostępnia metodę void addValue(int a), która wprowadza wartość na ostatnią wolną pozycję tablicy oraz metodę int getValue(), która zwraca pierwszą wartość z tablicy i zwalnia jej miejsce.
   b) Utwórz klasę MyQueueAddThread, która jest wątkiem i co 8 sekund dodaje losową wartość do obiektu MyQueue. Przed wywołaniem metody addValue wyświetl wprowadzaną wartość. Zmodyfikuj metodę addValue, tak aby również wyświetlała wprowadzaną wartość.
   c) Napisz program, który posiada jedno wystąpienie klasy MyQueue oraz uruchamiał dwa wątki MyQueueAddThread.
   d) Utwórz klasę MyQueueGetThread, która jest wątkiem i co 3 sekundy wyświetla kolejne wartości przechowywane w klasie MyQueue. Zmodyfikuj metodę getValue,  tak aby również wyświetlała zwracaną wartość przed swoim zakończeniem.
   e) Zmodyfikuj program tak aby dodatkowo uruchamiał MyQueueGetThread jako trzeci wątek.
   f) Zmodyfikuj program, tak aby użytkownik mógł określić ile ma być wątków
   MyQueueAddThread i MyQueueGetThread. Przeprowadź analizę działania aplikacji dla przypadków:
   i) Są trzy wątki MyQueueAddThread i jeden wątki MyQueueGetThread
   ii) Są dwa wątki MyQueueAddThread i dwa wątki MyQueueGetThread
   g) Zmodyfikuj klasę MyQueue, tak aby jej metody obsługiwały przypadki gdy nie ma 
   wolnego miejsca na dodanie nowej wartości i nie ma wartości do zwrócenia.  

2. Napisz program obsługujący dostęp do muzeum z M miejscami dla zwiedzających i 2 bramami: wejściową i wyjściową oraz K chętnymi klientami do jego odwiedzenia, gdzie M << K
   
   Klienci wchodzą i wychodzą przez bram w celu obejrzenia wystawy. Z bram można korzystać pojedynczo. W muzeum może w danym momencie przebywać maksymalnie M klientów. Klient może być wpuszczony przez pierwszą bramę wówczas, gdy są jakieś wolne miejsca dla zwiedzających. Wyjście z wystawy odbywa się drugą bramą. Miejsca dla zwiedzających i bramy należy traktować jako współdzielone zasoby. Klienci natomiast są wątkami. Program wyświetla odpowiednie komunikaty o stanie aplikacji na konsoli
