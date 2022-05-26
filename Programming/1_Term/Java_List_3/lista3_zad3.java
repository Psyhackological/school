package com.jetbrains;
import java.util.Random;

public class lista3_zad3
{
    public static int returnRandomInt(int lotto_range)
    {
        Random random = new Random();
        return random.nextInt(lotto_range) + 1;
    }

    // method overloading because why the hell not
    public static int returnRandomInt()
    {
        return returnRandomInt(49);
    }

    public static void Lotto()
    {
        int length = 6;
        int[] lotto = new int[length];

        // java by default fills the array with zeroes and has fixed sized
        // so my tasks is to replace each one of the zeroes
        int zeroes = length;
        int rnd;

        while(zeroes > 0)
        {
            // this actually speeds up the program because when you successfully set rnd to array
            // it is obvious that comparison between rnd and the same rnd is going to return true,
            // so it saves our program's time to think
            rnd = returnRandomInt();

            /* for loop counter could not be set to 0, so I had to switch to while loop where I can set my own counter
            for(int i = 0; length - zeroes > i; i++)
            {
                if(lotto[i] == rnd)
                {
                    rnd = returnLottoInt();
                }
            } */

            // iterations
            // first  | i = 0 | check 6 - 6 = 0 | 0 > i | elements: []
            // second | i = 0 | check 6 - 5 = 1 | 1 > i | elements: [0]
            // third  | i = 0 | check 6 - 4 = 2 | 2 > i | elements: [0, 1]
            // fourth | i = 0 | check 6 - 3 = 3 | 3 > i | elements: [0, 1, 2]
            // fifth  | i = 0 | check 6 - 2 = 4 | 4 > i | elements: [0, 1, 2, 3]
            // sixth  | i = 0 | check 6 - 1 = 5 | 5 > i | elements: [0, 1, 2, 4, 5]
            int start = 0;
            while(length - zeroes > start)
            {
                if(lotto[start] == rnd)
                {
                    rnd = returnRandomInt();
                    start = 0;
                    continue;
                }
                start++;
            }
            // found new unique random value
            lotto[length - zeroes] = rnd;

            // next iteration
            zeroes--;
        }


        for(int nr: lotto)
        {
            System.out.print(nr + " ");
        }
        System.out.println();
    }

    public static void main(String[] args)
    {
        for(int i = 0; 10 > i; i++)
        {
            Lotto();
        }
    }
}