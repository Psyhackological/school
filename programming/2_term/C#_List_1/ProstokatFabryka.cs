namespace L1ZadEND
{
    internal class ProstokatFabryka : FiguraFabryka
    {
        public override IFigura Utworz(double a, double b)
        {
            return new Prostokat(a, b);
        }
    }
}
