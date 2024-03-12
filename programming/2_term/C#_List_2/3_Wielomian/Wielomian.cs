namespace Wielomian;

internal class Wielomian
{
    private int[] _tablicaWspolczynnikow;

    public Wielomian(int n)
    {
        if(0 > n)
        {
            throw new ArgumentException("Stopien wielomianu musi byc >0!");
        }
        _tablicaWspolczynnikow = new int[n+1];
    }

    public void WypelnijLosowymi()
    {
        Random r = new Random();

        for (int i = 0; i < _tablicaWspolczynnikow.Length; i++)
        {
            _tablicaWspolczynnikow[i] = r.Next(-9, 10);
        }
    }

    public void WypelnijZadanymi(params int[] wartosci)
    {
        if (wartosci.Length < _tablicaWspolczynnikow.Length)
        {
            throw new ArgumentException("Za malo argumentow!");
        }

        for (int i = 0; i < _tablicaWspolczynnikow.Length; i++)
        {
            _tablicaWspolczynnikow[i] = wartosci[i];
        }
    }

    public override string ToString()
    {
        string napis = "W(x) = ";

        for (int i = 0; i < _tablicaWspolczynnikow.Length; i++)
        {
            if (_tablicaWspolczynnikow.Length - 1 - i != 0)
            {
                napis += $"{_tablicaWspolczynnikow[i]}x^{_tablicaWspolczynnikow.Length - 1 - i}";
                if (_tablicaWspolczynnikow[i + 1] >= 0) napis += "+";
            }
            else
            {
                napis += _tablicaWspolczynnikow[i];
            }
        }
        return napis;
    }

    public int ObliczHornerem(int x)
    {
        int wynik = _tablicaWspolczynnikow[0];
 
        for (int i = 1; i < _tablicaWspolczynnikow.Length; i++)
        {
            wynik = wynik * x + _tablicaWspolczynnikow[i];
        }
 
        return wynik;
    }
}