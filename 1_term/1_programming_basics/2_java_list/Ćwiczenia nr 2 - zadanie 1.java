package com.jetbrains;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Collections;

public class Main
{
    public static void main(String[] args)
    {
        ArrayList<String> al = new ArrayList<>();
        LinkedList<String> ll = new LinkedList<>();

        System.out.println(al instanceof ArrayList);
        System.out.println(ll instanceof LinkedList);

        al.add("Adam");
        al.add("Bartek");
        al.add("Cezary");
        al.add("Daniel");
        al.add("Ewa");
        al.add("Filip");
        al.add("Gosia");
        al.add("Henryk");
        al.add("Izabella");
        al.add("Jacek");

        ll.add("Adam");
        ll.add("Bartek");
        ll.add("Cezary");
        ll.add("Daniel");
        ll.add("Ewa");
        ll.add("Filip");
        ll.add("Gosia");
        ll.add("Henryk");
        ll.add("Izabella");
        ll.add("Jacek");

        System.out.println();

        al.forEach(e -> System.out.println(e));

        System.out.println();

        ll.forEach(e -> System.out.println(e));

        System.out.println();

        System.out.println(al.get(0) + " " + al.get(1) + " " + al.get(2));
        System.out.println(al.get(7) + " " + al.get(8) + " " + al.get(9));

        System.out.println();

        System.out.println(ll.get(0) + " " + ll.get(1) + " " + ll.get(2));
        System.out.println(ll.get(7) + " " + ll.get(8) + " " + ll.get(9));

        System.out.println();

        al.add(4, "Imie na 5 pozycji");
        ll.add(4, "Imie na 5 pozycji");

        al.forEach(e -> System.out.println(e));

        System.out.println();

        ll.forEach(e -> System.out.println(e));

        System.out.println();

        for(int i=0; i<3; i++)
        {
            al.remove(0);
            al.remove(al.size()-1);
            ll.removeFirst();
            ll.removeLast();
        }

        al.forEach(e -> System.out.println(e));

        System.out.println();

        ll.forEach(e -> System.out.println(e));

        System.out.println();

        List<String> lista = List.of("Alpaka", "Bobr", "Cykada", "Daniel", "Emu", "Flaming");
        al.addAll(lista);

        al.forEach(e -> System.out.println(e));

        System.out.println();

        Collections.sort(al);
        al.forEach(e -> System.out.println(e));

        System.out.println();

        Collections.sort(al, Collections.reverseOrder());
        al.forEach(e -> System.out.println(e));
    }
}