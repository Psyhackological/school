package com.jetbrains;
import java.util.Set;
import java.util.HashSet;
import java.util.TreeSet;

public class Main
{
    public static void main(String[] args)
    {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new TreeSet<>();

        for (int i = 1; 6 >= i; i++)
        {
            set1.add(i);
            if (i % 2 == 0) set2.add(i);
        }

        int count = 0;
        for(Integer e1: set1)
        {
            if(set2.contains(e1)) count++;
        }

        System.out.println("Set1 contains " + count + " elements of set2.\n");

        set1.forEach(e -> System.out.println(e));
        System.out.println();
        set2.forEach(e -> System.out.println(e));
        System.out.println();

        set1.addAll(set2);
        System.out.println(set1);

        set2.retainAll(set1);
        System.out.println(set2);

        set1.removeAll(set2);
        System.out.println(set1);
    }
}
