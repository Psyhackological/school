package com.jetbrains;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in);

        System.out.println("+ Suma");
        System.out.println("- Roznica");
        System.out.println("* Iloczyn");
        System.out.println("/ Iloraz");
        System.out.print("Wybierz operacje: ");
        char wybor = inp.next().charAt(0);

        System.out.print("Liczba 1: ");
        double liczba1 = inp.nextDouble();

        System.out.print("Liczba 2: ");
        double liczba2 = inp.nextDouble();

        System.out.println();

        switch (wybor) {
            case '+' -> System.out.print("Suma to: " + (liczba1 + liczba2) );
            case '-' -> System.out.print("Roznica to: " + (liczba1-liczba2) );
            case '*' -> System.out.print("Iloczyn to: " + (liczba1*liczba2) );
            case '/' -> System.out.print( (liczba2==0) ? "Nie dziel przez 0!" : "Iloraz to: " + (liczba1/liczba2) );
            default -> System.out.print("Takiego dzialania nie ma!");
        }
		inp.close();
    }
}