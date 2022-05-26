package com.jetbrains;
import java.util.Random;
import java.util.Scanner;

public class lista3_zad1
{
    public static int returnRnd(int min, int max)
    {
        if(min > max)
        {
            int temp = min;
            min = max;
            max = temp;
        }

        Random random = new Random();
        return random.nextInt(max - min) + min;
        //max - min to zakres
        // + min to jest dodawanie dodatniej lub odejmowanie dodatniej
    }

    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in);

        System.out.print("Min: ");
        int min = inp.nextInt();

        System.out.print("Max: ");
        int max = inp.nextInt();

        System.out.println(returnRnd(min, max));
    }
}