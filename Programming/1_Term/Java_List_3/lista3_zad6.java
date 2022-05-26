package com.jetbrains;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Map;
import java.util.TreeMap;

public class lista3_zad6
{
    public static void main(String[] args) throws FileNotFoundException
    {
        File file = new File("NAPIS.txt");
        Scanner inp = new Scanner(file);
        HashSet<String> napisy = new HashSet<>();
        Map<Integer, String> mapka = new TreeMap<>();

        String napis;
        int linia = 0;
        while(inp.hasNextLine())
        {
            linia++;
            napis = inp.nextLine();
            if( !napisy.add(napis) ) mapka.put(linia, napis);
        }
        inp.close();

        System.out.println("Duplikaty: ");
        // for(type variableName : array / collection)
        // Map.Entry = key-value pair                    | type
        // m = element of key-value pair                 | variable name
        // mapka.entrySet() = create entrySet from mapka | array / collection
        for(Map.Entry m : mapka.entrySet())
        {
            System.out.println(m.getKey() + " " + m.getValue());
        }

    }
}