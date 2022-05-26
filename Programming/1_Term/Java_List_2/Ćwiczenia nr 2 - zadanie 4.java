package com.jetbrains;
import java.util.ArrayList;
import java.util.Iterator;

class Osoba
{
    private final String imie;

    public Osoba(String i)
    {
        this.imie = i;
    }

    public String getImie() {
        return imie;
    }
}

public class Main
{
    public static void main(String[] args)
    {
        Osoba[] osoby = new Osoba[5];
        osoby[0] = new Osoba("Agnieszka");
        osoby[1] = new Osoba("Kamil");
        osoby[2] = new Osoba("Konrad");
        osoby[3] = new Osoba("Maciej");
        osoby[4] = new Osoba("Asia");

        ArrayList<String> imiona = new ArrayList<>();

        imiona.add(osoby[0].getImie());
        imiona.add(osoby[1].getImie());
        imiona.add(osoby[2].getImie());
        imiona.add(osoby[3].getImie());
        imiona.add(osoby[4].getImie());

        System.out.println("Przed: ");
        imiona.forEach(e -> System.out.println(e));
        System.out.println();

        Iterator<String> iter = imiona.iterator();

        String imie;
        while(iter.hasNext())
        {
            imie = iter.next();
            if (imie.charAt(0) == 'A') iter.remove();
        }

        System.out.println("Po: ");
        imiona.forEach(e -> System.out.println(e));
    }
}