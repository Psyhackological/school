package com.jetbrains;
import java.util.Scanner;
import static java.lang.Math.*;

public class Main
{
    static double oblicz_V(double r)
    {
        return 4d/3d * PI * r * r * r;
    }

    static double oblicz_P(double r)
    {
        return 4 * PI * r * r;
    }

    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in);

        System.out.print("Podaj r: ");
        double r = inp.nextDouble();

        double V = oblicz_V(r);
        double P = oblicz_P(r);

        System.out.print("P wynosi: ");
        System.out.format("%.2f%n", P);
        System.out.print("V wynosi: ");
        System.out.format("%.2f", V);
		inp.close();
    }
}