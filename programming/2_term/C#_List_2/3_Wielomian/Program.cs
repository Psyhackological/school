namespace Wielomian;

public class Program
{
    public static void Main()
    {
        Wielomian w1 = new Wielomian(3);
        w1.WypelnijLosowymi();
        Console.WriteLine(w1.ToString());
        Console.WriteLine($"x = 4 => W(x) = {w1.ObliczHornerem(4)}");
        
        Console.WriteLine();
        
        Wielomian w2 = new Wielomian(2);
        w2.WypelnijZadanymi(1, 3, -6);
        Console.WriteLine(w2.ToString());
        Console.WriteLine($"x = 2 => W(x) = {w2.ObliczHornerem(2)}");
    }
}