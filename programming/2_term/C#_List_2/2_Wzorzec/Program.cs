namespace Wzorzec;

public class Program
{
    public static void Main()
    {
        Wzorzec wz1 = new Wzorzec("Ko", "Konrad Konieczny");
        wz1.SzukajPozycje();
        Console.WriteLine(wz1);

        Wzorzec wz2 = new Wzorzec("K", "Krol Karol Kupil Krolowej Karolinie Korale Koloru Kolarowego");
        wz2.SzukajPozycje();
        Console.WriteLine(wz2);

        Wzorzec wz3 = new Wzorzec("n", "konstantynopolitanczykowianeczka");
        wz3.SzukajPozycje();
        Console.WriteLine(wz3);
        
        Wzorzec wz4 = new Wzorzec("r", "Wyrewolwerowany rewolwerowiec wyrewolwerował swoj nie wyrewolwerowany rewolwer.");
        wz4.SzukajPozycje();
        Console.WriteLine(wz4);
        
        Wzorzec wz5 = new Wzorzec("wa", "Wyrewolwerowany rewolwerowiec wyrewolwerował swoj nie wyrewolwerowany rewolwer.");
        wz5.SzukajPozycje();
        Console.WriteLine(wz5);
    }
}