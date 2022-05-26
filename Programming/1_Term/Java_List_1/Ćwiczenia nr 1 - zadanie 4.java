package com.jetbrains;
import java.util.Scanner;
import java.util.Arrays;

public class Main
{
    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in);

        int[] tablica = new int[5];

        for(int i = 0; 5 > i; i++)
        {
            System.out.print("Podaj " + (i + 1) + " inta: ");
            tablica[i] = inp.nextInt();
        }

        Arrays.sort(tablica);
        System.out.println("Tablica w ascending order: " + Arrays.toString(tablica));
		inp.close();
    }
}