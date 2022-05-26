namespace L1ZadEND
{
    static class Program
    {
        static void Main()
        {
            Random rnd = new Random();
            List<IFigura> lista_figur = new List<IFigura>();
            Figura figura = new Figura();

            int choice=0;
            int x=0;
            int y=0;

            for (int i = 0; i < 10; i++)
            {
                lista_figur.Add(figura.WygenerujFigure((Figura.FiguraType)rnd.Next(1, 4), rnd.Next(1, 51), rnd.Next(1, 51)));
            }
            
            do
            {
                Console.WriteLine("1. Wyswietl liste figur.");
                Console.WriteLine("2. Wyswietl wybrana figure.");
                Console.WriteLine("3. Usun wybrana figure.");
                Console.WriteLine("4. Dodaj nowa figure.");
                Console.WriteLine("5. Pomniejsz wybrana figure.");
                Console.WriteLine("6. Powieksz wybrana figure.");
                Console.WriteLine("7. Wyjscie.");
                try
                {
                    Console.Write("\nNumerek: ");
                    choice = int.Parse(Console.ReadLine());

                    switch (choice)
                    {
                        case 1:
                            Console.WriteLine("Lista figur:");
                            int nr = 1;
                            foreach (var element in lista_figur)
                            {
                                Console.WriteLine(nr + ". " + element);
                                nr++;
                            }
                            Thread.Sleep(3000);
                            Console.Clear();
                            break;

                        case 2:
                            Console.Write("Podaj numer figury: ");
                            x = int.Parse(Console.ReadLine());
                            if (x <= 0 || x > lista_figur.Count)
                            {
                                Console.WriteLine("Wybrano numer figury spoza zakresu.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            else
                            {
                                Console.WriteLine(lista_figur[x-1]);
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            break;

                        case 3:
                            Console.Write("Podaj numer figury: ");
                            x = int.Parse(Console.ReadLine());
                            if (x <= 0 || x > lista_figur.Count)
                            {
                                Console.WriteLine("Wybrano numer figury spoza zakresu.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            else
                            {
                                lista_figur.RemoveAt(x-1);
                                Console.WriteLine("Usunieto figure.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            break;

                        case 4:
                            Console.Write("Podaj typ figury (1 - Kwadrat, 2 - Prostokat, 3 - Kolo):");
                            x = int.Parse(Console.ReadLine());
                            if (x == 1)
                            {
                                Console.Write("Podaj x:");
                                x = int.Parse(Console.ReadLine());
                                lista_figur.Add(figura.WygenerujFigure(Figura.FiguraType.Kwadrat, x, x));
                                Console.Write("Dodano figure.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            else if (x == 2)
                            {
                                Console.Write("Podaj x:");
                                x = int.Parse(Console.ReadLine());
                                Console.Write("Podaj y:");
                                y = int.Parse(Console.ReadLine());
                                lista_figur.Add(figura.WygenerujFigure(Figura.FiguraType.Prostokat, x, y));
                                Console.WriteLine("Dodano figure.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            else if (x == 3)
                            {
                                Console.Write("Podaj r:");
                                x = int.Parse(Console.ReadLine());
                                lista_figur.Add(figura.WygenerujFigure(Figura.FiguraType.Kolo, x, x));
                                Console.WriteLine("Dodano figure.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            else
                            {
                                Console.WriteLine("Wybrano nieistniejacy typ figury.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            break;

                        case 5:
                            Console.Write("Podaj numer figury: ");
                            x = int.Parse(Console.ReadLine());
                            if (x <= 0 || x > lista_figur.Count)
                            {
                                Console.WriteLine("Wybrano numer figury spoza zakresu.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            else
                            {
                                lista_figur[x-1].Pomniejsz();
                                Console.WriteLine("Zmniejszono figure.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            break;

                        case 6:
                            Console.Write("Podaj numer figury: ");
                            x = int.Parse(Console.ReadLine());
                            if (x <= 0 || x > lista_figur.Count)
                            {
                                Console.WriteLine("Wybrano numer figury spoza zakresu.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            else
                            {
                                lista_figur[x-1].Powieksz();
                                Console.WriteLine("Zwiekszono figure.");
                                Thread.Sleep(3000);
                                Console.Clear();
                            }
                            break;
                    }
                }
                catch
                {
                    Console.WriteLine("Podano znak nie bedacy liczba!");
                    Thread.Sleep(3000);
                    Console.Clear();
                }
            } while (choice != 7);
        }
    }
}
