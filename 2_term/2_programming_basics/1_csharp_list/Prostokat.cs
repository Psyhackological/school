namespace L1ZadEND
{
    internal class Prostokat : IFigura
    {
        private double _a;
        private double _b;

        public Prostokat(double x, double y)
        {
            _a = Math.Abs(x);
            _b = Math.Abs(y);
        }

        public double get_obwod()
        {
            return 2 * _a + 2 * _b;
        }

        public double get_pole()
        {
            return _a * _b;
        }

        public override String ToString()
        {
            return "Prostokat: " + _a + "x" + _b;
        }

        public void Powieksz()
        {
            _a *= Math.Sqrt(2);
            _b *= Math.Sqrt(2);
        }

        public void Pomniejsz()
        {
            _a /= Math.Sqrt(2);
            _b /= Math.Sqrt(2);
        }
    }
}
