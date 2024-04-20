package com.jetbrains;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner inp = new Scanner(System.in);

        System.out.print("Podaj imie: ");
        String imie = inp.nextLine();

        System.out.print("Hello " + imie +"!");
        inp.close();
    }
}