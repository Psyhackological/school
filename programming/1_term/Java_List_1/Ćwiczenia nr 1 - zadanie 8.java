package com.jetbrains;
import java.util.Scanner;

public class Main
{
    /* REKURENCJA
    public static long fib_r(int n)

    {
        if(n==1 || n==2) return 1;
        else return fib(n-1) + fib(n-2);
    }
    */

    public static void fib(int n)
    {
        long f1 = 1;
        long f2 = 1;
        long temp;

        System.out.println("Wyraz nr " + 1 + " to: " + f1);
        System.out.println("Wyraz nr " + 2 + " to: " + f2);

        for(int i=3; n>=i; i++)
        {
            temp = f2;
            f2 += f1;
            f1 = temp;
            System.out.println("Wyraz nr " + i + " to: " + f2);
        }
    }

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Podaj ile n wyrazow: ");
        int ile = input.nextInt();
        
        /* Dla rekursji
        for(int i=1; ile >= i; i++)
        {
            System.out.println("Wyraz nr " + i + " to: " + fib_r(i));
        }
        */

        fib(ile);

        input.close();
    }
}