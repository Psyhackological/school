package com.jetbrains;
import java.util.Random;
import java.util.Scanner;
import java.util.Map;
import java.util.TreeMap;


public class Main
{
    public static int returnRnd(int X)
    {
        Random random = new Random();
        return random.nextInt(X) + 1;
    }

    public static void generateRndInts(int X, int Y)
    {
        Map<Integer, Integer> mapka = new TreeMap<>();

        int rnd_int;
        for(int i = 0; Y > i; i++)
        {
            rnd_int = returnRnd(X);
            if (mapka.get(rnd_int) == null) mapka.put(rnd_int, 1);
            else mapka.put(rnd_int, mapka.get(rnd_int) + 1);
        }

        System.out.print(mapka);
    }

    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in);

        System.out.print("Przedzial od 1 do: ");
        int X = inp.nextInt();

        System.out.print("Generuj liczb: ");
        int Y = inp.nextInt();

        generateRndInts(X, Y);
    }
}