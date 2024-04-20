package com.jetbrains;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in);

        System.out.print("Podaj 1 inta: ");
        int a = inp.nextInt();

        System.out.print("Podaj 2 inta: ");
        int b = inp.nextInt();

        System.out.print("Podaj 3 inta: ");
        int c = inp.nextInt();

        if(a>b && a>c) System.out.println("Najwieksza to a: " + a);
        else if(b>a && b>c) System.out.println("Najwieksza to b: " + b);
        else System.out.println("Najwieksza to c: " + c);
        inp.close();
    }
}