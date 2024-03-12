package com.jetbrains;
import java.util.Random;
import java.util.Scanner;

public class lista3_zad2
{
    public static int returnRnd()
    {
        Random random = new Random();
        return random.nextInt(100) + 1;
    }

    public static void main(String[] args)
    {
        System.out.println("Wylosowalem losowa liczbe od 1 do 100: ");

        int rnd = returnRnd();
        int proby = 0;
        int strzal;

        Scanner inp = new Scanner(System.in);

        while (true)
        {
            System.out.print("Twoj strzal (1-100): ");
            strzal = inp.nextInt();
            if(strzal == rnd) break;
            System.out.println((strzal > rnd) ? "Za duzo!" : "Za malo!");
            proby++;
        }

        System.out.println("\nWygrales w " + proby + " probach!");
    }
}