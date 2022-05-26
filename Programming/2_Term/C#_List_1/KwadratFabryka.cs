namespace L1ZadEND
{
    internal class KwadratFabryka : FiguraFabryka
    {
        public override IFigura Utworz(double a, double n=0)
        {
            return new Kwadrat(a);
        }
    }
}
