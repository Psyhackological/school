namespace L1ZadEND
{
    internal class KoloFabryka : FiguraFabryka
    {
        public override IFigura Utworz(double r, double n=0)
        {
            return new Kolo(r);
        }
    }
}
