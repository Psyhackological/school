package com.jetbrains;
import java.util.Scanner;
import java.util.Locale;

public class Main
{
    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in).useLocale(Locale.US);

        double suma = 0;

        for(int i = 0; 8 > i; i++)
        {
            System.out.print("Podaj " + (i + 1) + " zmiennoprzecinkowa (z .): ");
            suma += inp.nextDouble();
        }

        System.out.print("Srednia tych liczb to: " + suma/8.0);
        inp.close();
    }
}