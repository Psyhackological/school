# 1. Klasy i dziedziczenie

##### ZADANIA

1. Utwórz klasę Kwadrat. Klasa powinna posiadać:  
   • Konstruktor z jednym parametrem określającym długość boku kwadratu  
   • Prywatne pole przechowujące długość boku kwadratu  
   • Publiczną metodę zwracającą obwód kwadratu  
   • Publiczną metodę zwracającą pole powierzchni kwadratu  
   • Implementację metody przysłoniętej toString() która zwróci ciąg „Kwadrat:  
   długość_boku”  

2. Utwórz analogiczną klasę Prostokąt. Z tym, że konstruktor powinien zawierać dwa parametry oraz w klasie powinny być dwa pola do przechowywania długości obu boków.  

3. Zauważ, że klasy te mają takie same właściwości. W związku z tym utwórz klasę Figura,  
   który będzie posiadał:  
   • Publiczną metodę zwracającą obwód figury  
   • Publiczną metodę zwracającą pole powierzchni figury  
   Przerób klasy Prostokąt i Kwadrat tak aby dziedziczyły po klasie Figura.  

4. Co sądzisz o klasie Figura? Czy jest to porwana implementacji?  
   Zmodyfikuj program tak, żeby zamiast klasy Figura wykorzystywał interfejs IFigura.  

5. Utwórz od podstaw klasę Koło implementującą interfejs IFigura.  

6. Zmodyfikuj interfejs IFigura poprzez dodanie do niego definicji dwóch metod: Powiększ i Pomniejsz. Zaobserwuj co stało się z klasami implementującymi ten interfejs.  

7. Zaimplementuj metody Powiększ i Pomniejsz w każdej klasie implementującej interfejs  IFigura. Metody mają działać w taki sposób aby po ich wywołaniu pole powierzchni figury uległo zmniejszeniu lub zwiększeniu 2 raz. Uwaga, nie należy przechowywać w klasach wartości powierzchni, metody te powinny przeliczyć długości boków czy promień tak aby powierzchnia uległa zadanej zmianie.  

8. Zapoznaj się ze wzorcem projektowym fabryki.

9. Utwórz abstrakcyjną klasę fabryki FiguraFabryka dla IFIgura, posiadającą jedną metodę abstrakcyjną Utwórz.  
10. Utwórz klasę fabryki dla każdej z figur, która dziedziczy po klasie FiguraFabryka.  
11. Utwórz klasę Figura zawierającą słownik fabryk i metodę tworzącą odpowiednią figurę.  
12. Napisz program, który utworzy listę losowych figur z wykorzystaniem wcześniej  
    utworzonej fabryki. Program powinien posiadać menu tekstowe za pomocą, którego użytkownik będzie mógł wyświetlić listę figur, wyświetlić wybraną figurę, usunąć   wybraną figurę, dodać nową figurę, pomniejszyć wybraną figurę lub powiększyć wybraną figurę
