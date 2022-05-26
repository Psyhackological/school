package com.jetbrains;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in);

        System.out.print("Podaj cene towaru (max 50 000): ");
        double cena = inp.nextDouble();

        if(cena > 50000 || cena < 1)
        {
            while(cena > 50000 || cena < 1)
            {
                System.out.println("Podaj cene towaru (max 50 000): ");
                cena = inp.nextDouble();
            }
        }

        System.out.print("Podaj liczbe rat (max 48): ");
        int raty = inp.nextInt();

        if(raty > 48 || raty < 1)
        {
            while(raty > 48 || raty < 1)
            {
                System.out.println("Podaj liczbe rat (max 48): ");
                raty = inp.nextInt();
            }
        }

        double proc;

        if(raty < 12) proc = 1.03;
        else if (raty < 24) proc = 1.06;
        else proc = 1.1;

        System.out.println("Cena z %: " + cena * proc);
        System.out.println("Mieszieczna rata: " + cena * proc / raty);
		inp.close();
    }
}