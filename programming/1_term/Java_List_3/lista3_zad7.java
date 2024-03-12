package com.jetbrains;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class lista3_zad7
{
    public static void main(String[] args) throws FileNotFoundException
    {
        File file = new File("NAPIS.txt");
        Scanner inp = new Scanner(file);

        String napis;
        int linia = 0;
        boolean asc;
        while(inp.hasNextLine())
        {
            linia++;
            napis = inp.nextLine();
            asc = true;
            // checking if napis is ascending string in ascii
            for(int i = 0; napis.length() - 1 > i; i++)
            {
                char a1 = napis.charAt(i);
                char a2 = napis.charAt(i+1);

                if ( (int) a1 >= (int) a2 )
                {
                    asc = false;
                    break;
                }
            }

            // we assumed that is true and if our checking failed this going to be true
            if(asc)
            {
                System.out.println(linia + " " + napis);
                for(int i = 0; napis.length() > i; i++)
                {
                    char c = napis.charAt(i);
                    if(i != napis.length() - 1) System.out.print((int) c + " < ");
                    else System.out.print((int) c);
                }
                System.out.println();
                System.out.println();
            }
        }

        inp.close();
    }
}