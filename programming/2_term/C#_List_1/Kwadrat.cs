namespace L1ZadEND
{
    internal class Kwadrat : IFigura
    {
        private double _bok;

        public Kwadrat(double a)
        {
            _bok = Math.Abs(a);
        }

        public double get_obwod()
        {
            return 4 * _bok;
        }

        public double get_pole()
        {
            return _bok * _bok;
        }

        public override String ToString()
        {
            return "Kwadrat: " + _bok;
        }

        public void Powieksz()
        {
            _bok *= Math.Sqrt(2);
        }

        public void Pomniejsz()
        {
            _bok /= Math.Sqrt(2);
        }
    }
}
