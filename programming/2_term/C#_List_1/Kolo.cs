namespace L1ZadEND
{
    internal class Kolo : IFigura
    {
        private double _r;

        public Kolo(double promien)
        {
            _r = Math.Abs(promien);
        }

        public double get_obwod()
        {
            return 2 * Math.PI * _r;
        }

        public double get_pole()
        {
            return Math.PI * Math.Pow(_r, 2);
        }

        public override String ToString()
        {
            return "Kolo o promieniu: " + _r;
        }

        public void Powieksz()
        {
            _r *= Math.Sqrt(2);
        }

        public void Pomniejsz()
        {
            _r /= Math.Sqrt(2);
        }
    }
}
