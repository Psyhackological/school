using System.Diagnostics;

namespace Sortowanie
{
    public class Program
    {
        public static void Main()
        {
            Random random = new Random();
            Stopwatch stopwatch = new Stopwatch();

            int len = 20000;

            int[] tab1 = new int[len];
            int[] tab2 = new int[len];

            for (int i = 0; i < len; i++)
            {
                tab1[i] = random.Next(-1000, 1001);
                tab2[i] = tab1[i];
            }

            /* Console.WriteLine("Tablica przed sortowaniem:");

            for (int i = 0; i < tab1.Length; i++)
            {
                Console.Write(tab1[i] + " ");
            } */

            stopwatch.Start();
            Sort.BubbleSort(tab1);
            stopwatch.Stop();
            
            /* Console.WriteLine("\n\nTablica po sortowaniu BubbleSort:");

            for (int i = 0; i < tab1.Length; i++)
            {
                Console.Write(tab1[i] + " ");
            } */

            Console.Write($"Sortowanie {len} elementow za pomoca BubbleSort zajelo {stopwatch.ElapsedMilliseconds} milisekund. \n");

            stopwatch.Restart();
            stopwatch.Start();
            Sort.QuickSort(tab2);
            stopwatch.Stop();

            /* Console.WriteLine("\nTablica po sortowaniu QuickSort:");

            for (int i = 0; i < tab2.Length; i++)
            {
                Console.Write(tab2[i] + " ");
            } */

            Console.Write($"Sortowanie {len} elementow za pomoca QuickSort zajelo {stopwatch.ElapsedMilliseconds} milisekund.");
        }
    }
}