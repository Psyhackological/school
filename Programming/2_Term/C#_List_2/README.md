# 2. Algorytmy

##### ZADANIA

1. Zaimplementować algorytm sortowania bąbelkowego (ang. bubble sort) i sortowania szybkiego (ang. quicksort). Zademonstruj i porównaj działanie obu algorytmów w prostym programie sortującym losowe tablice.  

2. Zaimplementować algorytm wyszukiwania zadanego wzorca w ciągu znaków. Następnie napisać prosty program, który umożliwi użytkownikowi wprowadzenie ciągu znaków oraz wzorca do wyszukiwania i wypisze wszystkie pozycje wystąpienia wzorca we wprowadzonym ciągu.  

3. Utwórz klasę Wielomian, która będzie reprezentowała wielomian n-stopnia:
   𝑊(𝑥) = 𝑎𝑛𝑥𝑛 + 𝑎𝑛−1𝑥𝑛−1 + ⋯ + 𝑎2𝑥𝑛2 + 𝑎1𝑥 + 𝑎0.
   Klasa powinna zawierać:
   • tablicę o rozmiarze n+1 do przechowywania współczynników wielomianu,
   • konstruktor jednoargumentowy do utworzenia nowego wielomianu n-stopnia,
   • bezargumentową metodę wypełniające tablicę współczynników losowymi
   wartościami,
   • metodę o zmiennej liczbie argumentów (varargs) wypełniające tablicę współczynników zadanymi wartościami,
   • metodę z jednym argumentem wyliczającą wartość wielomianu z wykorzystaniem algorytmu Hornera dla zadanej wartości. 
   Napisać prosty sekwencyjny, program ilustrujący wykorzystanie klasy i działanie wszystkich metod.  

4. Utworzyć klasy BinaryNode i BinaryTree, reprezentujące drzewo binarne.

Klasa BinaryNode reprezentuje wierzchołek i powinna zawierać:
• pole typu int przechowujące wartość/wagę wierzchołka,
• pole zawierające lewy liść,
• pole zawierające prawy liść,
• konstruktor jednoargumentowy, tworzący wierzchołek o zadanej wadze.
Klasa BinaryTree reprezentuje całe drzewo binarne i powinna zawierać:
• pole root typu BinaryNode zawierające korzeń drzewa,
• jednoargumentową metodę addNode dodająco nowy wierzchołek do drzewa według algorytmu:  

1) Jeżeli drzewo nie posiada korzenia to tworzony jest korzeń,  
2) Jeżeli drzewo posiada korzeń, to korzeń dodawany jest do kolejki sprawdzania,  
3) Zdejmowany jest pierwszy wierzchołek z kolejki sprawdzania,  
4) Jeżeli zdjęty wierzchołek posiada oba liście to dodawane są one do kolejki sprawdzania w kolejności lewy i prawy i wracamy do pkt. 3),  
5) Jeżeli zdjęty wierzchołek nie posiada żadnego liścia to nowy wierzchołek dodawany jest jako lewy liść, a jeżeli wierzchołek posiada tylko jeden liść to nowy liść dodawany jest na wolnej pozycji.
   Uwaga: przy tak skonstruowanym algorytmie nie powinna wystąpić sytuacji, że wierzchołek posiada prawy liść na nie posiada lewego.
   • Metodę zwracającą wartości wierzchołków jako listę w kolejności przechodzenia pre-order (przejście wzdłużne, VLR), czyli najpierw pobierana jest wartość   wierzchołka a następnie przechodzimy na lewy a potem na prawy liść. Należy  zastosować algorytm rekurencyjny,
   • Metodę zliczającą ilość wierzchołków w drzewie,
   • Metodę zliczającą ilość poziomów w drzewie,
   • Metodę wyliczającą wartość całego drzewa jako sumę wartości wszystkich wierzchołków,
   • Metodę zwracającą minimalną wartość wierzchołka,
   • Metodę zwracającą maksymalną wartość wierzchołka.
   Napisać prosty sekwencyjny, program ilustrujący wykorzystanie klas i działanie wszystkich metod poprzez utworzenie losowego drzewa.
