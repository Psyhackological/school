namespace L1ZadEND
{
    internal class Figura
    {
        public enum FiguraType
        {
            Kwadrat=1,
            Prostokat,
            Kolo
        }

        public IFigura? WygenerujFigure(FiguraType type, double x, double y)
        {
            switch(type)
            {
                case FiguraType.Kwadrat: // 1
                    KwadratFabryka kwadratFabryka = new KwadratFabryka();
                    return kwadratFabryka.Utworz(x, y);
                case FiguraType.Prostokat: // 2
                    ProstokatFabryka prostokatFabryka = new ProstokatFabryka();
                    return prostokatFabryka.Utworz(x, y);
                case FiguraType.Kolo: // 3
                    KoloFabryka koloFabryka = new KoloFabryka();
                    return koloFabryka.Utworz(x, y);
                default: // ?
                    return null;
            }
        }
    }
}
