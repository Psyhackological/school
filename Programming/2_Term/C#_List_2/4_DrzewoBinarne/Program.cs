namespace DrzewoBinarne
{
    public class Program
    {
        public static void Main()
        {
            Random random = new Random();
            BinaryTree bt = new BinaryTree();

            for (int i = 0; i < 10; i++)
            {
                bt.AddNode(random.Next(-10, 11));
            }

            foreach (var x in bt.PreOrder())
            {
                Console.Write(x + " ");
            }

            Console.WriteLine($"\nIlość wierzchołków: {bt.CountNodes()}");
            Console.WriteLine($"Ilość poziomów: {bt.CountLevels()}");
            Console.WriteLine($"Suma wartości wszystkich wierzchołków: {bt.Sum()}");
            Console.WriteLine($"Minimalna wartość wierzchołka: {bt.Min()}");
            Console.WriteLine($"Maksymalna wartość wierzchołka: {bt.Max()}");

        }
    }
}